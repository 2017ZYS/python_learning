# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 14:31:12 2019

@author: 19045847
"""

#opencv显示图像
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')
b, g, r = cv2.split(img)
img1 = cv2.merge([r,g,b])
plt.subplot(121)
plt.imshow(img1)#用plt正常显示rgb图像
plt.axis('off')

img2 = cv2.imread('logo.png')
b, g, r = cv2.split(img2)
img2 = cv2.merge([r,g,b])
plt.subplot(122)
plt.imshow(img2)#用plt正常显示rgb图像
plt.axis('off')
plt.show()
