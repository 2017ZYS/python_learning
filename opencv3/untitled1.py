# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 09:50:48 2018

@author: zhangyushun
"""

import cv2 as cv
 
#读入图片文件
src=cv.imread('1.png')
#创建一个名字加 “ input image ” 的窗口，
# 窗口可以根据图片大小自动调整
cv.namedWindow('input image',cv.WINDOW_AUTOSIZE)
#在窗口显示图片
cv.imshow('input image',src)
 
#等待用户操作
cv.waitKey(0)
#释放所有窗口
cv.destroyAllWindows()
