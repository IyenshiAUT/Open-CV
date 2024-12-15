import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img/man.jpg')
cv.imshow('Man', img)

# Average Blur
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)


# Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian_Blur", gaussian_blur)

#Median Blur
median_blur = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median_blur)

#Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 255)
cv.imshow("Bilateral", bilateral)
cv.waitKey()