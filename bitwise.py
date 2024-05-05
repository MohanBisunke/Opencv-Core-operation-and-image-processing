import cv2
import numpy as np

img1 = np.zeros((512,512,3), np.uint8)
cv2.rectangle(img1, pt1=(200,0), pt2=(300,100), thickness=-1, color=(255,255,255))

img2 = np.zeros((512,512,3), np.uint8)
cv2.rectangle(img2, pt1=(256,0), pt2=(512,512), thickness=-1, color=(255,255,255))

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1,img2)
bitnot = cv2.bitwise_not(img1)
bitXor = cv2.bitwise_xor(img1,img2)
while True:
    cv2.imshow('window1', img1)
    cv2.imshow('window2', img2)
    cv2.imshow('bitAnd', bitAnd)
    cv2.imshow('bitor', bitOr)
    cv2.imshow('bitnot', bitnot)
    cv2.imshow('bitXor', bitXor)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()
