import cv2
import numpy as np

video = cv2.VideoCapture(0) #default webcam

fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('img/video.avi',fourcc,20.0,(500,500))

while True:
    
    ret, frame = video.read()
    out.write(frame) #saving frame
    
    cv2.imshow('webcam', frame) #frame is np array
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
   
out.release() 
cv2.destroyAllWindows()