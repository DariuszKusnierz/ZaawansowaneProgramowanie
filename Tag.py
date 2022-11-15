from flask_restful import Resource


class Tag(Resource):
    def __init__(self, userId, moveId, tag, timestamp) -> None:
        self.userId = userId
        self.moveId = moveId
        self.tag = tag
        self.timestamp = timestamp


def downloadTagsData(fileCSV):
    data = []
    with open(fileCSV, "r", encoding="utf-8") as content:
        for line in content:
            splittedData = line.split(",")
            data.append(Tag(splittedData[0], splittedData[1], splittedData[2], splittedData[3]).__dict__)
    return data
