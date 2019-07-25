import cv2
import numpy as np
import matplotlib.pyplot as plt

#read image
img = cv2.imread('test.jpg',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
B,G,R=cv2.split(img)
img=cv2.merge([R,G,B])
plt.subplot(121)
plt.imshow(img)#显示原图
plt.subplot(122)
plt.figure(1)
plt.imshow(gray,cmap="gray")#显示灰度图


img=cv2.resize(gray,(800,800),interpolation=cv2.INTER_CUBIC)#resize到800*800
#输入图像是RGB图像，故构造一个三维数组，四个二维数组是mask四个点的坐标，
site = np.array([[[0, 0], [200, 0],[200, 100], [0,100]]], dtype=np.int32)#四个坐标分别是分别相邻的即可，第一个是横坐标，第二个是纵坐标
im = np.zeros(img.shape[:2], dtype="uint8") #生成image大小的全白图
cv2.polylines(im, site, 1, 255) #在im上画site大小的线，1表示线段闭合，255表示线段颜色
cv2.fillPoly(im, site, 255) #在im的site区域，填充颜色为255
mask = im
plt.figure(2)
plt.imshow(mask,cmap="gray")#显示掩膜灰度图