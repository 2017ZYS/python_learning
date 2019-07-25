# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:04:23 2017

@author: zhangyushun
"""
#返回斐波拉契序列的函数
def fibs(n):
    result=[0,1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result
fibs(5)