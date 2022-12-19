import imutils
import cv2

# Initializing the HOG person 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 
#hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())

#hog = cv2.HOGDescriptor('WinSize',[48,48*2], 'NLevels',13, 'GammaCorrection',True)
#hog.SvmDetector = 'DaimlerPeopleDetector'
#opts = {'HitThreshold',1.4, 'WinStride',[8,8], 'Padding',[0,0], 'Scale',1.05, 'FinalThreshold',8}


def CheckImage(image):
    # Reading the Image 
    image = cv2.imread('example4.jpg') 
    con_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Resizing the Image 
    image = imutils.resize(image, width=min(600, image.shape[1])) 
   
    # Detecting all humans 
    (humans, _) = hog.detectMultiScale(image,  winStride=(5, 5), padding=(3, 3), scale=1.08)
    # getting no. of human detected
    print('Human Detected : ', len(humans))
   
    # Drawing the rectangle regions
    for (x, y, w, h) in humans: 
        cv2.rectangle(image, (x, y),  
                    (x + w, y + h),  
                    (0, 0, 255), 2) 
  
    # Displaying the output Image 
    #return image
    cv2.imwrite("IMG/img.jpg", image)
    #cv2.imshow("Image", image) 
    #cv2.waitKey(0)


#def SaveImgInMemory(image):
    #obj = io.BytesIO()
    #image (obj, format="jpg")
    #obj.seek(0)
    #return obj
