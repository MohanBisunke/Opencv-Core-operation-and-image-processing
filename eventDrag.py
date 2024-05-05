import cv2
import numpy as np

img = np.zeros((512,512,3))

flag = False
ix =-1
iy=-1

def drawshape(event, x,y,flags,params):
    
    global flag,ix,iy
    
    if event ==1:
        flag =True
        ix=x
        iy=y
        img.fill(0)
    elif event ==0:
        if flag ==True:
            cv2.rectangle(img, pt1=(ix,iy), pt2=(x,y), thickness=1, color=(0,255,255))
    elif event ==4:
        flag =False
        cv2.rectangle(img,pt1=(ix,iy), pt2=(x,y), thickness=1, color=(255,0,0))

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window', drawshape) #sends x,y location of mouse.

while True:
    cv2.imshow('window', img)
    
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cv2.destroyAllWindows()