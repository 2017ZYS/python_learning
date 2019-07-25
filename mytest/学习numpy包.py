# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:56:37 2019

@author: zhangyushun
"""

#学习numpy基础知识
#NumPy的主要对象是同类型的多维数组。它是一张表，所有元素（通常是数字）的类型都相同，
#并通过正整数元组索引。在NumPy中，维度称为轴。轴的数目为rank。
#arange()类似于内置函数range()，通过指定开始值、终值和步长创建表示等差数列的一维数组，注意得到的结果数组不包含终值。
#linspace()通过指定开始值、终值和元素个数创建表示等差数列的一维数组，可以通过endpoint参数指定是否包含终值，默认值为True，即包含终值。

import numpy as np
a = np.arange(15).reshape(3, 5)
type(a)#NumPy的数组类被称为ndarray,别名为 array
a.shape#数组的维度。这是一个整数的元组，表示每个维度中数组的大小。对于有n行和m列的矩阵，shape将是(n,m)。
a.ndim#数组的轴（维度）的个数。在Python世界中，维度的数量被称为rank

a=np.arange(20).reshape(2,2,5)#先分成2大组，每大组再分成2行到5列

a.ndim#这里有三个轴（维数）
a.size#数组元素的总数。这等于shape的元素的乘积
a.dtype.name#一个描述数组中元素类型的对象
a.itemsize#数组中每个元素的字节大小
#可以以使用array函数从常规Python列表或元组中创建数组
a=np.array([2,3,4])
b = np.array((1.2, 3.5, 5.1))

b = np.array([(1.5,2,3), (4,5,6)])
c = np.array( [ [1,2], [3,4] ], dtype=complex )


np.zeros(4, np.int)
np.zeros(4,int)
np.zeros(4)
np.ones(4,float)
np.ones(4,complex)
np.full(4, np.pi)#full()将数组元素初始化为指足的值
a=np.random.random((3,4))

b=np.ones_like(a)
b=np.zeros_like(a)
b=np.empty_like(a)
b=np.full_like(a,3)
a=np.arange(10)
a[:]
a[:-1]
a[::-1]

a = np.arange(5) 
b = np.arange(4., -1, -1) 
print (a == b)
print (a > b)
print (np.logical_or(a == b, a > b) )# 和 a>=b 相同
print (np.logical_and(a == b, a > b) )


#要创建数字序列，NumPy提供了一个类似于 range 的函数，该函数返回数组而不是列表。
a=np.arange(10,20,2)

np.ones( (2,3,4), dtype=np.int16 ) 
from math import pi
x = np.linspace( 0, 2*pi, 100 )
f=np.sin(x)

#打印数组
import numpy as np
a=np.arange(6)
print(a)

b=np.arange(12).reshape(4,3)
print(b)

c = np.arange(24).reshape(2,3,4)
print(c)

#基本操作
a=np.array([20,30,40,50])
b=np.arange(4)
c=a-b
b**2
10*np.sin(a)
a<35
#与许多矩阵语言不同，乘法运算符 * 的运算在NumPy数组中是元素级别的
A=np.array([[1,1],
            [0,1]])
B=np.array([[2,0],[3,4]])
A*B
#矩阵乘积可以使用 dot 函数或方法执行
A.dot(B)
np.dot(A,B)


a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
b.dtype.name



a = np.random.random((2,3))
a.sum()
a.min()
a.max()
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
a=np.arange(10)
a[2]
a[2:5]
a[:4:2]=-1000#从0元素到4元素，每隔2个元素取
a[ : :-1]#倒过来
for i in a:
    print(i**(1/3.))
#多维情形    
b=np.arange(20).reshape(5,4)
b    
b[2,3]
b[0:5,1]#b的第二列的0到5行，跟matlab一样
b[:,1]#b的第二列的所有行，跟前面一样
b[1:3,:]#第二行到第三行的每列
#迭代（Iterating） 多维数组是相对于第一个轴完成的
for row in b:
    print(row)#打印行向量
for column in b.T:
    print(column)#打印列向量
#如果想要对数组中的每个元素执行操作，可以使用 flat 属性
for element in b.flat:
    print(element)#从左到右，从上到下
    
print(a[2,4])#要索引2D（二维）数组，我们只需引用行数和列数即可。
print(a[0, 1:4]) #0行的 1:3列，对于2D数组，我们的第一片定义了行的切片，第二片定义了列的切片。
print(a[1:4, 0]) 
print(a[::2,::2])

#形状操作
a = np.floor(10*np.random.random((3,4)))
a.shape
a.ravel() #fattened array
a.reshape(6,2)#12个元素重新安排成6*2的array并返回,但是原来的a不会改变
a.T#转置
a.reshape(3,-1)#reshape操作中将维度指定为-1，则会自动计算其他维度,这里是4
a.resize(6,2)#跟reshape不同，改变形状的是a自己
#将不同数组堆叠在一起
a=np.floor(10*np.random.random((2,2)))         
a
b=np.floor(10*np.random.random((2,2)))
b
np.vstack((a,b)) #纵向堆叠        
np.hstack((a,b)) #横向堆叠
np.row_stack((a,b))#相当于vstack
np.column_stack((a,b))  #相当于hstack
#复制和视图
#简单赋值不会创建数组对象或其数据的拷贝。   
a=np.arange(12)   
b=a#没有新对象被创建
b is a
b.shape=[4,3]
b.shape=4,3
a.shape=(3,4)
a         
id(a)
id(b)
#视图或浅复制    
c=a.view()
c is a
id(c)
id(a)
c.base is a# c is a view of the data owned by a
c.shape = 2,6                      # a's shape doesn't change
a.shape
c[0,4] = 1234                      # a's data changes
a
#深拷贝
d=a.copy()
d is a
d.base is a # d doesn't share anything with a
d[0,0]=9999
a
#花式索引
a = np.arange(12)**2                       # the first 12 square numbers
i = np.array( [ 1,1,3,8,5 ] )              # an array of indices
a[i]                                       # the elements of a at the positions i
j = np.array( [ [ 3, 4], [ 9, 7 ] ] )  
a[j]                            # the same shape as j

palette = np.array( [ [0,0,0],                # black
                       [255,0,0],              # red
                       [0,255,0],              # green
                      [0,0,255],              # blue
                       [255,255,255] ] )       # white
image = np.array( [ [ 0, 1, 2, 0 ],           # each value corresponds to a color in the palette
                     [ 0, 3, 4, 0 ]  ] )
palette[image]                            # the (2,4,3) color image
       
#给出多个维度的索引。每个维度的索引数组必须具有相同的形状      
a = np.arange(12).reshape(3,4)
i = np.array( [ [0,1],                        # indices for the first dim of a
               [1,2] ] )
j = np.array( [ [2,1],                        # indices for the second dim
                [3,3] ] )
a[i,j]
#使用布尔值作为数组索引
a=np.arange(12).reshape(3,4)
b=a>4
a[b]#将a中大于4的元素取出
a[b] = 0## All elements of 'a' higher than 4 become 0
a 
 

a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])             # first dim selection
b2 = np.array([True,False,True,False])       # second dim selection
a[b1,:]                                   # selecting rows
a[b1]# same thing as before
a[:,b2]
a[b1,b2]

import numpy as np
import matplotlib.pyplot as plt
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu,sigma=2,0.5
v=np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, normed=1)       # matplotlib version (plot)
plt.show()

(n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
plt.plot(.5*(bins[1:]+bins[:-1]), n)#计算分段区间中间横坐标位置（有点技巧性）为x,n为y
plt.show()
a=np.random.random((10,2))
a.max()
print(np.__version__)
np.full((3,3),True,dtype=bool)
np.full((3,3),3,dtype=int)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2==1]

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)#获取数组a和数组b之间的公共项
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
# From 'a' remove all of 'b'
np.setdiff1d(a,b)

arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
out

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
#如何得到两个数组元素匹配的位置？
np.where(a == b)#输出满足条件的元素的坐标
#获取5到10之间的所有项目。
#method1
a=np.array([2,6,1,9,10,3,27])
index=np.where((a>=5)&(a<=10))
a[index]
#method2
a[(a >= 5) & (a <= 10)]
#如何反转二维数组的行？
arr = np.arange(9).reshape(3,3)
arr[::-1]#等同于arr[::-1,:]
#如何反转二维数组的列？
arr = np.arange(9).reshape(3,3)
arr[:, ::-1]
#创建一个形状为5x3的二维数组，以包含5到10之间的随机十进制数。
rand_arr=np.random.randint(low=5,high=10,size=(5,3))#返回[low,high)范围内的整数值
rand_arr1=rand_arr+np.random.random((5,3))
#####注意区分！！！！！### 
#random.randint(a, b)     # python random模块的返回闭区间 [a, b] 范围内的整数值
#np.random.randint(a, b)   # 返回开区间 [a, b) 范围内的整数值

    
    
# Limit to 3 decimal places
rand_arr = np.random.random((5,3))
np.set_printoptions(precision=3)
rand_arr[:4,:]
rand_arr[:4]
#从一维numpy数组中删除所有NaN值
#inf和nan的不同在于，inf是一个超过浮点表示范围的浮点数（其本质仍然是一个数，只是他无穷大，因此无法用浮点数表示，比如1/0），
#而nan则一般表示一个非浮点数（比如无理数）
import numpy as np
a=np.array([1,2,3,np.nan,5,6,7,np.nan])
a[np.where(~np.isnan(a))]#根据非nan的元素的位置取得数组
a[~np.isnan(a)]#根据非nan的元素的位置取得数组
#Python扩展库numpy中where()函数的三种用法
#第一种用法：只给where()函数传递一个数组作为参数，返回其中非0元素的下标。
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([[1,0,3],
            [4,5,0]])
print(np.where(x))
print(np.where(y))#返回array的元组，第一个是行下标，第二个是列下标
#第二种用法：给where()函数传递一个包含True/False值的数组，返回该数组中True值的下标，
#结合numpy数组的关系运算，可以返回数组中符合特定条件的元素的下标。
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([[1,0,3],
            [4,5,0]])
print(np.where(x%2==1))#返回数组中True值得下标
print(x[np.where(x%2==1)])#提取出奇数
print(np.where(y>2))
print(y[np.where(y>2)])#返回y中大于2的元素
#第三种用法：给where()函数传递一个条件数组和两个值或数组，对于条件数组中等价于True的位置，
#从第一个值或数组中取值进行替换，否则从第二个值或数组中取值进行替换。
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([[1,0,3],
            [4,5,0]]) 
print(np.where(x%2==1,x,-x))
print(np.where(y%2==1,1,-1))
print(np.where(y,[30,40,50],[60,70,80]))
#如何计算两个数组之间的欧氏距离？
a=np.array([1,2,3,4,5])
b=np.array([4,5,6,7,8])
dist=np.linalg.norm(a-b)
dist


a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
doublediff = np.diff(np.sign(np.diff(a)))
peak_locations = np.where(doublediff == -2)[0] + 1
peak_locations
import numpy 
# svd
import numpy as np
U,Sigma,VT=np.linalg.svd([[1,1],[7,7]])
U
Sigma
VT
np.dot(U,Sigma)
#找出x中数字1的第5次重复的索引
x = np.array([1, 2, 1, 1, 3, 4, 3, 1, 1, 2, 1, 1, 2])
n=5
index=np.where(x==1)[0][n-1]#法一，借助where函数[0]是定位返回的元组的第一个array:array([ 0,  2,  3,  7,  8, 10, 11], dtype=int64)

[i for i, v in enumerate(x) if v == 1][n-1]#法二，借助enumerate和if 语句的列表解析
#中位数计算
import numpy as np 
 
a = np.array([[10, 7, 4], [3, 2, 1]])
print ('我们的数组是：')
print (a)
print ('调用 percentile() 函数：')
# 50% 的分位数，就是 a 里排序之后的中位数
print (np.percentile(a, 50)) 
 
# axis 为 0，在纵列上求
print (np.percentile(a, 50, axis=0)) 
# axis 为 1，在横行上求
print (np.percentile(a, 50, axis=1)) 
#矩阵的逆
import numpy as np 
 
x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print (x)
print(y)
 
# 保存到 outfile.npy 文件上
np.save('outfile.npy',a) 
b = np.load('outfile.npy')  
print (b)
#画三角形图像
def triangle_wave(x, c, c0, he):
      x = x - int(x) #三角波的周期为1，因此只取x坐标的小数部分进行计算
      if x >= c: r = 0.0
      elif x < c0: r = x / c0 * he
      else: r = (c-x) / (c-c0) * he
      return r
x = np.linspace(0,2, 1000)
y1 = np.array([triangle_wave(t, 0.6, 0.4, 1.0) for t in x])
plt.plot(x,y1)
#通过frompyfunc()可以将计算单个值的函数转换为能对数组的每个元素进行计兑的ufunc()函数
triangle_ufunc1 = np.frompyfunc(triangle_wave, 4, 1) 
x = np.linspace(0,2, 1000)
y2 = triangle_ufunc1(x, 0.6, 0.4, 1.0)#这里x是数组了，不是单个值了
plt.plot(x,y2)
plt.plot(y1-y2)

x,y = np.mgrid[:5,:5]
#二项式分布
a = numpy.random.binomial(n=10, p=0.7, size = 1)#其三个参数分别为试验次数、正例概率和采样个数
#多项式分布
a = numpy.random.multinomial(n=10, pvals=[0.2,0.4,0.4], size = 1) 
a = np.ones((2,3), dtype=int)


