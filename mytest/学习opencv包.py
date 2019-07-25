# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:55:19 2019

@author: zhangyushun
"""



#-*-encoding=utf-8-*-
import cv2
import numpy as np
#导入cv、numpy包
 
# 载入图像
im = cv2.imread('./1.png')
 
# 打印图像尺寸
h,w = im.shape[:2]
print(h,w)
 
# 保存PNG格式图像为JPEG格式
cv2.imwrite('./22.jpg',im)


import cv2 as cv
src = cv.imread("./1.png")
#cv.namedWindow("1", 0)
cv.imshow("dasiming",src)
cv.waitKey(0)
cv.destroyAllWindows()