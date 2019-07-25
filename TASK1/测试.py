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
import heapq
import sys
#parameters setting
Qualified=True   #默认是True
num_dots=5       #能匹配的最少的点
#path1 ='./test_images/64.jpg'
#path2 ='./test_images/logo_5.jpg'
#

#测试小米
#path1 ='./test_images/120.jpg'
#path1 ='./test_images/121.jpg'
#path1 ='./test_images/122.jpg'
#path1 ='./test_images/123.jpg'
#path1 ='./test_images/124.jpg'
#path1 ='./test_images/125.jpg'
path1 ='./test_images/145.jpg'
path2 ='./test_images/logo_8.jpg'


#read image
img1 = cv2.imread(path1,cv2.IMREAD_COLOR)
img1=cv2.resize(img1,(800,800),interpolation=cv2.INTER_CUBIC)#resize到800*800
# if img1.shape[0]==800 and img1.shape[1]>800:
#     img1 = img1[:,0:799]
# 生成左上角200*300的掩模矩阵
# 输入图像是RGB图像，故构造一个三维数组，四个二维数组是mask四个点的坐标，
mask= np.zeros((800,800),np.uint8)#创建一个掩膜（全黑）
mask[0:150,0:250]=255#将感兴趣区域变白
#检测商品图里的左上角特征子
#SIFT检测
sift=cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(img1,mask)#kp是关键点列表，des是形状为Number_of_Keypoints×128的numpy数组.
points1 = cv2.KeyPoint_convert(kp1)#将KeyPoint格式数据中的xy坐标提取出来,向右是x,向下是y        

img11 = cv2.drawKeypoints(img1,kp1,img1,color=(0,255,0)) #画出特征点，并显示为绿色圆圈
plt.imshow(img11[:,:,(2,1,0)])


#检测并查看调整大小的logo图里的特征子
#img2 = cv2.imread('./logo.jpg')
img2 = cv2.imread(path2)

expand_y=100/img2.shape[0]
expand_x=200/img2.shape[1]
expand=expand_y if expand_y<expand_x else expand_x
img2_resize=cv2.resize(img2,None,fx=expand,fy=expand)#resize到100*200最大能允许的大小
kp2, des2 = sift.detectAndCompute(img2_resize,None)
points2 = cv2.KeyPoint_convert(kp2)#将KeyPoint格式数据中的xy坐标提取出来,向右是x,向下是y        

plt.figure()
img33 = cv2.drawKeypoints(img2_resize,kp2,img2_resize,color=(0,255,0)) #画出特征点，并显示为绿色圆圈
plt.imshow(img33[:,:,(2,1,0)])

#def flann_match(rel_dis=0.8,des1,des2,good):
#      FLANN_INDEX_KDTREE = 0
#      index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
#      search_params = dict(checks=50)
#      flann = cv2.FlannBasedMatcher(index_params,search_params)
#      matches = flann.knnMatch(des1,des2,k=2)
#      good = []
#      for m,n in matches:
#          if m.distance < rel_dis*n.distance:
#              good.append([m])
#      num_match = len(good)
#      return num_match



# FlannBasedMatcher解决匹配
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)
good = []
for m,n in matches:
    if m.distance < 0.83*n.distance:
        good.append([m])
num_match = len(good)
if num_match<num_dots:
    Qualified = False   #匹配点太少，认为左上角区域没有logo，不合格
    print("该商品图区域一不合格!")
    sys.exit(0)
#############################################可视化匹配            
print ('FLANN matches...',len(matches))        
print ('FLANN good',len(good))
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
plt.figure(figsize=(10,10))
fig=plt.gcf()
plt.imshow(img3[:,:,(2,1,0)])
fig.savefig("./img_match.png")#保存
plt.show()
#############################################            
#分别求出goodmatch的特征点对应的queryIdx和trainIdx
queryIdx_list=[]
trainIdx_list=[]
for i in range(num_match):
    queryIdx_list.append(good[i][0].queryIdx)
for i in range(num_match):
    trainIdx_list.append(good[i][0].trainIdx)
#通过匹配的索引找到相应的坐标
points_query=cv2.KeyPoint_convert(kp1,queryIdx_list)#第一列是x方向向右，第二列是y方向向下
points_train=cv2.KeyPoint_convert(kp2,trainIdx_list)
#再精选（尽量确保匹配的点是正确的）
times_mt=np.zeros((num_match,num_match))#缩放比例矩阵
times_list=[]
for i in range(num_match):
    for j in range(i+1,num_match):
        if np.sum(np.square(points_train[i,:]-points_train[j,:]))>1e-8:    
            times_mt[i,j]=np.sqrt(np.sum(np.square(points_query[i,:]-points_query[j,:])))/np.sqrt(np.sum(np.square(points_train[i,:]-points_train[j,:])))
            times_list.append(times_mt[i,j])
#统计该倍数数组的直方图，进行筛选出正确的距离倍数            
n,bins=np.histogram(times_list,15,range=(0.5,2))#倍数准确度在0.1精度
plt.figure(figsize=(8,8))
plt.hist(times_list,16,range=(0.5,2))
candidates=[]
left_node=np.argsort(n)[-1]#最大的
for i in range(len(times_list)):
    if times_list[i]>bins[left_node] and times_list[i]<bins[left_node+1]:
        candidates.append(times_list[i])

       
n, bins=np.histogram(candidates,5)
plt.figure(figsize=(8,8))
plt.hist(candidates,5,range=(0.5,2))
times=[]
left_node=np.argsort(n)[-1]
for i in range(len(candidates)):
    if candidates[i]>bins[left_node] and candidates[i]<bins[left_node+1]:
        times.append(candidates[i])
if len(times)==0:
      times=np.mean(candidates)
else:
      times=np.mean(times)#定了query左上角logo图的放大比例            
print("times是",times)            
#寻找匹配正确的点
times_mask=np.zeros((num_match,num_match))
for i in range(num_match):
    for j in range(i+1,num_match):
        if (times_mt[i,j]-times<0.02) and (times-times_mt[i,j]<0.02):#距离在均值左右0.02认为可能性大
             times_mask[i,j]=1
Pro=np.sum(times_mask,axis=1)    #求行和数字越大，代表该点越可能是准确点   
index=heapq.nlargest(num_dots,range(len(Pro)),Pro.take)   #最可能的num_dots个点索引   
if len(index)<2:#如果两个准确点都找不到，就是认为不合格
    Qualified = False   
    print("两个匹配点都没有，左上角无logo, 该商品图区域一不合格!")
    sys.exit(0)
#再剔除重复准确坐标的点
queryIdx_3=np.array(queryIdx_list)[index].tolist()
points_query=cv2.KeyPoint_convert(kp1,queryIdx_3)#获取商品图这num_dots点的实际坐标
for i in range(len(points_query)):
    for j in range(i+1,len(points_query)):
        if np.sum(np.square( points_query[i,:]-points_query[j,:]))<1e-8:
            points_query[i,]=[0,0]  #将重复的点之一设为0            
row_query=[]#不重复的行索引
for i in range(len(points_query)):
    if points_query[i,1]!=0:
       row_query.append(i)

trainIdx_3=np.array(trainIdx_list)[index].tolist()#训练图的点的索引跟train图的索引对应
points_train=cv2.KeyPoint_convert(kp2,trainIdx_3)    
for i in range(len(points_train)):
    for j in range(i+1,len(points_train)):
        if np.sum(np.square( points_train[i,:]-points_train[j,:]))<1e-8:
            points_train[i,]=[0,0]  #将重复的点之一设为0            
row_train=[]#不重复的行索引
for i in range(len(points_train)):
    if points_train[i,1]!=0:
       row_train.append(i)       
row_valid=[val for val in row_query if val in row_train]#交集    
points_query_valid=points_query[row_valid,:]#获取了商品图不重复的较为准确的点坐标
points_train_valid=points_train[row_valid,:]#获取了训练图不重复的较为准确的点坐标

if len(points_train)<2:#如果两个准确点都找不到，就是认为不合格
    Qualified = False   
    print("两个匹配点都没有，左上角无logo, 该商品图区域一不合格!")
    sys.exit(0)
#最后其实只需要两个可靠的不重复的匹配点坐标！！！         
#####################################可视化看出最后匹配的两个点对不对
plt.figure(figsize=(10,10))
plt.imshow(img1[:,:,(2,1,0)])
plt.show()

cv2.circle(img1,tuple(np.rint(points_query_valid[0,:]).astype(np.int16)),2,(255,0,0),2)
cv2.circle(img1,tuple(np.rint(points_query_valid[1,:]).astype(np.int16)),2,(255,0,0),2)
plt.figure(figsize=(10,10))
plt.imshow(img1[:,:,(2,1,0)])
plt.show()

plt.figure(figsize=(8,8))
plt.imshow(img2[:,:,(2,1,0)])
plt.show()

cv2.circle(img2_resize,tuple(np.rint(points_train_valid[0,:]).astype(np.int16)),2,(255,0,0),1)
cv2.circle(img2_resize,tuple(np.rint(points_train_valid[1,:]).astype(np.int16)),2,(255,0,0),1)
plt.figure(figsize=(8,8))
plt.imshow(img2_resize[:,:,(2,1,0)])
plt.show()
###################################           
if times>1:
    Qualified = False  #放大的在100*200的最大logo图还大，不合格    
elif times<0.8:
    Qualified = False  #即使是在区域内但是不满80%，仍然不合格
# 当times在0.8和1之间后，需要判断左上角里的logo是否完整，即是否有部分不在指定区域内
else:
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
      left_upper_x=dx if dx>0 else 0  #匹配的主图上训练图的左上角坐标（可能是负数）
      left_upper_y=dy if dy>0 else 0
      #计算匹配的商品图右下角的坐标
      right_lower_x=int(np.rint(x_[0]))
      right_lower_y=int(np.rint(x_[1]))
      if right_lower_x>=200 or right_lower_y>=100:
          Qualified = False # 匹配的主图上的训练图超出区域，判定为不合格！   
      # Making decision
      if Qualified:
          print("该商品图区域一合格!")
      else:
         print("该商品图区域一不合格!")
##############################################################截取匹配区域    
left_upper_detect_cropped=img1[int(left_upper_y):int(np.rint(x_[1])),int(left_upper_x):int(np.rint(x_[0]))]
cv2.imwrite("./match_cropped_images/match_cropped.jpg", left_upper_detect_cropped)
print("截取匹配区域Done!")            
############################################################## 
cv2.rectangle(img1,(int(left_upper_x),int(left_upper_y)),(int(np.rint(x_[0])),int(np.rint(x_[1]))),(0, 0, 255), 2)#画矩形框
cv2.imwrite("./match_cropped_images/match_location.jpg",img1)
print("定位Done!")            