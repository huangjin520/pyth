import cv2
import numpy as np
import matplotlib.pyplot as plt
src = cv2.imread("7.jpg", 1)
result = cv2.resize(src, None, fx=0.4, fy=0.4)  # 图片缩放
height = result.shape[0]
width = result.shape[1]
grayimg = np.zeros((height, width, 3), np.uint8)
print ('grayimg')
for i in range(height):
    for j in range(width):
        #灰度加权平均法
        gray = 0* result[i,j][0] + 0* result[i,j][1] +1 * result[i,j][2]#蓝通道下的灰度化效果是最好的
        grayimg[i,j] = np.uint8(gray)
ret,threshimg = cv2.threshold(grayimg, 130, 250, cv2.THRESH_BINARY)#二值化图像
#contours, hierarchy = cv2.findContours(threshimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(threshimg, contours, -1, (0, 255, 0), 1)
cv2.imshow('result', threshimg)
cv2.waitKey()
cv2.destroyAllWindows()
#位数不对]FindContours supports only CV_8UC1 images when mode != CV_RETR_FLOODFILL otherwise supports CV_32SC1 images only in function 'cv