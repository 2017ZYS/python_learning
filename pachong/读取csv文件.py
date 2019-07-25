# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:29:59 2019

@author: ZYS
"""

import csv
import numpy as np
import os
import requests

exampleFile=open("exportData.csv")
exampleReader=csv.reader(exampleFile)

exampleData=list(exampleReader)

exampleData=exampleData[2:]
Data=np.array(exampleData)
links=Data[:,3]#URL列表
Labels=Data[:,4]

#建立文件夹
i=1
for i in range(28315,len(Data)):
      print("第"+str(i)+"个链接处理：")
      if Labels[i].strip()=="1":
            #建立文件夹
            path="C:\\Users\\ZYS\Desktop\\python_learning\\pachong\\7_24_1"
            if not os.path.exists(path):
                  os.makedirs(path)
            #获取链接并下载图片
            link=links[i].strip()#后面有\t需要删除空白字符
            if  link=="is_not_pic" or link=="size_over":
                  continue    
            res=requests.get(link)
          #  print(res.status_code)#打印响应
           
            filename=path+"\\"+str(i)+".png"
            with open(filename, 'wb') as f:
                  f.write(res.content) 
            print(link+"图片下载完毕！")
      elif Labels[i].strip()=="2":
            path="C:\\Users\\ZYS\Desktop\\python_learning\\pachong\\7_24_2"
            if not os.path.exists(path):
                  os.makedirs(path)
            #获取链接并下载图片
            link=links[i].strip()#后面有\t需要删除空白字符
            if  link=="is_not_pic" or link=="size_over":
                  continue         
            res=requests.get(link)
           # print(res.status_code)#打印响应
            
            filename=path+"\\"+str(i)+".png"
            with open(filename, 'wb') as f:
                  f.write(res.content) 
            print(link+"图片下载完毕！")
      elif Labels[i].strip()=="3":
            path="C:\\Users\\ZYS\Desktop\\python_learning\\pachong\\7_24_3"
            if not os.path.exists(path):
                  os.makedirs(path)
            #获取链接并下载图片
            link=links[i].strip()#后面有\t需要删除空白字符
            if  link=="is_not_pic" or link=="size_over":
                  continue    
            res=requests.get(link)
            #print(res.status_code)#打印响应
            
            filename=path+"\\"+str(i)+".png"
            with open(filename, 'wb') as f:
                  f.write(res.content) 
            print(link+"图片下载完毕！")

      


