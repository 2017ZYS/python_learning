# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:01:35 2019

@author: zhangyushun
"""

import requests
res=requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
res.raise_for_status()
playFile=open("RomeoAndJuliet.txt",'wb')#写二进制
for chunk in res.iter_content(10):
    playFile.write(chunk)
playFile.close()
