# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#使用break语句查找2至50（不含50）的素数，如果不是素数则分解因数
for n in range(2,50):
    for x in range(2,n):
        if n%x==0:#不是素数要分解因数
#            format="%d不是素数是合数，且%d=%d*%d"
#            values=(n,n,x,n/x)
#            print(format % values)
#            break
#        if n==x+1:
#            print("%d是素数" % n)
            print("%d不是素数是合数，且%d=%d*%d" % (n,n,x,n/x))
            break
        if n==x+1:
            print("%d是素数" % n)
            
        