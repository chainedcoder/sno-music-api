import json
import js2py
from flask import Flask
import pafy
from ytmusicapi import YTMusic
from typing import List, Dict, Union

app = Flask(__name__)
eval_res, jsFile = js2py.run_file('yt_decipher.js')


# ytmusic = YTMusic('headers_auth.json')
ytmusic = YTMusic("headers_auth.json")

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


## ++++++++++++++  GET +++++++++++++
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
    print(songData)
    adpt_streams = songData["streamingData"]["adaptiveFormats"]
    sort_order = {258: 0, 256: 1, 172: 2, 251: 3, 141: 4, 171: 5, 140: 6, 250: 7, 249: 8, 139: 9, 303: 10, 302: 11, 299: 12, 298: 13, 278: 14, 272: 15, 271: 16, 266: 17, 264: 18, 248: 19, 247: 20, 246: 21, 245: 22, 244: 23, 243: 24, 242: 25, 219: 26, 218: 27, 170: 28, 169: 29, 168: 30, 167: 31, 160: 32, 138: 33, 137: 34, 136: 35, 135: 36, 134: 37, 133: 38}
    try:
        adpt_streams.sort(key=lambda x: sort_order[x["itag"]])
    except:
        pass
    return adpt_streams

@app.route("/get_stream/<video_id>/")
def get_stream_url(video_id):
    

    url = "https://www.youtube.com/watch?v=" + video_id
    # video = pafy.new(url)
    # streamURL = video.getbestaudio().url
    # print(video.getbestaudio().url)
    
    song = ytmusic.get_song(videoId = video_id)
    # print("********", getAudios(song))
    # best_audio = getAudios(song)[1]
    # ba_signature_cipher = best_audio["signatureCipher"]
    # streamURL = jsFile.decipher(ba_signature_cipher)
    # print(streamURL)
    return song #getAudios(song)

    # other_detail = song["microformat"]["microformatDataRenderer"]["videoDetails"]
    # result = { "videoId": video_id, "streamURL": streamURL, "duration": other_detail["durationSeconds"]  }
    # return result

@app.route("/")
@app.route("/mood/")
def get_mood_categories():
    # items =[ ] 
    # for group in ytmusic.get_mood_categories()["For you"]

    return json.dumps([{"For you":[{"params":"ggMPOg1uX2NpRFNoSVRjRElQ","title":"African"},{"params":"ggMPOg1uX2J1MDVJbDZxM2tO","title":"Pop"},{"params":"ggMPOg1uX3IxSk5vQWhUWUdR","title":"Romance"},{"params":"ggMPOg1uX2JxQ2hxc2J5UFhR","title":"R&B & Soul"},{"params":"ggMPOg1uX3ROaWVGeFdVRmdV","title":"2010s"},{"params":"ggMPOg1uXzJxenpkRkNOMk1y","title":"Black Lives Matter"}],"Genres":[{"params":"ggMPOg1uX2NpRFNoSVRjRElQ","title":"African"},{"params":"ggMPOg1uX0JFbU9QNXBBWldQ","title":"Arabic"},{"params":"ggMPOg1uX3pDQ1ZXWVB5SWE1","title":"Blues"},{"params":"ggMPOg1uX2hacTRJOU5KcndD","title":"Bollywood & Indian"},{"params":"ggMPOg1uX3Vmb2NXbUdLcHNU","title":"Brazilian"},{"params":"ggMPOg1uX3E1VnpSRHhLVElG","title":"Christian & Gospel"},{"params":"ggMPOg1uXzhnOElUNm9TY21k","title":"Classical"},{"params":"ggMPOg1uX0Y2bGpHeHhUUEtH","title":"Country & Americana"},{"params":"ggMPOg1uXzVLbmZnaWI4STNs","title":"Dance & Electronic"},{"params":"ggMPOg1uX3NjZllsNGVEMkZo","title":"Decades"},{"params":"ggMPOg1uXzMyY3J2SGM0bVh5","title":"Family"},{"params":"ggMPOg1uXzBTRFBmQ3N4b0R6","title":"Folk & Acoustic"},{"params":"ggMPOg1uX2E4aVJuU05GOVQ0","title":"Hip-Hop"},{"params":"ggMPOg1uX21NWWpBbU01SDgy","title":"Indie & Alternative"},{"params":"ggMPOg1uXzAwSjVITDBZckJR","title":"J-Pop"},{"params":"ggMPOg1uX3FJMlE0aDZWQWg5","title":"Jazz"},{"params":"ggMPOg1uX0JrbjBDOFFPSzJW","title":"K-Pop"},{"params":"ggMPOg1uX29wWTRjMHV1dWN5","title":"Latin"},{"params":"ggMPOg1uX2hXVUQwc0JTNXlE","title":"Mandopop & Cantopop"},{"params":"ggMPOg1uXzdlSXhKZ0hMV1Z4","title":"Metal"},{"params":"ggMPOg1uX2J1MDVJbDZxM2tO","title":"Pop"},{"params":"ggMPOg1uX2JxQ2hxc2J5UFhR","title":"R&B & Soul"},{"params":"ggMPOg1uX1lWbmVRNkFIa0k0","title":"Reggae & Caribbean"},{"params":"ggMPOg1uXzJKTm5jUEZ5Uzlu","title":"Rock"},{"params":"ggMPOg1uX2tDYW42Z0F0blRl","title":"Soundtracks & Musicals"}],"Moods & moments":[{"params":"ggMPOg1uXzJxenpkRkNOMk1y","title":"Black Lives Matter"},{"params":"ggMPOg1uXzVuc0dnZlhpV3Ba","title":"Chill"},{"params":"ggMPOg1uX2ozUHlwbWM3ajNq","title":"Commute"},{"params":"ggMPOg1uX1NhQU5LVGdGTkdo","title":"Energy Boosters"},{"params":"ggMPOg1uXzZQbDB5eThLRTQ3","title":"Feel Good"},{"params":"ggMPOg1uX1JNQmpISHRnczVF","title":"Focus"},{"params":"ggMPOg1uXzQ2UUV2Um13S3Jn","title":"Holiday"},{"params":"ggMPOg1uXzRJcVprRXdGMzVz","title":"Party"},{"params":"ggMPOg1uX1YzRjl4a2NKajkx","title":"Pride"},{"params":"ggMPOg1uX3IxSk5vQWhUWUdR","title":"Romance"},{"params":"ggMPOg1uX1AyU0U4UnRYVXpv","title":"Sleep"},{"params":"ggMPOg1uXzhZNkhXNUlFb3pV","title":"Workout"}]}])

@app.route("/mood/<mood_key>/")
def get_mood_playlists(mood_key):
    """
    mood_key is `param` retrieved from get_mood_categories --> /mood/
    """
    print(mood_key)
    
    return json.dumps(ytmusic.get_mood_playlists(params=mood_key))#json.dumps(ytmusic.get_mood_playlists(params=mood_key))

@app.route("/mood/<mood_key>/all/")
def get_mood_playlists_all_songs(mood_key):
    """
    mood_key is `param` retrieved from get_mood_categories --> /mood/
    """
    all_songs = []
    print("ALL songs")
    playlists = ytmusic.get_mood_playlists(params=mood_key)[:2]
    for playlist in playlists:
        all_songs += ytmusic.get_playlist(playlist["playlistId"])["tracks"]
    
    
    return json.dumps(all_songs)#json.dumps(ytmusic.get_mood_playlists(params=mood_key))


@app.route("/charts/")
def get_charts(country: str = 'ZZ'):
    """
    Get latest charts data from YouTube Music: Top songs, top videos, top artists and top trending videos. Global charts have no Trending section, US charts have an extra Genres section with some Genre charts.
    """
    return {"charts": ytmusic.get_charts(country) }


@app.route("/liked/")
def get_liked_songs():
    """
    Gets playlist items for the ‘Liked Songs’ playlist
    """
    return {"liked_songs": ytmusic.get_liked_songs() }


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
def rate_song(videoId: str, rating: str = 'INDIFFERENT') :
    """
    Rates a song (“thumbs up”/”thumbs down” interactions on YouTube Music)
    """
    return ytmusic.rate_song(videoId, rating) 

@app.route("/subscribe/<channelIds>")
def subscribe_artists(channelIds: List[str]) :
    """
    Subscribe to artists. Adds the artists to your library
    """
    return ytmusic.subscribe_artists(channelIds) 

@app.route("/unsubscribe/<channelIds>")
def unsubscribe_artists(channelIds: List[str]) :
    """

    """
    return ytmusic.unsubscribe_artists(channelIds) 

@app.route("/playlist/<playlistId>/")
def get_playlist(playlistId: str):
    """
    """
    return ytmusic.get_playlist(playlistId)


@app.route("/playlist/add/<playlistId>/<videoIds>/")
def add_playlist_items(playlistId: str, videoIds: List[str] = None):
    """
  
    """
    return ytmusic.add_playlist_items(playlistId, videoIds=videoIds)

@app.route("/playlist/remove/<playlistId>/<videoIds>/")
def remove_playlist_items(playlistId: str, videos: List[Dict]):
    """
  
    """
    return ytmusic.remove_playlist_items(playlistId=playlistId, videos=videos)



pafy.decipherer("s=l4IAIPNyurQliF4VvfIOr-957MUEv7Zf5x3y47FIsK6kDHICkhk64BUsBapbUBi4etk7XtpAtd3extOXkJ3_hMh8JkDgIARw8JQ0qOA&sp=sig&url=https://rr3---sn-p5qlsndr.googlevideo.com/videoplayback%3Fexpire%3D1640264694%26ei%3Dlh_EYej8B4KG8wSbvYe4AQ%26ip%3D35.199.51.57%26id%3Do-AMKAoO3fhyCtY29DgibZC7eTQUu2mhHvA1V6cdUoorPJ%26itag%3D134%26source%3Dyoutube%26requiressl%3Dyes%26mh%3DfP%26mm%3D31%252C26%26mn%3Dsn-p5qlsndr%252Csn-ab5l6nzr%26ms%3Dau%252Conr%26mv%3Dm%26mvi%3D3%26pl%3D20%26ctier%3DA%26pfa%3D5%26gcr%3Dus%26hightc%3Dyes%26vprv%3D1%26mime%3Dvideo%252Fmp4%26ns%3DnLJcV5wCJc0msQ6f2P_D--4G%26gir%3Dyes%26clen%3D1157003%26dur%3D201.040%26lmt%3D1565521630163241%26mt%3D1640242861%26fvip%3D3%26keepalive%3Dyes%26fexp%3D24001373%252C24007246%26c%3DWEB_REMIX%26txp%3D1311222%26n%3DGvYcfmzEWEJA3oI6F%26sparams%3Dexpire%252Cei%252Cip%252Cid%252Citag%252Csource%252Crequiressl%252Cctier%252Cpfa%252Cgcr%252Chightc%252Cvprv%252Cmime%252Cns%252Cgir%252Cclen%252Cdur%252Clmt%26lsparams%3Dmh%252Cmm%252Cmn%252Cms%252Cmv%252Cmvi%252Cpl%26lsig%3DAG3C_xAwRgIhAKbJLWXW-TXihXovvf5jGqmiDkhGuXHyoK0UOwSo1aD8AiEAiMGmg1P8AbhchX3xKsOZ2aF6vbzpZv5u3AoHgH_2IrU%253D")

