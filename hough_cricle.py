import cv2
import numpy as np
import matplotlib.pyplot as plt

img =cv2.imread('img/balls.webp', cv2.IMREAD_GRAYSCALE)

blur = cv2.medianBlur(img,5)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,45,param1=60,param2=40,minRadius=0,maxRadius=0)
print(circles)

#returns the all found circles with their center and radius
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    
    cv2.circle(cimg,(i[0],i[1]),2,(0,255,0),2)
    
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
    