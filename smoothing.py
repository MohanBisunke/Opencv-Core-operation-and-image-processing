import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/balls.webp')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


kernel = np.ones((5,5), np.float32)/25

conv2D = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)

#ksize	aperture linear size; it must be odd and greater than 1, for example: 3, 5, 7 ...
medianblur = cv2.medianBlur(img,5)

#Bilateral filtering also takes a Gaussian filter in space, but one more Gaussian filter which is a function of pixel difference.
# The Gaussian function of space makes sure that only nearby pixels are considered for blurring,
# while the Gaussian function of intensity difference makes sure that only those pixels with similar intensities 
# to the central pixel are considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation.


bilateralblur = cv2.bilateralFilter(img,9,75,75)


titles = ['img', 'conv2D', 'blur', 'gblur', 'mdblur','biblur']
images = [img, conv2D, blur, gblur,medianblur,bilateralblur]
for i in range(len(titles)):
    plt.subplot(2,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()