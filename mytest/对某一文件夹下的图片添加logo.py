# -*- coding: utf-8 -*-
"""
Created on Fri May 17 18:50:02 2019

@author: zhangyushun
"""

import os
from PIL import Image

SQUARE_FIT_SIZE=300
LOGO_FILENAME="catlogo.png"

logoIm=Image.open(LOGO_FILENAME)
logoCopyIm=logoIm.copy()
logoCopyIm=logoCopyIm.resize((80,80))

logowidth,logoheight=logoCopyIm.size

os.makedirs("withLogo",exist_ok=True)

for filename in os.listdir("."):
    if not (filename.endswith(".png") or filename.endswith(".jpg"))\
         or filename==LOGO_FILENAME:
             continue
    print("处理图片:"+filename)
    im=Image.open(filename)
    width,height=im.size
    #检查图片是否需要调整
    if width>SQUARE_FIT_SIZE and height>SQUARE_FIT_SIZE:
        if width>height:#太宽，宽度设为指定大小，高度按比例缩放
            height=int((SQUARE_FIT_SIZE/width)*height)
            width=SQUARE_FIT_SIZE
        else:#太高，高度设为指定大小，宽度按比例缩放
            width=int((SQUARE_FIT_SIZE)/height*width)
            height=SQUARE_FIT_SIZE
        #调整图片大小
        print("调整图片:"+filename)
        im=im.resize((width,height))
    #添加LOGO
    print("添加LOGO到图片："+filename)
    im.paste(logoCopyIm,(width-logowidth,height-logoheight),logoCopyIm)#将logo添加到im图片的指定位置
    #im.paste(logoCopyIm,(width-logowidth,height-logoheight))#将logo添加到im图片的指定位置

    im.save(os.path.join("withLogo",filename))
        
        
           