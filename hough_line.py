import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/adaptive.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,10,150,apertureSize=3)

lines = cv2.HoughLines(edges,1, np.pi/180,100)

linep =cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines :
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    
    x0 = a * rho
    y0 = b * rho
    
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000 *(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000* (a))
    
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
    
    
for l in linep:
    x1,x2,y1,y2 = l[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


while True:
    cv2.imshow('image', img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    ()
cv2.destroyAllWindows