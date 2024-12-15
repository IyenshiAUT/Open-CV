import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/man.jpg')
cv.imshow('Man', img)
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

plt.imshow(img)
plt.show()
'''

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

cv.waitKey()