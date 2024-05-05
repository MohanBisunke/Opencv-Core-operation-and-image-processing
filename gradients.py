import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('img/gradienttest.webp' ,cv2.IMREAD_GRAYSCALE)


sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=3)
sobelx2 = np.uint8(np.absolute(sobelx))
sobely = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=3)
sobely2 = np.uint8(np.absolute(sobely))

laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian2 = np.uint8(np.absolute(laplacian))

titles = ['image' ,'sobelx','sobelx2', 'sobely','sobely2', 'laplacian', 'abs_laplacian']
images = [img, sobelx,sobelx2, sobely,sobely2, laplacian, laplacian2]


for i in range(len(titles)):
    plt.subplot(3,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()