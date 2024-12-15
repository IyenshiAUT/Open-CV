import cv2 as cv
import numpy as np

img = cv.imread('img/pretty.jpg')
cv.imshow("Pretty", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

threshhold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

threshhold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresh', thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adapt Thresh', adaptive_thresh)



cv.waitKey()