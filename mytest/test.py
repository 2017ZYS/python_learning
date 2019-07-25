# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:03:32 2019

@author: zhangyushun
"""
spam=0
while spam<5:
    print("Hello world!")
    spam+=1
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
for i in range(1,6,2):
    print(i)
    
import random
for i in range(5):
    print(random.randint(1,10))
    

import sys
while True:
    print("Type exit to exit.")
    response=input()
    if response=='exit':
        sys.exit()
    print("You typed "+response +'.')
spam=['cat','bat','rat','elephant']
spam[0]
spam[3]
['cat','bat','rat','elephant'][3]
print('Hello',end=' ')
print('world')
print('cat','dog','mice',sep=',')
#异常处理
def spam(a):
    try:
        return 42/a
    except ZeroDivisionError:
        print('除数不能为0')      
spam(2)
spam(0)
#判断奇偶数
def iseven(num):
    if 0==num%2:
        return True
    return False
iseven(11)
#列表常用方法
spam=['hello','hi','howdy','heyas']
spam.index('hello')
spam.index("hi")
spam.append("how are you")
spam.insert(2,'you are welcome')        
spam=[2,5,3.14,1,-7]
spam.sort()
spam#有小到大
spam=['ants','cats','dog','badgers','elphants']
spam.sort()
            
spam=['apples',
      'orange',\
      'bananas']

def isphonenumber(text):#返回真假，即判断字符串是否是指定电话号码模式
    if len(text)!=12:
        return False
    for i in range(3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isphonenumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isphonenumber('Moshi moshi'))

message='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk=message[i:i+12]
    if isphonenumber(chunk):
        print("phone number found:"+chunk)

print("Done") 

import datetime
now=datetime.datetime.now()
print(now)