# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:54:06 2019

@author: ZYS
"""

#学习Scikit-learn模块
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)
# 输出数据所属的真实标签
print(iris.target)
# 输出数据的纬度
print(iris.data.shape)
# 输出数据标签的名字
print(iris.target_names)



from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
print('iris数据集的大小：',iris.data.shape)
print('目标数据集的大小：',iris.target.shape)
#"""
#data所要划分的样本特征集
#target所要划分的样本标签结果
#test_size样本占比，若为整数则为样本的数量
#random_state随机数种子，同时也是该组随机数的编号，在需要重复实验时，能生成相同的随机数。为0、为空或不同时，生成不同的随机数；当种子相同时即使实例不同也会产生相同的随机数
#X_train生成的训练集的特征
#X_test生成的测试集的特征
#Y_train生成的训练集的标签结果
#Y_test生成的测试集的标签结果
#"""
X_train,X_test,Y_train,Y_test = train_test_split(iris.data,iris.target,test_size = 0.4,random_state = 0)
print('生成的训练集的特征个数（数据个数）：',X_train.shape)
print('生成的训练集的标签个数（样本个数）：',Y_train.shape)
print('生成的测试集的特征（数据个数）：',X_test.shape)
print('生成的测试集的标签个数（样本个数）：',Y_test.shape)
print('iris数据集前5行的数据：',iris.data[:5])
print('生成的训练集的前5行的数据：',X_train[:5])
#在这个实例中train_test_split()函数的参数test_size=0.4,说明生成的数据集中，测试集占40\%,训练集占60\%。

#Scikit-learn使用cross_val_score()对数据集进行制定次数的交叉验证并为每次验证结果进行测评
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn import svm
iris = load_iris()
# 使用支持向量机模型进行验证
clf = svm.SVC(kernel='linear',C=1)
scores = cross_val_score(clf,iris.data,iris.target,cv=5)
print(scores)#
print(scores.mean())

#     K-折交叉验证
import numpy as np
from sklearn.model_selection import KFold

X = ['a','b','c','d','e','f']
# 进行2折交叉验证
kf = KFold(n_splits=2)
# 输出拆分结果
for train,test in kf.split(X):
    print(train,test)
    print(np.array(X)[train],np.array(X)[test])

    
#留一法
import numpy as np
from sklearn.model_selection import LeaveOneOut

X = ['a','b','c','d','e','f']
loo = LeaveOneOut()
for train,test in loo.split(X):
    print(train,test)
    print(np.array(X)[train],np.array(X)[test])

###############################
#1. 线性回归
import numpy as np
from sklearn.linear_model import LinearRegression

X_train=np.array([6,8,10,14,18]).reshape(-1,1)
y_train=[7,9,13,17.5,18]

X_test=np.array([8,9,11,16,12]).reshape(-1,1)
y_test=[11,8.5,15,18,11]

model=LinearRegression()
model.fit(X_train,y_train)
#model.fit(X_train,np.array(y_train))
r_squared=model.score(X_test,y_test)

print(r_squared)
#2. KNN
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

X_train=np.array(
                [ [158,64],
                 [170,86],
                 [183,84],
                 [191,80],
                 [155,49],
                 [163,59],
                 [180,67],
                 [158,54],
                 [170,67]]) 
y_train=['male','male','male','male','female',
         'female', 'female','female','female']
plt.figure
plt.title("分性别人类身高体重图")
plt.xlabel("身高（单位：厘米）")
plt.ylabel("体重（单位：千克）")
for i , x in enumerate(X_train):
      plt.scatter(x[0],x[1],c='r',marker='x' if y_train[i]=='male' else 'D')
      
      
from sklearn.preprocessing import LabelBinarizer
from sklearn.neighbors import KNeighborsClassifier

lb=LabelBinarizer()
y_train_binarized=lb.fit_transform(y_train)
y_train_binarized

K=3
clf=KNeighborsClassifier(n_neighbors=K)
clf.fit(X_train,y_train_binarized.reshape(-1))
prediction_binarized=clf.predict(np.array([155,70]).reshape(1,-1))[0]#在最新版本的sklearn中，所有的数据都应该是二维矩阵，哪怕它只是单独一行或一列，所以，要进行格式改正
predicted_label=lb.inverse_transform(prediction_binarized)
predicted_label

X_test=np()

import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

digits=datasets.load_digits()


