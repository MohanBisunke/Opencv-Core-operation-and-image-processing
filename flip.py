import cv2
import numpy as np

img = cv2.imread('img/img.jpg')
print(img.shape)

img = cv2.resize(img,(256,256))


img_flip0 = cv2.flip(img,0)
img_flip1 = cv2.flip(img,1)
img_flip2 = cv2.flip(img,-1)

final_img = np.hstack((img,img_flip0,img_flip1,img_flip2))

cv2.imshow('window' , final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

