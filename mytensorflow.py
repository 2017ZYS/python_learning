# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 22:06:41 2017

@author: zhangyushun
"""

import tensorflow as tf
import numpy as np

#create data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

##create tensorflow structure start##
Weights=tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases=tf.Varibel(tf.zeros([1]))

y=Weights*x_data+biases

loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.tain.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

init=tf.initialize_all_variables()


##create tensorflow structure end##
sess=tf.Session()
sess.run(init)#Very important

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weights),sess.run(biases))
        
