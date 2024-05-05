import cv2
import numpy as np
import time


video = cv2.VideoCapture('img/video.avi')

while True:
    ret, frame = video.read()
    time.sleep(1/20)
    cv2.imshow('webcam', frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()