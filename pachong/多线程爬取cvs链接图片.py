# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 00:12:28 2019

@author: ZYS
"""

import requests
import time
import threading
import queue
import csv
import numpy as np
#import os


exampleFile=open("exportData.csv")
exampleReader=csv.reader(exampleFile)

exampleData=list(exampleReader)

exampleData=exampleData[2:]
Data=np.array(exampleData)
urls=Data[:,3]#URL列表
urls=urls[1:100]
q = queue.Queue()
for url in urls:
    #print(url)
    url.strip()
    q.put(url)
start = time.time()
def fetch_img_func(q):
    while True:
        try:
            url = q.get_nowait()# 不阻塞的读取队列数据
            i = q.qsize()
        except Exception as e:
            print (e)
            break
        # print ('Current Thread Name Runing %s ... ' % threading.currentThread().name)
        print("当前还有%s个任务"% i)
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            save_img_path ='img/%s.png'%i
            # 保存下载的图片
#            with open(save_img_path, 'wb') as fs:
#                for chunk in res.iter_content(1024):
#                    fs.write(chunk)
            with open(save_img_path, 'wb') as f:
                 f.write(res.content) 
num=10  #线程数
threads =[]
for i  in range(num):
    t = threading.Thread(target=fetch_img_func, args=(q, ), name="child_thread_%s"%i)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join()

print(time.time()-start)
