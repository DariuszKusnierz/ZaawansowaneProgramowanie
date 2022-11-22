import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'


def ConvertImage2String(image):
    img = cv2.imread(image)
    print(pytesseract.image_to_string(img, lang='eng'))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


ConvertImage2String('photo1.jpg')
ConvertImage2String('photo2.jpg')
ConvertImage2String('photo3.jpg')
ConvertImage2String('photo4.jpg')
ConvertImage2String('photo5.jpg')
