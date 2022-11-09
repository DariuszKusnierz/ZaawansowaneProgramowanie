from flask_restful import Resource

class Rating(Resource):
    def __init__(self, userId, moveId, rating, timestamp) -> None:
        self.userId = userId
        self.moveId = moveId
        self.rating = rating
        self.timestamp = timestamp


def downloadRatingsData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            #data.append(tuple(line.split(",")))
            splittedData = line.split(",")
            data.append(Rating(splittedData[0],splittedData[1],splittedData[2], splittedData[3]).__dict__)
    return data