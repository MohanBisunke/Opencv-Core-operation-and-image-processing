import cv2
import numpy as np

def callbackfunction(x):
    print(x)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('window')

cv2.createTrackbar('trackbarb' ,'window', 0,255, callbackfunction)
cv2.createTrackbar('trackbarg' ,'window', 0,255, callbackfunction)
cv2.createTrackbar('trackbarr' ,'window', 0,255, callbackfunction)

switch = '0: OFF \n 1: ON'
cv2.createTrackbar(switch, 'window', 0,1,callbackfunction)

while True:
    cv2.imshow('window', img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
    b = cv2.getTrackbarPos('trackbarb' ,'window')
    g = cv2.getTrackbarPos('trackbarg', 'window')
    r = cv2.getTrackbarPos('trackbarr', 'window')
    s = cv2.getTrackbarPos(switch, 'window')
    
    if s ==0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv2.destroyAllWindows()
