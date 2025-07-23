from app import app
from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, fields, marshal_with
from app.models import Songs
import json
import pickle

api = Api(app)


class SongsList(Resource):
    def get(self, era):
        songs = Songs.query.filter_by(era=era).all()
        song_list = ([e.serialize() for e in songs])
        return song_list


api.add_resource(SongsList, "/SongList/<string:era>")







