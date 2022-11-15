from flask_restful import Resource


class Link(Resource):
    def __init__(self, movieId, imdbId, tmdbId) -> None:
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


def downloadLinksData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            splittedData = line.split(",")
            data.append(Link(splittedData[0], splittedData[1], splittedData[2]).__dict__)
    return data
