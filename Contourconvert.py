#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-28T06:52:38.406Z
# @Author  : CarryHJR

import cv2


def on_trace_bar_changed(args):
    pass


img = cv2.imread('7.jpg')
cv2.namedWindow("real")
cv2.imshow("real", img)
cv2.namedWindow("Image")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.createTrackbar('thres', 'Image', 0, 255, on_trace_bar_changed)

while True:
    cv2.imshow("Image", img)
    thresh = cv2.getTrackbarPos('thres', 'Image')
    img = cv2.threshold(blurred, thresh, 255, cv2.THRESH_BINARY_INV)[1]
    # 键盘检测函数，0xFF是因为64位机器
    # https: // stackoverflow.com / questions / 20539497 / opencv - python - waitkey d- dont - respond
    k = cv2.waitKey(1) & 0xFF
    # print k
    if k == ord('q'):
        break
cv2.waitKey()
cv2.destroyAllWindows()


