# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:59:34 2019

@author: zhangyushun
"""
import random
heads=0
for i in range(1,1001):
    if random.randint(0,1)==1:
        heads+=1
    if i==500:
        print("一半完成！")
print("总共掷了正面"+str(heads)+'次')