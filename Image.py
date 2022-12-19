import cv2


class Image:
    def __init__(self, pathToImg) -> None:
        self.pathToImg = pathToImg
        pass

    def PrepareImg(self):
        img = cv2.imread(self.pathToImg)
        