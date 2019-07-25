# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 16:15:11 2019

@author: zhangyushun
"""
import numpy as np
import operator
def createDataSet():
    group=np.array([[1,1.1],[1,1],[0,0],[0,0.1]])
    labels=["A","A","B","B"]
    return group,labels
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet
    sqDiffMat=diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    #选择距离最小的k个点
    classCount={}
    for i in range (k):
        voteIlabel=labels(sortedDistIndicies[i])
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.iteritems(),key=operator.temgetter(1),reverse=True)
    return sortedClassCount[0][0]
  