# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:53:28 2019

@author: ZYS
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:14:04 2019

@author: 19045847
"""
#完整的tensorflow识别MNIST数据集,准确率在90%左右
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./深度学习代码/MNIST_data/", one_hot=True)#读数据
x = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x,W) + b)
y_ = tf.placeholder("float", [None,10])#添加一个新的占位符用于输入正确值
cross_entropy = -tf.reduce_sum(y_*tf.log(y))#交叉熵
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)#在这里，我们要求TensorFlow用梯度下降算法（gradient descent algorithm）以0.01的学习速率最小化交叉熵。
#一个Session里面启动我们的模型，并且初始化变量
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
#开始训练模型，这里我们让模型循环训练1000次！
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print (sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))