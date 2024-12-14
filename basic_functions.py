import cv2 as cv

img = cv.imread('img/god.jpg')
cv.imshow('God', img)
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("God_", gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)


canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

dilated = cv.dilate(canny, (7,7,), iterations=7)
cv.imshow("Dilated", dilated)

erode = cv.erode(dilated, (7,7,), iterations=7)
cv.imshow("Erode", erode)


resized= cv.resize(img, (500, 500), interpolation=cv.INTER_AREA) #line, cubic
cv.imshow("Resized", resized)
'''

cropped = img[50:200, 150:500]
cv.imshow("Cropped", cropped)
cv.waitKey()