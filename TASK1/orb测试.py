# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:36:23 2019

@author: 19045847
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:24:31 2019

@author: 19045847
"""
#本示例将logo图放大处理（左上角最大大小），并且通过判断同一张图检测子两个点的长度的比例来判断缩放比例
import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy
import heapq

#def cv_imread(file_path):
#    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
#    return cv_img
#read image
#img1 = cv2.imread('./model.jpg',cv2.IMREAD_COLOR)
img1 = cv2.imread('./web_images/77.jpg')
#img1 = cv_imread('./test_images/20190718112141836.jpg')

plt.subplot(121)
plt.imshow(img1[:,:,(2,1,0)])#显示原图(注意opencv通道和pyplot通道的不同)
plt.subplot(122)

gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
plt.imshow(gray,cmap="gray")#显示灰度图

img_resize=cv2.resize(img1,(800,800),interpolation=cv2.INTER_CUBIC)#resize到800*800
plt.imshow(img_resize[:,:,(2,1,0)])
cv2.imwrite("./img_resize.jpg", img_resize)
left_upper_cropped=img_resize[0:100,0:200]
cv2.imwrite("./cv_cropped.jpg", left_upper_cropped)
# 生成掩模矩阵
#输入图像是RGB图像，故构造一个三维数组，四个二维数组是mask四个点的坐标，
site = np.array([[[0, 0], [300, 0],[300, 150], [0,150]]], dtype=np.int32)#四个坐标分别是分别相邻的即可，第一个是横坐标，第二个是纵坐标
im = np.zeros(img_resize.shape[:2], dtype="uint8") #生成image大小的全白图
cv2.polylines(im, site, 1, 255) #在im上画site大小的线，1表示线段闭合，255表示线段颜色
cv2.fillPoly(im, site, 255) #在im的site区域，填充颜色为255
mask = im

plt.imshow(mask,cmap="gray")#显示掩膜灰度图

#检测商品图里的左上角特征子
#surf检测
surf=cv2.xfeatures2d.SURF_create()
#kp=surf.detect(gray,None)#surf.detect（）函数在图像中查找关键点, 如果只想搜索图像的一部分，可以传递掩膜
img3=copy.copy(img_resize)
kp1=surf.detect(img3,mask)#只在左上角掩膜区域内查找关键点
img3=cv2.drawKeypoints(img3,kp1,img3,color=(0,255,0)) #画出特征点，并显示为绿色圆圈

plt.figure(figsize=(10,10))
plt.imshow(img3[:,:,(2,1,0)])

kp1,des1=surf.compute(img3,kp1)#返回的关键点是一个带有很多不用属性的特殊结构体，属性当中有坐标，方向、角度等等
#kp1,des1 = surf.detectAndCompute(img_resize,mask)#kp是关键点列表，des是形状为Number_of_Keypoints×128的numpy数组.
points1 = cv2.KeyPoint_convert(kp1)#将KeyPoint格式数据中的xy坐标提取出来,向右是x,向下是y

print("商品图特征子数量是%d:"% (len(points1)))
print(points1)
#只看商品图左上角的特征子
left_upper_detect_cropped=img3[0:150,0:250]
cv2.imwrite("./cv_detect_cropped.jpg", left_upper_detect_cropped)



#检测并查看logo图里的特征子
#img2 = cv2.imread('./logo.jpg')
img2=cv2.imread("./test_images/logo5.jpg")
#img2=cv_imread("./test_images/logo_2.jpg")
times1=100/img2.shape[0]
times2=200/img2.shape[1]
times=times1 if times1<times2 else times2
print(times)
img2_resize=cv2.resize(img2,None,fx=times,fy=times,interpolation=cv2.INTER_CUBIC)#resize到100*200最大能允许的大小
#img2_gray=cv2.cvtColor(img2_resize,cv2.COLOR_BGR2GRAY)
img4 = copy.copy(img2_resize)
kp2, des2 = surf.detectAndCompute(img4,None)
img4 = cv2.drawKeypoints(img4,kp2,img4,color=(0,255,0)) #画出特征点，并显示为绿色圆圈
plt.imshow(img4[:,:,(2,1,0)])
###################
points2 = cv2.KeyPoint_convert(kp2)#将KeyPoint格式数据中的xy坐标提取出来,向右是x,向下是y
print("logo特征子数量是%d"% (len(points2)))

#####################################
# FlannBasedMatcher解决匹配
# FLANN 参数设计
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
print ('FLANN matches...',len(matches))
good = []
for m,n in matches:
    if m.distance < 0.87*n.distance:
        good.append([m])
print ('FLANN good',len(good))
img5 = cv2.drawMatchesKnn(img3,kp1,img4,kp2,matches,None,flags=2)#匹配效果，比较杂乱，且会出错
#img5 = cv2.drawMatchesKnn(img3,kp1,img4,kp2,good,None,flags=2)
#保存
plt.figure(figsize=(10,10))
fig=plt.gcf()
plt.imshow(img5[:,:,(2,1,0)])
fig.savefig("./img_match.png")
plt.show()

num_dots=5
if len(good)>=num_dots:#最少两个可靠点（一定要可靠)
    print("左上角认为有logo")
#############################################################
#分别求出goodmatrch的特征点对应的queryIdx和trainIdx
queryIdx_list=[]
for i in range(len(good)):
    queryIdx_list.append(good[i][0].queryIdx)
print(queryIdx_list)

trainIdx_list=[]
for i in range(len(good)):
    trainIdx_list.append(good[i][0].trainIdx)
print(trainIdx_list)
#通过匹配的索引找到相应的坐标
points_query=cv2.KeyPoint_convert(kp1,queryIdx_list)
print(points_query)

points_train=cv2.KeyPoint_convert(kp2,trainIdx_list)
print(points_train)
#############################################################
#再精选（确保匹配的电是正确的）
times_mt=np.zeros((len(queryIdx_list),len(queryIdx_list)))#缩放比例矩阵
times_list=[]
#for i in range(len(queryIdx_list)):
#    for j in range(i+1,len(queryIdx_list)):
#        distance[i,j]=np.sqrt(np.sum(np.square(points_query[i,:]-points_query[j,:])))

for i in range(len(trainIdx_list)):
    for j in range(i+1,len(trainIdx_list)):
        if np.sqrt(np.sum(np.square(points_train[i,:]-points_train[j,:]))) >1e-8:    
            times_mt[i,j]=np.sqrt(np.sum(np.square(points_query[i,:]-points_query[j,:])))/np.sqrt(np.sum(np.square(points_train[i,:]-points_train[j,:])))
            times_list.append(times_mt[i,j])
#times_mt=times_mt.reshape(-1,1)  
#n, bins, patches=plt.hist(times_mt,20) 

plt.plot(times_list)
n, bins, patches=plt.hist(times_list,20)
candidates=[]
left_node=np.argsort(n)[-1]
for i in range(len(times_list)):
    if times_list[i]>bins[left_node] and times_list[i]<bins[left_node+1]:
        candidates.append(times_list[i])
plt.plot(candidates)

n, bins, patches=plt.hist(candidates,10)
times=[]
left_node=np.argsort(n)[-1]
for i in range(len(candidates)):
    if candidates[i]>bins[left_node] and candidates[i]<bins[left_node+1]:
        times.append(candidates[i])
plt.plot(times)
times=np.mean(times)#定了query左上角logo图的放大比例

#寻找匹配正确的点
times_mask=np.zeros((len(queryIdx_list),len(queryIdx_list)))
for i in range(len(queryIdx_list)):
    for j in range(i+1,len(queryIdx_list)):
        if (times_mt[i,j]-times<0.01) and (times-times_mt[i,j]<0.01):
             times_mask[i,j]=1
Pro=np.sum(times_mask,axis=1)    #求行和数字越大，代表该点越可能是准确点   
index=heapq.nlargest(num_dots,range(len(Pro)),Pro.take)   #最可能的5个点索引        

###################################################################
## 在两个图上分别标注这3个特征点
#剔除重复准确坐标的点
queryIdx_3=np.array(queryIdx_list)[index].tolist()
points_query=cv2.KeyPoint_convert(kp1,queryIdx_3)
print(points_query)

for i in range(len(points_query)):
    for j in range(i+1,len(points_query)):
        if np.sum(np.square( points_query[i,:]-points_query[j,:]))<1e-8:
            points_query[i,]=[0,0]  
            
row_list=[]
for i in range(len(points_query)):
    if points_query[i,1]!=0:
       row_list.append(i)
points_query_valid=points_query[row_list,:]
print(points_query_valid)#打印准确的切不重复的匹配点坐标

trainIdx_3=np.array(trainIdx_list)[index].tolist()
points_train=cv2.KeyPoint_convert(kp2,trainIdx_3)
points_train_valid=points_train[row_list,:]
print(points_train_valid)#打印准确的切不重复的匹配点坐标


#np.sqrt(np.sum(np.square(points_query_valid[0,:]-points_query_valid[1,:]   )))/np.sqrt(np.sum(np.square( points_train_valid[0,:]-points_train_valid[1,:]   )))
#np.sqrt(np.sum(np.square(points_query_valid[0,:]-points_query_valid[1,:])))/np.sqrt(np.sum(np.square(points_train_valid[0,:]-points_train_valid[1,:])))

#################################可视化
plt.figure(figsize=(10,10))
plt.imshow(img3[:,:,(2,1,0)])
plt.show()

cv2.circle(img_resize,tuple(np.rint(points_query_valid[0,:]).astype(np.int16)),2,(255,0,0),2)
cv2.circle(img_resize,tuple(np.rint(points_query_valid[1,:]).astype(np.int16)),2,(255,0,0),2)
plt.figure(figsize=(10,10))
plt.imshow(img_resize[:,:,(2,1,0)])
plt.show()

plt.figure(figsize=(8,8))
plt.imshow(img4[:,:,(2,1,0)])
plt.show()

cv2.circle(img2_resize,tuple(np.rint(points_train_valid[0,:]).astype(np.int16)),2,(255,0,0),1)
cv2.circle(img2_resize,tuple(np.rint(points_train_valid[1,:]).astype(np.int16)),2,(255,0,0),1)
plt.figure(figsize=(8,8))
plt.imshow(img2_resize[:,:,(2,1,0)])
plt.show()

print(times)
if times>1:
    print("左上角logo太大超过指定大小，不完全在区域内，请等比例缩小到合适大小！")
elif times<0.8:
    print("左上角logo存在，但是未铺满80%")
# 当times在0.8和1之间后，需要判断左上角里的logo是否完整，即是否有部分不在指定区域内
# 计算商品图logo左下角的坐标点
# 计算商品图logo左下角的坐标点
x1_query = points_query_valid[0,:]
x2_query = points_query_valid[1,:]


x1_train = points_train_valid[0,:]
x2_train = points_train_valid[1,:]


dx1=x1_query[0]-times*x1_train[0]#计算平移位置dx
dy1=x1_query[1]-times*x1_train[1]#计算平移位置dy
dx2=x2_query[0]-times*x2_train[0]#计算平移位置dx
dy2=x2_query[1]-times*x2_train[1]#计算平移位置dy

dx=(dx1+dx2)/2
dy=(dy1+dy2)/2


#那么左上角的位置就是(dx,dy)，x方向是向右，y方向是向下
x_=[0,0]
x_[0]=times*img2_resize.shape[1]+dx
x_[1]=times*img2_resize.shape[0]+dy


left_upper_x=dx if dx>0 else 0
left_upper_y=dy if dy>0 else 0
left_upper_detect_cropped1=img_resize[int(left_upper_y):int(np.rint(x_[1])),int(left_upper_x):int(np.rint(x_[0]))]
cv2.imwrite("./cv_detect_cropped1.jpg", left_upper_detect_cropped1)
