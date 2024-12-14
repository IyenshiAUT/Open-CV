import cv2 as cv
import numpy as np

img = cv.imread('img/pretty.jpg')
cv.imshow("Pretty", img)

'''
#move image
def translate(img, x, y):
    transMat = np.float32([[1,0, x], [0,1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated_img = translate(img, 10, 10)
cv.imshow("Translated", translated_img)

#plus -> plus| down


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint==None:
        rotPoint=(width//2, height//2)
        
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)



flip = cv.flip(img, 0) # 0-x, 1-y, -1-both
cv.imshow("Flipped", flip)
'''



cv.waitKey()