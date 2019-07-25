# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:47:19 2019

@author: zhangyushun
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:36:23 2019

@author: zhangyushun
"""
#将某一文件夹下的.py文件压缩打包成zip文件到指定文件夹中
import os,re,zipfile
path_source='.'#(指定需要压缩文件的所在目录)
path_destination=path_source#(指定zip文件所在的目录)
filenames=os.listdir(path_source)
basenameregex=re.compile(r'(\w+)(\.py)')#基本名称分组，一个是名字一个是后缀
for filename in filenames:
    #print(filename)
    namelist=basenameregex.findall(filename)
    if namelist!=[]:
        if '.py'==namelist[0][-1]:
            print(filename+'是py文件，需要压缩')
            #TODO将该文件添加至压缩文件
            newzip=zipfile.ZipFile(os.path.join(path_destination,'newzip.zip'),'a')#指定压缩后的zip文件名称和路径
            newzip.write(os.path.join(path_source,filename),compress_type=zipfile.ZIP_DEFLATED)#添加新的需要压缩的文件
            newzip.close()
