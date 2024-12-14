import cv2 as cv
import numpy as np
'''
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

blank[:] = 0,255,0
cv.imshow("Green", blank)

blank[230:300, 450:500] = 0,0,250
cv.imshow("Square", blank)
'''


blank = np.zeros((500, 500, 3), dtype='uint8')

'''
cv.rectangle(blank, (0,0), (250, 250), (0,0,255), thickness=-1) #thickness = 1, -1, cv.FILLED
cv.imshow("Rectangle", blank)

cv.circle(blank, (250, 250), radius=100, color=(0,0, 255), thickness=-3 )
cv.imshow("Circle", blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), 2)
cv.imshow("Line", blank)
'''
cv.putText(blank, "Taneesha Iyenshi", (125, 250), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,255), 2)
cv.imshow("Text", blank)
cv.waitKey()

