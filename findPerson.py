import imutils
import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def CheckImage(userImg):
    image = cv2.imread(userImg)
    image = imutils.resize(image, width=min(600, image.shape[1]))
    (humans, _) = hog.detectMultiScale(image,  winStride=(5, 5), padding=(3, 3), scale=1.08)
    for (x, y, w, h) in humans: 
        cv2.rectangle(image, (x, y),  
                    (x + w, y + h),  
                    (0, 0, 255), 2) 

    cv2.imwrite("static/IMG/img.jpg", image)



#def SaveImgInMemory(image):
    #obj = io.BytesIO()
    #image (obj, format="jpg")
    #obj.seek(0)
    #return obj
