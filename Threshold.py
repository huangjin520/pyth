import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('7.jpg',0)
resize = cv2.resize(img, None, fx=0.4, fy=0.4)
ret,thresh1 = cv2.threshold(resize,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(resize,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(resize,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(resize,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(resize,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('thresh1',thresh2)
titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()