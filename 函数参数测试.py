# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:38:12 2017

@author: 张裕顺
"""
#-----------------------------------------------------
#位置参数和关键字参数
#def hello(name,greeting):
#    print('%s,%s!' % (greeting,name))
#def hello1(greeting,name):
#    print('%s,%s!' % (greeting,name))
#hello('zhang','hello')
#hello1('zhang','hello')
#def hello3(name,greeting='hello',punctuation='!'):
#    print('%s,%s%s' % (greeting,name,punctuation))
#hello3('zhang')
#hello3('zhang','hi')
#hello3('zhang','hi','......')
#hello3('zhang',punctuation='.')
#hello3('zhang',greeting='my dear')
##-----------------------------------------------------
##收集参数设置
#def print_params(*params):
#    print(params)
#print_params('Testing')#结果作为元组打印出来
#print_params(1,2,3)
#参数前的星号将所有值放置在同一元组中
#将这些值收集起来，然后使用
#-----------------------------------------------------
#def print_params_2(title,*params):
#    print(title)
#    print(params)
#print_params_2('params:',1,2,3)
#print_params_2('nothing:')#如果不提供任何收集的元素，params就是个空元组
#print_params_2('hello',something=34)#会报错不能处理关键字参数
#-----------------------------------------------------
#关键字参数，位置参数和收集参数一起使用
#def print_params_4(x,y,z=3,*pospar,**keypar):
#    print (x,y,z)
#    print (pospar)#收集参数但不能处理关键字参数
#    print (keypar)#能处理关键字参数的“收集”操作
#print_params_4(1,2,3,4,5,6,7,foo=1,bar=2)
#print_params_4(1,2,3,foo=1,bar=2)
#-----------------------------------------------------
#def with_stars(**kwds):
#    print(kwds['name'],'is',kwds['age'],'years old')
#args={'name':'Mr.Gumby','age':43}
#with_stars(**args)
#-----------------------------------------------------
#练习使用参数
#-------------
#def story(**kwds):
#    return('Once upon a time,there was a %(job)s called %(name)s.'% kwds)
#print (story(job='king',name='Gumby'))
#print (story(name='Gumby',job='king'))
#params={'job':'language','name':'python'}
#print(story(**params))
#del params['job']
#print(story(job='stoke of genius',**params))
#-------------
#def interval(start,stop=None,step=1):
#    'Imitaes range() for step>0 '#文档字符串,模仿range()函数
#    if stop is None:      #如果没有为stop提供参数
#        start,stop=0,start#指定参数
#    result=[]
#    i=start#i初值就是start
#    while i<stop:#直到计算到stop的值
#        result.append(i)#将值添加到result内
#        i+=step#用step(>0)更新i值
#    return result
#interval(10)
#interval(5)
#interval(1,5)
#interval(3,12,4)
#-------------
#递归实现阶乘和幂
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
factorial(2)
def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
power(2,3)
#------------

    
    
    
    
    
    
