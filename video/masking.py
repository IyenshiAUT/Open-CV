import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('img/nature.jpg')
if img is None:
    print("Image not found. Please check the path.")
    exit()

cv.imshow('Nature', img)

# Create a blank image (single-channel) for the mask
blank = np.zeros(img.shape[:2], dtype='uint8')

# Create a circular mask
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

# Apply the mask to the image
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)


rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
weird_shape = cv.bitwise_and(mask, rectangle)
masked_1 = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)
