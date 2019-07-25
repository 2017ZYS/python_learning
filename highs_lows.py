# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 19:37:07 2018

@author: zhangyushun
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime
#从文件中获取日期、最高气温和最低气温
#filename='sitka_weather_07-2014.csv'
#filename='sitka_weather_2014.csv'
filename='death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    #print(header_row)
#    for index, column_header in enumerate(header_row):
#        print(index,column_header)

    dates, highs, lows=[],[],[]
    for row in reader:
        try:    
            current_date=datetime.strptime(row[0],"%Y-%m-%d")   
            high=int(row[1])                
            low=int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
#    print(highs)
#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#设置图形的格式
#plt.title("Daily high and low temperatures, July 2014", fontsize=24)
title="Daily high and low temperatures -2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
#plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#绘制斜的日期标签，以免它们彼此重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()


#first_date=datetime.strptime('2014-7-1','%Y-%m-%d')
#print(first_date)
    