# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:55:19 2019

@author: zhangyushun
"""
#学习scipy的stats模块
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']#为了让图标能显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
####################################################
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
plt.show()
#############################################
##泊松分布
a=np.arange(16)
poi=stats.poisson
lambda_=[1.5,4.25]
colors=["#348ABD","#A60628"]

plt.bar(a,poi.pmf(a,lambda_[0]),color=colors[0],label="$\lambda=%.1f$"%lambda_[0],alpha=0.6,edgecolor=colors[0],lw=3)
plt.bar(a,poi.pmf(a,lambda_[1]),color=colors[1],label="$\lambda=%.1f$"%lambda_[1],alpha=0.7,edgecolor=colors[1],lw=3)
plt.xticks(a+0.4,a)
plt.legend()
plt.ylabel(u"取值k的概率")
plt.xlabel(u"$k$")
plt.title("在不同$\lambda$取值情况下，Poisson随机变量的概率质量函数")
plt.show()

###正态分布
norm_dis = stats.norm(5, 3) # 利用相应的分布函数及参数，创建一个冻结的正态分布(frozen distribution)
x = np.linspace(-5, 15, 101)  # 在区间[-5, 15]上均匀的取101个点


# 计算该分布在x中个点的概率密度分布函数值(PDF)
pdf = norm_dis.pdf(x)

# 计算该分布在x中个点的累计分布函数值(CDF)
cdf = norm_dis.cdf(x)

# 下面是利用matplotlib画图
plt.figure(1)
# plot pdf
plt.subplot(211)  # 两行一列，第一个子图
plt.plot(x, pdf, 'b-',  label='pdf')
plt.ylabel('Probability')
plt.title(r'PDF/CDF of normal distribution')
plt.text(-4.5, .12, r'$\mu=5,\ \sigma=3$')  # 3是标准差，不是方差
plt.legend(loc='best', frameon=False)
# plot cdf
plt.subplot(212)
plt.plot(x, cdf, 'r-', label='cdf')
plt.ylabel('Probability')
plt.legend(loc='best', frameon=False)

plt.show()

##########################
a=np.linspace(0,4,100)
expo=stats.expon#指数分布
lambda_=[0.5,1]
colors=["#348ABD","#A60628"]

for l,c in zip(lambda_,colors):
    plt.plot(a,expo.pdf(a,scale=1./l),lw=3,color=c,label="$\lambda=%.1f$"%l)
    plt.fill_between(a,expo.pdf(a,scale=1./l),color=c,alpha=0.33)

plt.xlabel("z")
plt.ylabel("取值为z的概率密度函数")
plt.xlim(0,4)
plt.ylim(0,1.2)
plt.xticks(np.arange(0,4.1,0.5))
plt.yticks(np.arange(0,1.3,0.2))
plt.title("不同$\lambda$取值情况下，指数分布的概率密度函数")
plt.legend()    
    
#####################
from scipy.stats import binom
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np    


count_data=np.loadtxt("./贝叶斯方法  概率编程与贝叶斯推断 附代码/bcode/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers-master/Chapter1_Introduction/data/txtdata.csv")
#count_data=np.loadtxt("data/txtdata.csv")
n-count_data=len(count_data)
plt.bar(np.arange(n_count_data),count_data,color="#3448ABD")
plt.xlabel
import pymc as pm
alpha=1.0/count_data.mean()
lambda_1=pm.Exponential("lambda_1",alpha)
lambda_2=pm.Exponential("lambda_2",alpha)

print("Random output:",tau.random(),tau.random(),tau.random())


#####################
from scipy.stats import binom
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
 
## 设置属性防止中文乱码
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
fig,ax = plt.subplots(1,1)
n = 100
p = 0.5
#平均值, 方差, 偏度, 峰度
mean,var,skew,kurt = binom.stats(n,p,moments='mvsk')
print (mean,var,skew,kurt)
#ppf:累积分布函数的反函数。q=0.01时，ppf就是p(X<x)=0.01时的x值。
x = np.arange(binom.ppf(0.01, n, p),binom.ppf(0.99, n, p))
plt.plot(x, binom.pmf(x, n, p),'o')
plt.title(u'二项分布概率质量函数')
plt.show()