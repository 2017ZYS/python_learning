# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 19:09:47 2017

@author: zhangyushun
"""
#全局变量修改
count=5
def fun1():
    count=10#即使名字和全局变量count一样，但是这里的count依然是局部变量，作用域覆盖了全局变量count
    print(count)
fun1()
print(count)
#-----------------
def fun2():
    global count  #声明count是全局变量
    count=count+1
    print(count)
fun2()
print(count)
#函数嵌套练习：
def fun3():
    print('fun3()正在被调用...')
    def fun4():
        print('fun4()正在被调用...')
    fun4()
fun3() 
    
    