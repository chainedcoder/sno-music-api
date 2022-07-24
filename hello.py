from flask import Flask
from ytmusicapi.ytmusic import YTMusic
app = Flask(__name__)

@app.route("/")
def home():
    return "<p> Testing </>"