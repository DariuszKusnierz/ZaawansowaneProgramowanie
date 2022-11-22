import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'


def ConvertImage2String(image):
    img = cv2.imread(image)
    print(pytesseract.image_to_string(img, lang='eng'))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#ConvertImage2String('photo1.jpg')
#ConvertImage2String('photo2.jpg')
#ConvertImage2String('photo3.jpg')
#ConvertImage2String('photo4.jpg')
#ConvertImage2String('photo5.jpg')


def ConvertImage2StringWithPreprocessing(image):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    converted_img_method_1 = cv2.threshold(cv2.GaussianBlur(gray_img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    converted_img_method_2 = cv2.threshold(cv2.bilateralFilter(gray_img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    converted_img_method_3 = cv2.threshold(cv2.medianBlur(gray_img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    converted_img_method_4 = cv2.adaptiveThreshold(cv2.GaussianBlur(gray_img, (5, 5), 0), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    converted_img_method_5 = cv2.adaptiveThreshold(cv2.bilateralFilter(gray_img, 9, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    converted_img = cv2.adaptiveThreshold(cv2.medianBlur(gray_img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    print(pytesseract.image_to_string(converted_img_method_2, lang='eng'))

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


ConvertImage2StringWithPreprocessing('photo1.jpg')
ConvertImage2StringWithPreprocessing('photo2.jpg')
ConvertImage2StringWithPreprocessing('photo3.jpg')
ConvertImage2StringWithPreprocessing('photo4.jpg')
ConvertImage2StringWithPreprocessing('photo5.jpg')