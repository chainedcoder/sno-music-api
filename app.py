import json
import js2py
import subprocess
from flask import Flask, request, jsonify, Response, send_file, send_from_directory
import yt_dlp
import os
from ytmusicapi import YTMusic
from typing import List, Dict, Union
import subprocess
from os import environ
import sys
import selectors
import io
from typing import Tuple
from dotenv import load_dotenv

load_dotenv()

HOST = environ.get("HOST")

app = Flask(__name__)
eval_res, jsFile = js2py.run_file("yt_decipher.js")


# ytmusic = YTMusic('headers_auth.json')
headers_auth_path = "/etc/secrets/headers_auth.json"
if not os.path.exists(headers_auth_path):
    headers_auth_path = "headers_auth.json"
    if not os.path.exists(headers_auth_path):
        raise Exception("headers_auth.json not found")

ytmusic = YTMusic(headers_auth_path)


def run_command(command: str, shell=True, stdout=subprocess.PIPE) -> Tuple[int, str]:

    proc = subprocess.Popen(command, shell=shell, stdout=stdout, stderr=subprocess.PIPE)

    sel = selectors.DefaultSelector()
    for fobj in [proc.stdout, proc.stderr]:
        os.set_blocking(fobj.fileno(), False)
        sel.register(fobj, selectors.EVENT_READ)

    out = io.StringIO()
    err = io.StringIO()

    # loop until all descriptors removed
    while len(sel.get_map()) > 0:
        events = sel.select()
        if len(events) == 0:
            # timeout or signal, kill to prevent wait hanging
            proc.terminate()
            break
        for key, _ in events:
            # read all available data
            buf = key.fileobj.read().decode(errors="ignore")
            if buf == "":
                sel.unregister(key.fileobj)
            elif key.fileobj == proc.stdout:
                sys.stdout.write(buf)
                sys.stdout.flush()
                out.write(buf)
            elif key.fileobj == proc.stderr:
                sys.stderr.write(buf)
                sys.stderr.flush()
                err.write(buf)

    sel.close()
    proc.wait()
    if proc.returncode != 0:
        return (proc.returncode, err.getvalue())
    return (0, out.getvalue())


## ++++++++  OBTAIN HEADER +++++++++
## +++++++++++++++++++++++++++++++++
@app.route("/headers/", methods=["POST"])
def headers_auth():
    # get raw_header from posted data
    raw_header = request.form.get("raw_header")
    headers_to_paste_in_headers_auth_file = YTMusic.setup(
        filepath=headers_auth_path,
        headers_raw=raw_header,  # raw value of headers copying from chrom -> look for browse? and copy headers from accept: */* to the end of section
    )
    return headers_to_paste_in_headers_auth_file


## ++++++++++++  SEARCH ++++++++++++
## +++++++++++++++++++++++++++++++++
@app.route("/search/<search_key>/")
def search(search_key):
    album = ytmusic.search(search_key)
    return album


@app.route("/artist/search/<artist>/")
def search_artist(artist):
    artists = ytmusic.search(artist, filter="artists")
    return artists


@app.route("/song/search/<song>/")
def search_song(song):
    songs = ytmusic.search(song, filter="songs")
    return songs


@app.route("/album/search/<album>/")
def search_album(album):
    albums = ytmusic.search(album, filter="albums")
    return albums


## ++++++++++  GET ARTIST ++++++++++
## +++++++++++++++++++++++++++++++++
@app.route("/artist/get/<artist_id>/")
def get_artist(artist_id):
    artist = ytmusic.get_artist(artist_id)
    # results = "".join([f"<p>{result}</p>" for result in search_results])
    return artist


@app.route("/artist/get/<artist_id>/")
def get_artist_albums(artist_id):
    albums = ytmusic.get_artist_albums(artist_id)
    # results = "".join([f"<p>{result}</p>" for result in search_results])
    return albums


@app.route("/album/get/<song_id>/")
def get_lyrics(browse_id):
    """
    Parameters:	browseId – Lyrics browse id obtained from get_watch_playlist
    Returns:	Dictionary with song lyrics.
    """
    songs = ytmusic.get_lyrics(browse_id)
    return songs


def getAudios(songData):
    # print(songData)
    adpt_streams = songData["streamingData"]["adaptiveFormats"]
    sort_order = {
        258: 0,
        256: 1,
        172: 2,
        251: 3,
        141: 4,
        171: 5,
        140: 6,
        250: 7,
        249: 8,
        139: 9,
        303: 10,
        302: 11,
        299: 12,
        298: 13,
        278: 14,
        272: 15,
        271: 16,
        266: 17,
        264: 18,
        248: 19,
        247: 20,
        246: 21,
        245: 22,
        244: 23,
        243: 24,
        242: 25,
        219: 26,
        218: 27,
        170: 28,
        169: 29,
        168: 30,
        167: 31,
        160: 32,
        138: 33,
        137: 34,
        136: 35,
        135: 36,
        134: 37,
        133: 38,
    }
    try:
        adpt_streams.sort(key=lambda x: sort_order[x["itag"]])
    except:
        pass
    return adpt_streams


@app.route("/get_stream/<video_id>/")
def get_stream_url(video_id):
    if video_id == "--" or not video_id:
        return json.dumps({"error": "video_id is empty"})

    url = "https://www.youtube.com/watch?v=" + video_id
    # video = pafy.new(url)
    # streamURL = video.getbestaudio().url

    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "outtmpl": f"videos/in/{video_id}.%(ext)s",
        "overwrites": True,
        "postprocessors": [
            # {
            #     "key" : "FFmpegVideoConvertor",
            #     "preferedformat" : "mp4",
            # },
            # {
            #     'key':'FFmpegMetadata',
            #     'add_metadata': True,
            # },
            # {
            #     "key": "Exec",
            #     "exec_cmd": f'cp videos/in/{video_id}.m4a videos/in/{video_id}_tmp.m4a && ffmpeg -y -i "videos/in/{video_id}_tmp.m4a" -c:a aac -b:a 128k -muxdelay 0 -f segment -sc_threshold 0 -segment_time 7 -segment_list "videos/hls/{video_id}.m3u8" -segment_format mpegts "videos/hls/{video_id}-%d.m4a" && rm videos/in/{video_id}_tmp.m4a ',
            # },
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ## check if videos/in/{video_id}.m4a exists and skip if it does
        download = False
        if not os.path.exists(f"videos/in/{video_id}.m4a"):
            download = True
        song_info = ydl.extract_info(url, download=download)

    # Check if videos/hls/{video_id}.m3u8 exists and skip if it does
    if not os.path.exists(f"videos/hls/{video_id}.m3u8"):
        command = f"ffmpeg -y -i 'videos/in/{video_id}.m4a' -c:a aac -b:a 128k -muxdelay 0 -f segment -sc_threshold 0 -segment_time 7 -segment_list 'videos/hls/{video_id}.m3u8' -segment_format mpegts 'videos/hls/{video_id}-%d.m4a'"
        process = run_command(command, shell=True, stdout=subprocess.PIPE)

        # while True:
        #     output = process.stdout.readline()
        #     if output == "" and process.poll() is not None:
        #         break
        #     if output:
        #         print(output.strip())

    result = {
        "videoId": video_id,
        "streamURL": f"{HOST}/stream/{video_id}",
        "duration": str(song_info["duration"]),
        "durationString": song_info["duration_string"],
    }
    print(result)

    return jsonify([result])


@app.route("/stream/<stream_id>/")
def stream(stream_id):
    print("Stream: ", stream_id)
    return send_from_directory(
        directory="videos/hls",
        path=f"{stream_id}.m3u8",
        mimetype="application/x-mpegURL",
    )


@app.route("/stream/<stream_id>/<path:path>")
def video(stream_id, path):
    print("Stream: ", stream_id)
    return send_from_directory(directory="videos/hls", path=path)


@app.route("/")
@app.route("/mood/")
def get_mood_categories():
    # items =[ ]
    # for group in ytmusic.get_mood_categories()["For you"]
    # print("***", ytmusic.get_mood_categories())
    return json.dumps([ytmusic.get_mood_categories()])


@app.route("/mood/<mood_key>/")
def get_mood_playlists(mood_key):
    """
    mood_key is `param` retrieved from get_mood_categories --> /mood/
    """
    print(mood_key)
    # print(ytmusic.get_mood_playlists(params=mood_key))

    return json.dumps(ytmusic.get_mood_playlists(params=mood_key))


@app.route("/mood/<mood_key>/all/")
def get_mood_playlists_all_songs(mood_key):
    """
    mood_key is `param` retrieved from get_mood_categories --> /mood/
    """
    all_songs = []
    print("ALL songs at mood_key:", mood_key)
    playlists = ytmusic.get_mood_playlists(params=mood_key)[:2]
    for playlist in playlists:
        all_songs += ytmusic.get_playlist(playlist["playlistId"])["tracks"]

    return json.dumps(
        all_songs
    )  # json.dumps(ytmusic.get_mood_playlists(params=mood_key))


@app.route("/charts/")
def get_charts(country: str = "ZZ"):
    """
    Get latest charts data from YouTube Music: Top songs, top videos, top artists and top trending videos. Global charts have no Trending section, US charts have an extra Genres section with some Genre charts.
    """
    return {"charts": ytmusic.get_charts(country)}


@app.route("/liked/")
def get_liked_songs():
    """
    Gets playlist items for the ‘Liked Songs’ playlist
    """
    return {"liked_songs": ytmusic.get_liked_songs()}


@app.route("/recently-played/")
def get_history():
    """
    Gets your play history in reverse chronological order
    """
    return json.dumps(ytmusic.get_history()[:10])


@app.route("/recently-played/remove/<feedbackTokens>")
def remove_history_items(feedbackTokens: List[str]):
    """
    Parameters:	feedbackTokens – Token to identify the item to remove, obtained from get_history()
    """
    return ytmusic.remove_history_items(feedbackTokens)


@app.route("/rate-song/<videoId>/<rating>")
def rate_song(videoId: str, rating: str = "INDIFFERENT"):
    """
    Rates a song (“thumbs up”/”thumbs down” interactions on YouTube Music)
    """
    return ytmusic.rate_song(videoId, rating)


@app.route("/subscribe/<channelIds>")
def subscribe_artists(channelIds: List[str]):
    """
    Subscribe to artists. Adds the artists to your library
    """
    return ytmusic.subscribe_artists(channelIds)


@app.route("/unsubscribe/<channelIds>")
def unsubscribe_artists(channelIds: List[str]):
    """ """
    return ytmusic.unsubscribe_artists(channelIds)


@app.route("/playlist/<playlistId>/")
def get_playlist(playlistId: str):
    """ """
    return ytmusic.get_playlist(playlistId)


@app.route("/playlist/add/<playlistId>/<videoIds>/")
def add_playlist_items(playlistId: str, videoIds: List[str] = None):
    """ """
    return ytmusic.add_playlist_items(playlistId, videoIds=videoIds)


@app.route("/playlist/remove/<playlistId>/<videoIds>/")
def remove_playlist_items(playlistId: str, videos: List[Dict]):
    """ """
    return ytmusic.remove_playlist_items(playlistId=playlistId, videos=videos)


# pafy.decipherer("s=l4IAIPNyurQliF4VvfIOr-957MUEv7Zf5x3y47FIsK6kDHICkhk64BUsBapbUBi4etk7XtpAtd3extOXkJ3_hMh8JkDgIARw8JQ0qOA&sp=sig&url=https://rr3---sn-p5qlsndr.googlevideo.com/videoplayback%3Fexpire%3D1640264694%26ei%3Dlh_EYej8B4KG8wSbvYe4AQ%26ip%3D35.199.51.57%26id%3Do-AMKAoO3fhyCtY29DgibZC7eTQUu2mhHvA1V6cdUoorPJ%26itag%3D134%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DfP%26mm%3D31%252C26%26mn%3Dsn-p5qlsndr%252Csn-ab5l6nzr%26ms%3Dau%252Conr%26mv%3Dm%26mvi%3D3%26pl%3D20%26ctier%3DA%26pfa%3D5%26gcr%3Dus%26hightc%3Dyes%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DnLJcV5wCJc0msQ6f2P_D--4G%26gir%3Dyes%26clen%3D1157003%26dur%3D201.040%26lmt%3D1565521630163241%26mt%3D1640242861%26fvip%3D3%26keepalive%3Dyes%26fexp%3D24001373%252C24007246%26c%3DWEB_REMIX%26txp%3D1311222%26n%3DGvYcfmzEWEJA3oI6F%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cctier%252Cpfa%252Cgcr%252Chightc%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%26lsig%3DAG3C_xAwRgIhAKbJLWXW-TXihXovvf5jGqmiDkhGuXHyoK0UOwSo1aD8AiEAiMGmg1P8AbhchX3xKsOZ2aF6vbzpZv5u3AoHgH_2IrU%253D")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
