# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:05:32 2019

@author: zhangyushun
"""

#学习使用matplotlib 
import numpy as np 
from matplotlib import pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei']#为了让图标能显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
x = np.arange(1,11) 
y =  2  * x +  5 
plt.plot(x,y) 
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.show()
##
x = range(10)  # 横轴的数据
y = [i*i for i in x]  # 纵轴的数据,列表解析：将for循环和创建新元素的代码合并成一行
plt.plot(x, y,'+r-')  # 调用pylab的plot函数绘制曲线
plt.show()  # 显示绘制出的图
plt.xlabel(u"我是横轴")
plt.ylabel(u"我是纵轴")
##
plt.plot(x, y, 'ob-', label=u'y=x^2曲线图')  # 加上label参数添加图例
plt.legend()  # 让图例生效
plt.title(u'图像标题') # 字符串也需要是unicode编码
##
x = list(range(10))+[100]
y = [i*i for i in x]
plt.plot(x, y, 'ob-', label=u'y=x^2曲线图')#大量数据聚集在0附近，而少量很大的数据会导致图像显示效果很不好
plt.legend()  # 让图例生效
#限制需要显示的坐标范围：
plt.xlim(-1,11)
plt.ylim(-1,110)
plt.show()

##################
t = np.arange(0.0, 1.01, 0.01)
s = np.sin(2*2*np.pi*t)
plt.plot(t,s,'or-')
plt.fill(t,s*np.exp(-5*t),'b-')
plt.grid(True)
#保存为PDF格式，也可保存为PNG等图形格式
plt.savefig('test.png')
plt.show()


###########################
import numpy as np 
from matplotlib import pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei']#为了让图标能显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

t=np.linspace(0,10,1000)
x=np.sin(t)
y=np.cos(t**2)
plt.figure(figsize=(8,6),dpi=80)
plt.plot(t,x,'g--',label='$sin(x)$',linewidth=3)
plt.plot(t,y,'r-',label='$cos(x^2)$',lw=2)

plt.title("First python figure",fontsize=20)
plt.xlabel('Time(s)',fontsize=20)
plt.ylabel('Amplitude',fontsize=20)
#设置图片边界
plt.xlim([0,10])
plt.ylim([-1.2,1.2])
plt.legend(fontsize=18)  # 让图例生效
plt.tick_params(labelsize=18)#设置坐标轴字体大小
plt.show()
#plt.xlim(t.min()*1.1, t.max()*1.1)
#plt.ylim(y.min()*1.1, y.max()*1.1)

#############################
import numpy as np 
import matplotlib.pyplot as plt 
# 计算正弦和余弦曲线上的点的 x 和 y 坐标 
x = np.arange(0,  3  * np.pi,  0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
# 建立 subplot 网格，高为 2，宽为 1  
# 激活第一个 subplot
plt.subplot(2,  1,  1)  
# 绘制第一个图像 
plt.plot(x, y_sin) 
plt.title('Sine')  
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  
# 展示图像
plt.show()
###########################
from matplotlib import pyplot as plt 
x =  [5,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis') 
plt.show()

# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
import numpy as np 
from matplotlib import pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei']#为了让图标能显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
plt.figure(figsize=(8,6), dpi=80)
# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
plt.subplot(1,1,1)
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plt.plot(X, C,label="cosine", color="blue", linewidth=2.5, linestyle="-")
# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plt.plot(X, S, label="sine",color="green", linewidth=2.5, linestyle="-")
#设置坐标轴范围和刻度
plt.xlim(X.min()*1.1, X.max()*1.1)# 设置横轴的上下限
plt.ylim(C.min()*1.1, C.max()*1.1)# 设置纵轴的上下限
#设置图片边界更好的方式
#xmin ,xmax = X.min(), X.max()
#ymin, ymax = C.min(), C.max()
#dx = (xmax - xmin) * 0.2
#dy = (ymax - ymin) * 0.2
#plt.xlim(xmin - dx, xmax + dx)
#plt.ylim(ymin - dy, ymax + dy)
#plt.xticks(np.linspace(-4,4,9,endpoint=True))# 设置横轴记号
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
#plt.yticks(np.linspace(-1,1,5,endpoint=True))# 设置纵轴记号
plt.legend(loc='upper left')
#给一些特殊点做注释
t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.plot([t,t],[0,np.sin(t)],'r--',lw=2.5)
plt.scatter(t,np.sin(t),50,'b')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
         xy=(t, np.sin(t)), xycoords='data',
         xytext=(+10, +30), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
         xy=(t, np.cos(t)), xycoords='data',
         xytext=(-90, -50), textcoords='offset points', fontsize=16,
         arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)
# 在屏幕上显示
plt.show()
#史蒂夫职业的先验及后验概率
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#为了让图标能显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.figure(figsize=(8,4),dpi=300)
colors=["#348ABD","#A60628"]
prior=[1/21.,20/20.]
posterior=[0.087,1-0.087]
plt.bar([0,0.7],prior,alpha=0.7,width=0.25,align =  'center',color=colors[0],label='先验分布',lw=3,edgecolor=colors[0])
plt.bar([0.25,0.95],posterior,alpha=0.7,width=0.25,align =  'center',color=colors[1],label="后验分布",lw=3,edgecolor=colors[1])
plt.xticks([0+0.25,0.7+0.25],["图书管理员","农民"])#刻度
plt.title("史蒂夫职业的先验及后验概率")
plt.ylabel("概率")
plt.legend(loc="upper left")



"""
    水平条形图，需要修改以下属性
    orientation="horizontal"
"""
import numpy as np
import matplotlib.pyplot as plt

# 数据
N = 5
x = [20, 10, 30, 25, 15]
y = np.arange(N)

# 绘图 x= 起始位置， bottom= 水平条的底部(左侧), y轴， height 水平条的宽度， width 水平条的长度
p1 = plt.bar(x=0, bottom=y, height=0.5, width=x, orientation="horizontal")

# 展示图形
plt.show()


######################################
import scipy.stats as stats
a=np.arange(16)
poi=stats.poisson
lambda_=[1.5,4.25]
colors=["#348ABD","#A60628"]

plt.bar(a,poi.pmf(a,lambda_[0]),color=colors[0],label="$\lambda=%.1f$"%lambda_[0],alpha=0.6,edgecolor=colors[0],lw=3)
plt.bar(a,poi.pmf(a,lambda_[1]),color=colors[1],label="$\lambda=%.1f$"%lambda_[1],alpha=0.7,edgecolor=colors[1],lw=3)
plt.xticks(a+0.4,a)
plt.legend()
plt.ylabel("取值k的概率")
plt.xlabel("$k$")
plt.title("在不同$\lambda$取值情况下，Poisson随机变量的概率质量函数")
plt.show()
#####################################################
#对函数与坐标轴之间的区域进行填充，使用fill函数
import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(0, 5 * np.pi, 1000)
 
y1 = np.sin(x)
y2 = np.sin(2 * x)
#plt.plot(x, y1, label = "$ y = sin(x) $")
#plt.plot(x, y2, label = "$ y = sin(2 * x) $")

plt.fill(x, y1, color = "g", label = "$ y <= sin(x) $",alpha = 0.3)
plt.fill(x, y2, color = "b", label = "$ y <= sin(x) $",alpha = 0.3)
plt.legend(loc = 3)  
plt.show()
###################################################
#填充两个函数之间的区域，使用fill_between函数
x = np.linspace(0, 5 * np.pi, 1000)
 
y1 = np.sin(x)
y2 = np.sin(2 * x)
plt.plot(x, y1, label = "$ y = sin(x) $")
plt.plot(x, y2, label = "$ y = sin(2 * x) $") 
plt.fill_between(x, y1, y2,color = "y", alpha = 0.3)
 
plt.show()
#当y1在y2上方的时候，填充为蓝色，
#
#当y2在y1上方的时候，填充为黄色，
#
#在fill_between中使用where语句进行填充

# interpolate 自动填充空白，当x取得离散点差距较大时，
# 显示的时候两个函数之间的区域可能有空白存在，interpolate 就是用来填充这部分区域
plt.fill_between(x, y1, y2, where= y1 >= y2, facecolor = "blue", interpolate= True)
plt.fill_between(x, y1, y2, where= y2 > y1, facecolor = "yellow", interpolate= True)
 
plt.show()
################################################
#三维曲面
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()

