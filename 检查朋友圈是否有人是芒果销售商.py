# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:31:15 2018

@author: zhangyushun
"""
#广度优先搜索算法（breadth-first search, BFS）

from collections import deque
def person_is_seller(person):
    return person[-1]=='m'
#需要考虑 检查一个人之前，要确认之前没检查过他，这很重要
def search(name):
    search_queue=deque()#创建一个队列
    search_queue+=graph[name]  
    searched=[]#这个数组用于记录检查过的人
    while search_queue:#只要队列不为空
        person=search_queue.popleft()
        if person not in searched:#仅当这个人没有检查过时才检查
            if person_is_seller(person):
                print(person+" is a mango seller!")#是，打印芒果销售商
                return True
            else:
                search_queue+=graph[person]#此人不是芒果销售商，将其朋友加入到搜索队列
                searched.append(person)#将这个人记为检查过
    return False#如果到了这里，就说明队列中没人是芒果销售商
    
graph={}
graph["you"]=['alice','bob','claire']
graph["bob"]=['anuj','peggy']
graph["alice"]=['peggy']
graph["claire"]=['thom','jonny']
graph["anuj"]=[]
graph["peggy"]=[]
graph["thom"]=[]
graph["jonny"]=[]    
search('you')
name='you'

        
    