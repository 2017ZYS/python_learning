# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:55:19 2019

@author: zhangyushun
"""
import tensorflow as tf
sess=tf.Session()
a=tf.constant(10)
b=tf.constant(22)
print(sess.run(a+b))

