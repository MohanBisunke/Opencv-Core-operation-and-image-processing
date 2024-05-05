import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('img/equalizer.png' , cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(512,512))

equalizer = cv2.equalizeHist(img)
res = np.hstack((img, equalizer))


while True:
    cv2.imshow('window', res)
    
    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

cv2.destroyAllWindows()

