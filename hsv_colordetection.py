import cv2
import numpy as np


def nothing(x):
    pass

#cap = cv2.VideoCapture() for videos
cv2.namedWindow('Tracking')

cv2.createTrackbar('lh', 'Tracking', 0,255, nothing)
cv2.createTrackbar('ls', 'Tracking', 0,255, nothing)
cv2.createTrackbar('lv', 'Tracking', 0,255, nothing)

cv2.createTrackbar('hh', 'Tracking', 255,255, nothing)
cv2.createTrackbar('hs', 'Tracking', 255,255, nothing)
cv2.createTrackbar('hv', 'Tracking', 255,255, nothing)


while True:
    
    img = cv2.imread('img/balls.webp')
    img = cv2.resize(img, (600,512))
    
    # _, ref = cap.read() #for videos
    
    
    hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lh = cv2.getTrackbarPos('lh', 'Tracking')
    ls = cv2.getTrackbarPos('ls', 'Tracking')
    lv = cv2.getTrackbarPos('lv', 'Tracking')
    
    hh = cv2.getTrackbarPos('hh', 'Tracking')
    hs = cv2.getTrackbarPos('hs', 'Tracking')
    hv = cv2.getTrackbarPos('hv', 'Tracking')
    
    lb = np.array([lh, ls, lv])
    hb = np.array([hh, hs, hv])
    
    mask = cv2.inRange(hsv, lb, hb)
    
    res = cv2.bitwise_and(img, img,mask=mask)
    
    
    
    cv2.imshow('image', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

#cap.relase()  for video
cv2.destroyAllWindows()