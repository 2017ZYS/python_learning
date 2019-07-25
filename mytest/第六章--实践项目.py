# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:06:36 2019

@author: zhangyushun
"""
#第六章--实践项目
def printTable(tableData):
    row=len(tableData[0])#每一列有几个字符串
    column=len(tableData)#每一行有几个字符串
    colWidths=[0]*len(tableData)#存放每一列字符串的最大长度数
    for i in range(len(tableData)):
        for characters in tableData[i]:#遍历每一列的字符串得到该列的最长字符串的长度
            length=len(characters)
            if length>=colWidths[i]:
                colWidths[i]=length
    for i in range(row):
        for j in range(column):
            print(tableData[j][i].rjust(colWidths[j]),end=' ')
        print("\n",end='')    
            
tableData=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
printTable(tableData)

tableData=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose'],
           ["sdfdfdsf","dfdfwewg",'dfdfdfdasfdf','df']]
printTable(tableData)