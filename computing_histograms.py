import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('img/man.jpg')
cv.imshow('Man', img)
'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

plt.figure()
plt.title("Gray Scalse Histogram")
plt.xlabel("Bins")
plt.ylabel("No of Bins")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()



blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Create a circular mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title("Gray Scalse Histogram")
plt.xlabel("Bins")
plt.ylabel("No of Bins")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
'''


cv.waitKey()