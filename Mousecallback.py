import cv2
import numpy as np

img = np.zeros((512,512,3))


def drawshape(event, x,y,glags,params):
    if event ==1: #mouse click=1, move=0, unclick =4
        cv2.circle(img,center=(x,y),radius=100, thickness=3,color=(0,255,0))

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window', drawshape) #sends x,y location of mouse.

while True:
    cv2.imshow('window', img)
    
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break
cv2.destroyAllWindows()