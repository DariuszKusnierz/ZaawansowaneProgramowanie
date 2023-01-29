import numpy as np
import cv2 as cv
import imutils

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


def CheckImage(userImg):
    #userImg = imutils.resize(userImg, width=min(600, userImg.shape[1]))
    (humans, _) = hog.detectMultiScale(userImg,  winStride=(5, 5), padding=(3, 3), scale=1.08)
    for (x, y, w, h) in humans: 
        cv.rectangle(userImg, (x, y),  
                    (x + w, y + h),  
                    (0, 0, 255), 2) 
    #gray = cv.cvtColor(userImg, cv.COLOR_BGR2GRAY)
    cv.imshow("userImg", userImg)


video = cv.VideoCapture(0)

if not video.isOpened():
    exit()

while True:
    ret, frame = video.read()

    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    #cv.imshow("frame", gray)
    CheckImage(frame)
    if cv.waitKey(1) == ord('q'):
        break

video.release()
cv.destroyAllWindows()


