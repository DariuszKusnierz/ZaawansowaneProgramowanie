from flask import Flask, request
from Movie import downloadMoviesData
from Link import downloadLinksData
from Rating import downloadRatingsData
from Tag import downloadTagsData

movieFile = 'movies.csv'
linkFile = 'links.csv'
ratingFile = 'ratings.csv'
tagFile = 'tags.csv'

app = Flask(__name__)


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
