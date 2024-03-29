# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 00:34:37 2019

@author: ZYS
"""
#MNIST的AlexNet实现（严格按照论文网络结构）(训练集99.21%，测试集98.44%)
from __future__ import print_function
 
from tensorflow.examples.tutorials.mnist import input_data
 
mnist = input_data.read_data_sets("./深度学习代码/MNIST_data/", one_hot=True)
 
import tensorflow as tf
# 定义网络超参数
learning_rate = 0.001
training_iters = 200000
batch_size = 128
display_step = 10
 
# 定义网络参数
n_input = 784 # 输入的维度
n_classes = 10 # 标签的维度
dropout = 0.75 # Dropout 的概率
 
# 占位符输入
x = tf.placeholder(tf.float32, [None, n_input])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)
 
# 卷积操作
def conv2d(name, l_input, w, b):
    return tf.nn.relu(tf.nn.bias_add(tf.nn.conv2d(l_input, w, strides=[1, 1, 1, 1], padding='SAME'),b), name=name)
 
# 最大下采样操作
def max_pool(name, l_input, k):
    return tf.nn.max_pool(l_input, ksize=[1, k, k, 1], strides=[1, k, k, 1], padding='SAME', name=name)
 
# 归一化操作
def norm(name, l_input, lsize=4):
    return tf.nn.lrn(l_input, lsize, bias=1.0, alpha=0.001 / 9.0, beta=0.75, name=name)

#定义所有网络参数    
weights={
        "wc1":tf.Variable(tf.random_normal([11,11,1,96])),
        "wc2":tf.Variable(tf.random_normal([5,5,96,256])),
        "wc3":tf.Variable(tf.random_normal([3,3,256,384])),
        "wc4":tf.Variable(tf.random_normal([3,3,384,384])),
        "wc5":tf.Variable(tf.random_normal([3,3,384,256])),
        "wd1":tf.Variable(tf.random_normal([4*4*256,4096])),
        "wd2":tf.Variable(tf.random_normal([4096,4096])),
        "out":tf.Variable(tf.random_normal([4096,10]))  
        }
biases={
        "bc1":tf.Variable(tf.random_normal([96])),
        "bc2":tf.Variable(tf.random_normal([256])),
        "bc3":tf.Variable(tf.random_normal([384])),
        "bc4":tf.Variable(tf.random_normal([384])),
        "bc5":tf.Variable(tf.random_normal([256])),
        "bd1":tf.Variable(tf.random_normal([4096])),
        "bd2":tf.Variable(tf.random_normal([4096])),
        "out":tf.Variable(tf.random_normal([n_classes]))
        }
# 定义整个网络 
def alex_net(_X, _weights, _biases, _dropout):
    # 向量转为矩阵
    _X = tf.reshape(_X, shape=[-1, 28, 28, 1])
    
    # 第一层卷积
    # 卷积层
    conv1 = conv2d('conv1', _X, _weights['wc1'], _biases['bc1'])
    # 下采样层
    pool1 = max_pool('pool1', conv1, k=2)
    # 归一化层
    norm1 = norm('norm1', pool1, lsize=4)

    # 第二层卷积
    # 卷积
    conv2 = conv2d('conv2', norm1, _weights['wc2'], _biases['bc2'])
    # 下采样
    pool2 = max_pool('pool2', conv2, k=2)
    # 归一化
    norm2 = norm('norm2', pool2, lsize=4)
 
    # 第三层卷积
    # 卷积
    conv3 = conv2d('conv3', norm2, _weights['wc3'], _biases['bc3'])
    # 归一化
    norm3 = norm('norm3', conv3, lsize=4)

    # 第四层卷积
    # 卷积
    conv4 = conv2d('conv4', norm3, _weights['wc4'], _biases['bc4'])
    # 归一化
    norm4 = norm('norm4', conv4, lsize=4)
 
    # 第五层卷积
    # 卷积
    conv5 = conv2d('conv5', norm4, _weights['wc5'], _biases['bc5'])
    # 下采样
    pool5 = max_pool('pool5', conv5, k=2)
    # 归一化
    norm5 = norm('norm5', pool5, lsize=4)

#    #全连接层1
#    fc1=tf.reshape(norm5,[-1,weights["wd1"].get_shape().as_list()[0]])
#    fc1=tf.add(tf.matmul(fc1,weights["wd1"]),biases["bd1"],name="fc1")
#    fc1=tf.nn.relu(fc1)
#    #dropout
#    fc1=tf.nn.dropout(fc1,dropout)
#    #全连接层2
#    fc2=tf.reshape(fc1,[-1,weights["wd2"].get_shape().as_list()[0]])
#    fc2=tf.add(tf.matmul(fc2,weights["wd2"]),biases["bd2"],name="fc2")
#    fc2=tf.nn.relu(fc2)
#    #dropout
#    fc2=tf.nn.dropout(fc2,dropout)
#    #输出层
#    out=tf.add(tf.matmul(fc2,weights["out"]),biases["out"]) 

# 全连接层1，先把特征图转为向量
    dense1 = tf.reshape(norm5, [-1, _weights['wd1'].get_shape().as_list()[0]])
    dense1 = tf.nn.relu(tf.matmul(dense1, _weights['wd1']) + _biases['bd1'], name='fc1')
    dense1 = tf.nn.dropout(dense1, _dropout)
 
    # 全连接层2
    dense2 = tf.reshape(dense1, [-1, _weights['wd2'].get_shape().as_list()[0]])
    dense2 = tf.nn.relu(tf.matmul(dense1, _weights['wd2']) + _biases['bd2'], name='fc2') # Relu activation
    dense2 = tf.nn.dropout(dense2, _dropout)
 
    # 网络输出层
    out = tf.matmul(dense2, _weights['out']) + _biases['out']
    return out
###########################################################################################
# 构建模型
pred=alex_net(x,weights,biases,keep_prob)
# 定义损失函数和优化器
#cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred,y))  #旧版本  
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = pred, labels = y))
optimizer=tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)
#评估函数
correct_pred=tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
accuracy=tf.reduce_mean(tf.cast(correct_pred,tf.float32))
#
#初始化变量
#init=tf.global_variables_initializer()
init = tf.initialize_all_variables()

#########################################################################################

with tf.Session() as sess:
    sess.run(init)
    step=1
    #开始训练，直到达到training_iters, 即20000
    while step * batch_size < training_iters:
        batch_x, batch_y = mnist.train.next_batch(batch_size)  #获取批数据
        sess.run(optimizer,feed_dict={x: batch_x,y: batch_y,
                                      keep_prob:dropout})
        
        if step % display_step == 0:
            #计算损失值和准确度，输出
            loss,acc=sess.run([cost,accuracy],feed_dict={x: batch_x,
                              y: batch_y,
                              keep_prob:1.})
            print("Iter "+str(step*batch_size)+", Minibatch Loss= "+\
                  "{:.6f}".format(loss)+",Training Accuracy="+\
                  "{:.5f}".format(acc))
        step+=1
    print("Optimization Finished!")
    #计算测试集的准确度
    print("Testing Accuracy:",sess.run(accuracy,feed_dict={x: mnist.test.images[:256],y: mnist.test.labels[:256], keep_prob:1.}))
  
 