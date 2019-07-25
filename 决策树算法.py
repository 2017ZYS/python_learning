# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#1.学习使用数据集
#from sklearn.datasets import load_iris
#iris=load_iris()
#print (iris.feature_names)
#print (iris.target_names)
#print(iris.data[0])
#print(iris.target[0])
##迭代输出整个数据集
#for i in range(len(iris.target)):
#    print("Example %d:features %s,label %s" %(i,iris.data[i],iris.target[i]))
##2.学习训练数据集
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()
test_idx=[0,50,100]
#training data
train_target=np.delete(iris.target,test_idx)
train_data=np.delete(iris.data,test_idx,axis=0)

#testing data
test_target=iris.target[test_idx]
test_data=iris.data[test_idx]

clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print(test_target)
print(clf.predict(test_data))

#viz code
#-----------------------------------------------------
#from sklearn.externals.six import StringIO
#import pydotplus
#dot_data=StringIO()
#tree.export_graphviz(clf, out_file=dot_data, 
#                         feature_names=iris.feature_names,  
#                         class_names=iris.target_names,  
#                         filled=True, rounded=True,  
#                         impurity=False)  
#graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
#graph.write_pdf("iris.pdf")
#上面这些注释的代码不知道为什么不行
#-----------------------------------------------------
#生成iris.dotdot文件后再用dot命令转换成pdf文件
#dot命令为：dot -Tpdf iris.dot -o iris.pdf
with open("iris.dot", 'w') as f:
     f = tree.export_graphviz(clf, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         out_file=f) 


