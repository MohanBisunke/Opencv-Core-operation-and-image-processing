import cv2
import numpy as np

img = np.zeros((900,900,3))

#rectange
cv2.rectangle(img, pt1=(100,100), pt2=(300,300), color=(255,0,0), thickness=3)
cv2.rectangle(img, pt1=(400,100),pt2=(700,300),color=(0,255,0),thickness=-1) #fill rectangel


#circle

cv2.circle(img,center=(200,500), radius=100, color=(0,0,255), thickness=2)
cv2.circle(img,center=(550,500), radius=100,color=(0,0,255), thickness=-1)

#line
cv2.line(img,pt1=(0,0), pt2=(900,900), color=(0,255,0), thickness=2)
cv2.line(img,pt1=(900,0), pt2=(0,900),thickness=2,color=(0,255,0))

#text

cv2.putText(img,org=(100,350), fontFace=cv2.FONT_ITALIC, lineType=cv2.LINE_AA, fontScale=1, thickness=2,color=(0,255,255),text='Rectangle1')
cv2.putText(img, org=(400,350), lineType=cv2.LINE_AA, fontFace=cv2.FONT_ITALIC ,fontScale=1, thickness=2, color=(255,0,0), text='Rectangle2')
cv2.putText(img,org=(150,650), fontFace=cv2.FONT_ITALIC, lineType=cv2.LINE_AA, fontScale=1, thickness=2,color=(0,255,255),text='Circle1')
cv2.putText(img, org=(500,650), lineType=cv2.LINE_8, fontFace=cv2.FONT_ITALIC ,fontScale=1, thickness=2, color=(255,0,0), text='Circle2')



cv2.imshow('window',img)


cv2.waitKey(0)