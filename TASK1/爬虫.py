# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:49:05 2019

@author: 19045847
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:43:49 2019

@author: 19045739
"""


from bs4 import BeautifulSoup
import requests
import xlrd
if __name__=='__main__':
    url='https://search.suning.com/%E5%B0%8F%E7%B1%B3/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    req = requests.get(url=url, headers=headers)
#    req=requests.get(url=url,headers=headers)
    req.encoding = 'utf-8'
    html=req.text
#    print(html)
    bf=BeautifulSoup(html,'lxml')
#    print(type(bf.find('div',class_='img-block')))
    img_url=bf.find_all('div',class_='img-block')
    print(len(img_url))
    i = 120
    for each in img_url:
        print(i)
        name=each.img.get('alt')+'.jpg'
        path=r'C:\Users\ZYS\Desktop\python_learning\TASK1\web_images'
        file_name = path + '\\' + str(i) + '.jpg'
        i += 1
        try:
            req1=requests.get('http:'+each.img.get('src'),headers=headers)
            f=open(file_name,'wb')
            f.write(req1.content)
            f.close()
        except:
            print("some error")