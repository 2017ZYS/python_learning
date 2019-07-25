# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:28:41 2019

@author: zhangyushun
"""

def collatz(number):
    if 0==number%2:#num是偶数
        return number//2
    else:
        return 3*number+1
while True:
    try:
        num=int(input()) 
        num1=collatz(num)
        print(num1)
        if(1==num1):
            break
    except ValueError:
        print("必须输入一个整数！") 

    
    
