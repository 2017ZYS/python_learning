# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:46:03 2019

@author: ZYS
"""
#opencv显示图像
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('zophie.png',1)
cv2.imshow('image',img)

b, g, r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.imshow(img2)
############################################################
import numpy as np
import cv2
from matplotlib import pyplot as plt
'''
img = cv2.imread('cute.jpg',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.xticks([],plt.yticks([]))  # to hide tick values on X and Y axis
plt.show()
'''
 
'''
Color image loaded by OpenCV is in BGR mode.
But Matplotlib displays in RGB mode.
So color images will not be displayed correctly in Matplotlib if image is read with OpenCV.
Please see the exercises for more details.
'''
img = cv2.imread('zophie.png')
b, g, r = cv2.split(img)
img2 = cv2.merge([r,g,b])
# img2 = img[:,:,::-1]    this can be faster
plt.subplot(121);plt.imshow(img)  # expects distorted color
plt.title("扭曲的BGR图")
plt.subplot(122);plt.imshow(img2)  # expects true color
plt.title("真实的RGB图")
plt.show()
 
cv2.imshow('bgr image',img)  # expects true color
cv2.imshow('rgb image',img2)  # expects distrorted color
cv2.waitKey(0)
cv2.destroyAllWindows()