import cv2
import numpy as np




image = cv2.imread('img/add1.jpg')
image2  = cv2.imread('img/fig.png')
image = cv2.resize(image, (500,400))
image2 = cv2.resize(image2, (500,400))

#split and merge
b,g,r = cv2.split(image)
image = cv2.merge((b,g,r))


#image_final = cv2.add(image, image2)
image_final = cv2.addWeighted(image,0.1,image2,0.6,0)

while True:
    
    cv2.imshow('window', image_final)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    
cv2.destroyAllWindows()