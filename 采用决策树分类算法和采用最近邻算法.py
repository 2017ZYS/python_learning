# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:06:12 2017

@author: zhangyushun
"""
# import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X=iris.data
y=iris.target

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.5)
#--------------------------------------------------------
#采用决策树分类算法
#from sklearn import tree
#my_classifier=tree.DecisionTreeClassifier()
#采用最近邻算法
from sklearn.neighbors import KNeighborsClassifier
my_classifier=KNeighborsClassifier()

my_classifier.fit(X_train,y_train)#训练分类器

predictions = my_classifier.predict(X_test)#分类器对测试数据分类
#print(predictions)

from sklearn.metrics import accuracy_score
print (accuracy_score(y_test,predictions))


