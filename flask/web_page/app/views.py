from flask import Flask, redirect, url_for, render_template
from app import app
from app.forms import EraForm
from flask_restful import Api, Resource
import requests


BASE = "http://0.0.0.0:80/"


@app.route('/', methods=['GET'])
def home():
    return redirect(url_for("era_selection"))


@app.route('/era_list/<era>', methods=['GET', 'POST'])
def era_list(era):
    song_list = requests.get(BASE + "SongList/" + era).json()
    return render_template("song_list.html", song_list=song_list)


@app.route('/era_selection', methods=['GET', 'POST'])
def era_selection():
    form = EraForm()
    if form.validate_on_submit():
        data = form.era.data
        return redirect(url_for('era_list', era=data))
    return render_template("era_form.html", form=form)


@app.route('/youtube_search/<song>', methods=['GET', 'POST'])
def youtube_search(song):

    search = 'https://www.googleapis.com/youtube/v3/search'

    # Retrieve search from YouTube API
    search_parameters = {
        'key': 'AIzaSyCDh90enZjxp_VYX1ZZyhBzzR8ixabGSSY',
        'part': 'id',
        'q': song,
        'maxResults': 1
    }

    # Store result in json format, then find video ID from dictionary
    req1 = requests.get(search, params=search_parameters)
    print(req1.text)
    video_id = req1.json()['items'][0]['id']['videoId']

    result = 'https://www.googleapis.com/youtube/v3/videos'

    # Retrieve result data from Youtube API
    result_parameter = {
        'key': 'AIzaSyCDh90enZjxp_VYX1ZZyhBzzR8ixabGSSY',
        'id': video_id,
        'part': 'snippet'
    }

    req2 = requests.get(result, params=result_parameter)
    video_data = req2.json()['items'][0]

    video_info = {
        'url': f"https://www.youtube.com/watch?v={video_data['id']}",
        'thumbnail': video_data['snippet']['thumbnails']['default']['url'],
        'title': video_data['snippet']['title']
    }
    return render_template("video_display.html", video_info=video_info)






