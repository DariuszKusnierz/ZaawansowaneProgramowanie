from flask_restful import Resource


class Movie(Resource):
    def __init__(self, id, title, genres) -> None:
        self.id = id
        self.title = title
        self.genres = genres


def downloadMoviesData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            splittedData = line.split(",")
            data.append(Movie(splittedData[0], splittedData[1], splittedData[2]).__dict__)
    return data
