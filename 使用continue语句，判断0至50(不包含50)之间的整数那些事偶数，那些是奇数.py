# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:00:06 2017

@author: zhangyushun
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#使用continue语句，判断0至50(不包含50)之间的整数那些事偶数，那些是奇数
for n in range(0,50):
   if n%2==0:
       print('%d是偶数'%n)
       continue
   print('%d是奇数'%n)