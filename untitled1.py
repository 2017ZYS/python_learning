# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 23:18:36 2019

@author: ZYS
"""

import xlrd
import requests
import os

workbook = xlrd.open_workbook(r'exportData.xlsx')

exportData = workbook.sheet_by_index(0)

#for i in range(64):
#    print(i)
#    row = sheet1.row_values(i)[0]
#    print(row)
os.makedirs('D:/7_24_1/')
os.makedirs('D:/7_24_3/')
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
for i in range(2, 28824):
    print(i)
    img_url = exportData.row_values(i)[3]
    print(img_url)
    label = exportData.row_values(i)[4]
#    print(label)
    img = requests.get(img_url.strip())
#    print(img)
    if label.strip() == '1':
        print("111111")
        file_name = 'D:/7_24_1/'+img_url.strip()[-16:]
    if label.strip() == '3':
        print("33333")
        file_name = 'D:/7_24_3/'+img_url.strip()[-16:]
    f = open(file_name, 'wb')
    f.write(img.content)
    f.close()
