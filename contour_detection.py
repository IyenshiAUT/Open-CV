import cv2 as cv
import numpy as np

img = cv.imread('img/pretty.jpg')
cv.imshow("Pretty", img)
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.blur(gray, (7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 125)
cv.imshow("canny", canny)
'''

ret, thresh = cv.threshold(img, 5,67, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))