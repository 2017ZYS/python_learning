# -*- coding: utf-8 -*-
"""
Created on Wed May 15 20:36:50 2019

@author: zhangyushun
"""


#表示一段时间
import datetime
delta=datetime.timedelta(days=11,hours=10,minutes=9,seconds=8)
delta.days,delta.minutes,delta.microseconds
delta.total_seconds()
str(delta)
#日期运算
dt=datetime.datetime.now()
thousandDays=datetime.timedelta(days=1000)#计算1000天之后的日期
dt+thousandDays

dt=datetime.datetime(2015,10,21,16,29,0)
aboutThirtyYears=datetime.timedelta(days=365*30)
dt
dt-aboutThirtyYears
dt-2*aboutThirtyYears
#将时间显示为特定格式
dt.strftime("%Y/%m/%d %H:%M:%S")

