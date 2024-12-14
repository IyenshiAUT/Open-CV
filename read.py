import cv2 as cv
'''
img1 = cv.imread('img/girl.jpg')
# read images
cv.imshow("Girl", img1)
# waiting
cv.waitKey()
'''


'''
capture = cv.VideoCapture('video/video1.mp4')
while True:
    isTure, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20)&0xFF==ord('a'):
        break

capture.release()
cv.destroyAllWindows()
'''


def rescales_frame(frame, scale=0.75):
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
capture = cv.VideoCapture('video/video1.mp4')
while True:
    isTure, frame = capture.read()
    frame_resized = rescales_frame(frame)
    cv.imshow('Video1', frame)
    cv.imshow('Video', frame_resized)
    
    if cv.waitKey(20)&0xFF==ord('a'):
        break

capture.release()
cv.destroyAllWindows() 

def change_res(width, height):  # live videp
    capture.set(3, width)
    capture.set(4, height)

    