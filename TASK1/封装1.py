# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:51:35 2019

@author: ZYS
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:32:21 2019

@author: ZYS
"""
#测试相对系数0.75
import cv2
import numpy as np
#import matplotlib.pyplot as plt
import heapq

def Check(kp1,kp2,good,times,times_mt,num_match):#挑选正确的匹配点并且去除重复的坐标点
      queryIdx_list=[]
      trainIdx_list=[]
      for i in range(num_match):
          queryIdx_list.append(good[i][0].queryIdx)
          trainIdx_list.append(good[i][0].trainIdx)
      #通过匹配的索引找到相应的坐标
      points_query=cv2.KeyPoint_convert(kp1,queryIdx_list)#第一列是x方向向右，第二列是y方向向下
      points_train=cv2.KeyPoint_convert(kp2,trainIdx_list)
      #寻找匹配正确的点
      times_mask=np.zeros((num_match,num_match))
      for i in range(num_match):
          for j in range(i+1,num_match):
              if (times_mt[i,j]-times<0.02) and (times-times_mt[i,j]<0.02):#距离在均值左右0.02认为可能性大
                   times_mask[i,j]=1
      Pro=np.sum(times_mask,axis=1)    #求行和数字越大，代表该点越可能是准确点   
      index=heapq.nlargest(num_dots,range(len(Pro)),Pro.take)   #最可能的num_dots个点索引   
      if len(index)==num_dots:
          #当点够时,再剔除重复准确坐标的点，其实只要两个点就可以了
            queryIdx=np.array(queryIdx_list)[index].tolist()
            points_query=cv2.KeyPoint_convert(kp1,queryIdx)#获取商品图这num_dots点的实际坐标
            for i in range(len(points_query)):
                for j in range(i+1,len(points_query)):
                    if np.sum(np.square( points_query[i,:]-points_query[j,:]))<1e-8:
                        points_query[i,]=[0,0]  #将重复的点之一设为0            
            row_query=[]#不重复的行索引
            for i in range(len(points_query)):
                if points_query[i,1]!=0:
                   row_query.append(i)      
            trainIdx=np.array(trainIdx_list)[index].tolist()#训练图的点的索引跟train图的索引对应
            points_train=cv2.KeyPoint_convert(kp2,trainIdx)    
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
      else:
            points_query_valid=[]
            points_train_valid=[]
      return points_query_valid,points_train_valid
def In_Region1(points_query_valid,points_train_valid,times,img_logo_resize_shape):
      if times>1:#可以适当放大点
          Qualified = False  #放大的在100*200的最大logo图还大，不合格    
      elif times<0.8:#可以适当放小点
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
            x_[0]=times*img_logo_resize_shape[1]+dx
            x_[1]=times*img_logo_resize_shape[0]+dy
            ###附加功能：截取商品图匹配logo的位置（可注释）
            left_upper_x=dx if dx>0 else 0  #匹配的主图上训练图的左上角坐标（可能是负数）
            left_upper_y=dy if dy>0 else 0
            left_upper_detect_cropped=img_commodity[int(left_upper_y):int(np.rint(x_[1])),int(left_upper_x):int(np.rint(x_[0]))]
            cv2.imwrite("./match_cropped_images/match_cropped.jpg", left_upper_detect_cropped)
            print("截取匹配区域Done!") 
            cv2.rectangle(img_commodity,(int(left_upper_x),int(left_upper_y)),(int(np.rint(x_[0])),int(np.rint(x_[1]))),(0, 0, 255), 2)#画矩形框
            cv2.imwrite("./match_cropped_images/match_location.jpg",img_commodity)
            print("定位Done!") 
            ###
            #计算匹配的商品图右下角的坐标
            right_lower_x=int(np.rint(x_[0]))
            right_lower_y=int(np.rint(x_[1]))
            if right_lower_x>=200 or right_lower_y>=100:
                Qualified = False # 匹配的主图上的训练图超出区域，判定为不合格！！！          
            else:
                Qualified = True # 匹配的主图上的训练图在区域内，判定为合格！
      return Qualified

def Cal_times(good,points_query,points_train,kp1,kp2):
      num_match=len(good)
      #再精选（尽量确保匹配的点是正确的）
      times_mt=np.zeros((num_match,num_match))#缩放比例矩阵
      times_list=[]
      for i in range(num_match):
          for j in range(i+1,num_match):
              if np.sum(np.square(points_train[i,:]-points_train[j,:]))>1e-8:    
                  times_mt[i,j]=np.sqrt(np.sum(np.square(points_query[i,:]-points_query[j,:])))/np.sqrt(np.sum(np.square(points_train[i,:]-points_train[j,:])))
                  times_list.append(times_mt[i,j])
      #统计该倍数数组的直方图，进行筛选出正确的距离倍数            
      n,bins=np.histogram(times_list,15,range=(0.5,2))#倍数准确度在0.05精度
#      plt.figure(figsize=(8,8))
#      plt.hist(times_list,20,range=(0.5,2))
      candidates=[]
      left_node=np.argsort(n)[-1]#最大的
      for i in range(len(times_list)):
          if times_list[i]>bins[left_node] and times_list[i]<bins[left_node+1]:
              candidates.append(times_list[i])
              
              
      n, bins=np.histogram(candidates,5)
#      plt.figure(figsize=(8,8))
#      plt.hist(candidates,10,range=(0.5,2))
      times=[]
      left_node=np.argsort(n)[-1]
      for i in range(len(candidates)):
          if candidates[i]>bins[left_node] and candidates[i]<bins[left_node+1]:
              times.append(candidates[i])
      if len(times)==0:
            times=np.mean(candidates)
      else:
            times=np.mean(times)#定了query左上角logo图的放大比例                     
      return times,times_mt

def Validation(good,kp1,kp2,img_logo_resize_shape):
      num_match=len(good)
      queryIdx_list=[]
      trainIdx_list=[]
      for i in range(num_match):
          queryIdx_list.append(good[i][0].queryIdx)
      for i in range(num_match):
          trainIdx_list.append(good[i][0].trainIdx)
#      for i in range(num_match):
#          queryIdx_list.append(good[i][0].queryIdx)
#          trainIdx_list.append(good[i][0].trainIdx)
      #通过匹配的索引找到相应的坐标
      points_query=cv2.KeyPoint_convert(kp1,queryIdx_list)#第一列是x方向向右，第二列是y方向向下
      points_train=cv2.KeyPoint_convert(kp2,trainIdx_list)
      times,times_mt = Cal_times(good,points_query,points_train,kp1,kp2)
      
      print("times是",times)
      
      points_query_valid,points_train_valid=Check(kp1,kp2,good,times,times_mt,num_match)       
      if len(points_query_valid)==0:
            return False
      else: 
            return In_Region1(points_query_valid,points_train_valid,times,img_logo_resize_shape)
def Decision_region1(img_commodity,img_logo,num_dots):
      mask= np.zeros((800,800),np.uint8)#创建一个掩膜（全黑）
      mask[0:150,0:250]=255#将感兴趣区域变白
      sift=cv2.xfeatures2d.SIFT_create()
      kp1,des1 = sift.detectAndCompute(img_commodity,mask)#kp是关键点列表，des是形状为Number_of_Keypoints×128的numpy数组.
            
      expand_y=100/img_logo.shape[0]
      expand_x=200/img_logo.shape[1]
      expand=expand_y if expand_y<expand_x else expand_x
      img_logo_resize=cv2.resize(img_logo,None,fx=expand,fy=expand)#resize到100*200最大能允许的大小
      kp2, des2 = sift.detectAndCompute(img_logo_resize,None)     
      good=Match(des1,des2)#匹配
      num_match = len(good)
      if num_match>=num_dots:#继续判断
            Qualified=Validation(good,kp1,kp2,img_logo_resize.shape)
      else:
            Qualified=False#good的点不够num_dots,认为左上角无logo
      return Qualified
def Match(des1,des2):
      # FlannBasedMatcher解决匹配
      FLANN_INDEX_KDTREE = 0
      index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
      search_params = dict(checks=50)
      flann = cv2.FlannBasedMatcher(index_params,search_params)
      matches = flann.knnMatch(des1,des2,k=2)
      good = []
      for m,n in matches:
          if m.distance < 0.75*n.distance:
              good.append([m])
      print ('FLANN matches...',len(matches))        
      print ('FLANN good',len(good))
      return good
##############################  
#parameters setting
num_dots=5       #能匹配的最少的点

#测试乔丹
#path1 ='./test_images/60.jpg'
#path1 ='./test_images/61.jpg'
#path1 ='./test_images/62.jpg'
#path1 ='./test_images/63.jpg'
#path1 ='./test_images/64.jpg'
#path1 ='./test_images/65.jpg'
#path1 ='./test_images/66.jpg'
#path1 ='./test_images/67.jpg'#没测到
#path1 ='./test_images/68.jpg'
#path1 ='./test_images/82.jpg'
#path2 ='./test_images/logo_5.jpg'
#测试古莱登
#path1 ='./test_images/20190718112141836.jpg'
#path1 ='./test_images/20190718112154125.jpg'
#path1 ='./test_images/20190718112157893.jpg'
#path1 ='./test_images/20190718112200900.jpg'
#path1 ='./test_images/20190718112206220.jpg'
#path1 ='./test_images/20190718112208748.jpg'
#path1 ='./test_images/20190718112211388.jpg'
#path2 ='./test_images/logo_1.jpg'
#测试禾玉珠宝
#path1 ='./test_images/90.jpg'
#path1 ='./test_images/91.jpg'
#path1 ='./test_images/92.jpg'
#path1 ='./test_images/93.jpg'
#path1 ='./test_images/94.jpg'
#path1 ='./test_images/95.jpg'
#path1 ='./test_images/112.jpg'
#path2 ='./test_images/logo_6.jpg'
#测试周六福
#path1 ='./test_images/0.jpg'
#path1 ='./test_images/1.jpg'
#path1 ='./test_images/2.jpg'
#path1 ='./test_images/3.jpg'
#path1 ='./test_images/4.jpg'
#path1 ='./test_images/5.jpg'
#path2 ='./test_images/logo_3.jpg'
#测试小米
path1 ='./test_images/120.jpg'#标志合格
#path1 ='./test_images/121.jpg'#标志合格
#path1 ='./test_images/122.jpg'
#path1 ='./test_images/123.jpg'
#path1 ='./test_images/124.jpg'
#path1 ='./test_images/125.jpg'
##path1 ='./test_images/127.jpg'
#path1 ='./test_images/137.jpg'
#path1 ='./test_images/145.jpg'
path2 ='./test_images/logo_8.jpg'


#read images
img_commodity=cv2.imread(path1)#商品图
img_commodity=cv2.resize(img_commodity,(800,800),interpolation=cv2.INTER_CUBIC)#resize到800*800
img_logo=cv2.imread(path2)#logo图
Qualified=Decision_region1(img_commodity,img_logo,num_dots)
if Qualified:
      print("该商品图区域一合格！")
else:
      print("该商品图区域一不合格！！！")