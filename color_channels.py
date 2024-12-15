import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img/man.jpg')
cv.imshow('Man', img)

b, g, r = cv.split(img)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

merged = cv.merge([b,g,r])
cv.imshow("Merged Image", merged)


blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

cv.waitKey()