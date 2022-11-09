from flask import Flask, request
from flask_restful import Resource, Api

import os

movieFile = 'movies.csv'
linkFile = 'links.csv'
ratingFile = 'ratings.csv'
tagFile = 'tags.csv'

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}



api.add_resource(HelloWorld, '/')

class Movie(Resource):
    def __init__(self, id, title, genres) -> None:
        self.id = id
        self.title = title
        self.genres = genres

class Link(Resource):
    def __init__(self, movieId, imdbId, tmdbId) -> None:
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating(Resource):
    def __init__(self, userId, moveId, rating, timestamp) -> None:
        self.userId = userId
        self.moveId = moveId
        self.rating = rating
        self.timestamp = timestamp

class Tag(Resource):
    def __init__(self, userId, moveId, tag, timestamp) -> None:
        self.userId = userId
        self.moveId = moveId
        self.tag = tag
        self.timestamp = timestamp


def downloadMoviesData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            #data.append(tuple(line.split(",")))
            splittedData = line.split(",")
            data.append(Movie(splittedData[0],splittedData[1],splittedData[2]).__dict__)
    return data


def downloadLinksData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            #data.append(tuple(line.split(",")))
            splittedData = line.split(",")
            data.append(Link(splittedData[0], splittedData[1], splittedData[2]).__dict__)
    return data

def downloadRatingsData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            #data.append(tuple(line.split(",")))
            splittedData = line.split(",")
            data.append(Rating(splittedData[0],splittedData[1],splittedData[2], splittedData[3]).__dict__)
    return data

def downloadTagsData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            #data.append(tuple(line.split(",")))
            splittedData = line.split(",")
            data.append(Tag(splittedData[0],splittedData[1],splittedData[2], splittedData[3]).__dict__)
    return data

@app.route("/movies")
def movies():
    return downloadMoviesData(movieFile)

@app.route("/links")
def links():
    return downloadLinksData(linkFile)

@app.route("/ratings")
def ratings():
    return downloadRatingsData(ratingFile)

@app.route("/tags")
def tags():
    return downloadTagsData(tagFile)


if __name__ == '__main__':
    app.run(debug=True)

