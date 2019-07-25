# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:03:32 2019

@author: zhangyushun
"""
spam=0
while spam<5:
    print("Hello world!")
    spam+=1
for i in range(5):
    print(i)
for i in range(1,6):
    print(i)
for i in range(1,6,2):
    print(i)
    
import random
for i in range(5):
    print(random.randint(1,10))
    

import sys
while True:
    print("Type exit to exit.")
    response=input()
    if response=='exit':
        sys.exit()
    print("You typed "+response +'.')
spam=['cat','bat','rat','elephant']
spam[0]
spam[2]="hello"
['cat','bat','rat','elephant'][3]

eggs=("hello",42,0.5)
eggs[0]
eggs[1:3]
type(("hello",))
type(("hello"))
tuple(['cat','dog',5])
list(('cat','dog',5))
spam=['a','b','c','d']
bacon=[]

import copy 
spam=['A','B','C','D']
cheese=copy.copy(spam)
cheese[1]=42

spam=['A','B','C','D',['a','b','c','d']]
cheese=copy.copy(spam)
cheese1=copy.deepcopy(spam)
cheese[1]=42
cheese[2]=5
cheese[4][0]=5
cheese1[1]=42
cheese1[2]=5
cheese1[4][1]=5

grid=[['.','.','.','.','.','.'],
      ['.','0','0','.','.','.'],
      ['0','0','0','0','.','.'],
      ['0','0','0','0','0','.'],
      ['.','0','0','0','0','0'],
      ['0','0','0','0','0','.'],
      ['0','0','0','0','.','.'],
      ['.','0','0','.','.','.'],
      ['.','.','.','.','.','.']
      ]
for i in range(6):
    for j in range(9):
        print(grid[j][i],end='')
    print("")

spam={"color":'red','age':42}
spam.keys()
spam.setdefault('color','black')

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

print(pprint.pformat(count))

theBoard={'top-L':"",'top-M':"",'top-R':"",
          'mid-L':"",'mid-M':"",'mid-R':"",
          'low-L':"",'low-M':"",'low-R':""}#表示空的井字棋盘

allGuests={'zhangyushun':{"apples":5,"pretzels":12},
           'bob':{"ham sandwiches":3,"apples":2},
           'Carol':{"cups":3,"apple pies":1}}
messages='COMMENTS FOR THE AUTHOR:\
Reviewer #1: This paper proposed a new fault detection and classification method for rolling bearings. The three stages including feature extraction, dictionary pair creation, and fault pattern recognition. Overall the paper interesting. Additional comments are as follows:\
1) The authors should emphasize their main contribution and the novelty of the work. What is the explanation behind combining DPL and CR classification? \
2) More details can be included in Figure 1. And Chapter 2 should be focusing on the proposed method rather than theory introduction. For example, dimensional reduction using PCA is not illustrated anywhere in the paper. \
3) In the experiment part, how are the parameters been determined? Is there any parameter tuning process for both proposed method and other machine learning methods? \
4) In page 9, the reason to explain only 20 data samples are used for the training process is not convincing. Please either include more samples for training or explain it clearly.\
5) Computational space and time complexities should also be considered and compared.\
Reviewer #2: The opinion of this evaluator is that the scientific contribution of the article is marginal, but it is grounded and seeks to be self-contained. The problem is well placed and its properties and constraints are made explicit. The notation is consistent and the bibliography is satisfactory. However, authors should only revise written language, specifically in the introduction section, to increase the clarity and comprehension of the text in some passages. The following points should be improved in the article.\
\
The physical foundations of the model adopted in equations (14) are not in the text. Authors should do so or refer to it.\
The authors say in Section 4.1 (Experiment on simulated data) that the index in (15) is introduced in the paper. This index is then abandoned in section 4.2 (Real data experiment). It is not clear that this index differs from accuracy, widely used, calculated from the confusion matrix.\
The confusion matrices resulting from the experiments should be included in the article and their results should be interpreted.\
The results of Section 4.2 can not be taken as definitive. The data in Section 4.2 are valid data, obtained from the laboratory bench but are not data from a real operation. The performance of the method still needs to be proven in real operating situation. This should be said.\
The captions of some figures should be enriched to facilitate their autonomous reading.\
Clarify TD (x) in the text and in Algorithm 1.'


messages="""COMMENTS FOR THE AUTHOR:

Reviewer #1: This paper proposed a new fault detection and classification method for rolling bearings. The three stages including feature extraction, dictionary pair creation, and fault pattern recognition. Overall the paper interesting. Additional comments are as follows:
1) The authors should emphasize their main contribution and the novelty of the work. What is the explanation behind combining DPL and CR classification? 
2) More details can be included in Figure 1. And Chapter 2 should be focusing on the proposed method rather than theory introduction. For example, dimensional reduction using PCA is not illustrated anywhere in the paper. 
3) In the experiment part, how are the parameters been determined? Is there any parameter tuning process for both proposed method and other machine learning methods? 
4) In page 9, the reason to explain only 20 data samples are used for the training process is not convincing. Please either include more samples for training or explain it clearly.
5) Computational space and time complexities should also be considered and compared.


Reviewer #2: The opinion of this evaluator is that the scientific contribution of the article is marginal, but it is grounded and seeks to be self-contained. The problem is well placed and its properties and constraints are made explicit. The notation is consistent and the bibliography is satisfactory. However, authors should only revise written language, specifically in the introduction section, to increase the clarity and comprehension of the text in some passages. The following points should be improved in the article.

The physical foundations of the model adopted in equations (14) are not in the text. Authors should do so or refer to it.

The authors say in Section 4.1 (Experiment on simulated data) that the index in (15) is introduced in the paper. This index is then abandoned in section 4.2 (Real data experiment). It is not clear that this index differs from accuracy, widely used, calculated from the confusion matrix.

The confusion matrices resulting from the experiments should be included in the article and their results should be interpreted.

The results of Section 4.2 can not be taken as definitive. The data in Section 4.2 are valid data, obtained from the laboratory bench but are not data from a real operation. The performance of the method still needs to be proven in real operating situation. This should be said.

The captions of some figures should be enriched to facilitate their autonomous reading.

Clarify TD (x) in the text and in Algorithm 1.
"""



#打印一段话里出现的字符和相应的次数
count={}#创建字典存放出现的字符（键）和相应的次数（值）
for character in messages:
    count.setdefault(character,0)#确保了具体的字符在count的键中且默认的值为0
    count[character]+=1
import pprint
pprint.pprint(count)
    
spam="This is zhangyushun's car"    
spam='This is zhangyushun\'s car'
spam=r'This is zhangyushun\'s car'

spam='Hello world!'
spam=spam.upper()
spam=spam.lower()
spam.islower()
spam.isupper()
'hello'.isalpha()
'hello123'.isalpha()
'hello123'.isalnum()
'123'.isdecimal()
' '.isspace()
'This is a movie'.istitle()
'This Is A Movie'.istitle()
while True:
    print("请输入您的年龄:")
    age=input()
    if age.isdecimal():#判断是数字
        break
    print("请输入你年龄的数字而不是文字！")
while True:
    print("请输入新的密码（只包含字母和数字）")
    password=input()
    if password.isalnum():
        break
    print("密码只包含字母和数字！")
        
import pyperclip
pyperclip.copy("Hello world!")    
pyperclip.paste()


import re
message='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#mo=phoneNumRegex.search('My number is 415-555-4242')
mo=phoneNumRegex.search(message)
mo.group(1)
mo.group(2)
mo.group(0)
mo.groups()
phoneNumRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search('My number is (415)-555-4242')
mo.group(1)
mo.group(2)

heroRegex=re.compile(r'Batman|Tina Fey')
mo1=heroRegex.search('Batman and Tina Fey')
mo1.group(0)
mo2=heroRegex.search('Tina Fey and Batman')
mo2.group(0)
batRegex=re.compile(r'Bat(man|mobile|copter|bat)')
mo=batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)
#用问好实现可选匹配
import re
batRegex=re.compile(r'Bat(wo)?man')
mo1=batRegex.search("The advantage of Batman")
mo1.group()

mo2=batRegex.search("The advantage of Batwoman")
mo2.group()

phoneRegex=re.compile(r'(\d\d\d)? \d\d\d-\d\d\d\d')
mo1=phoneRegex.search('My name is 415 555-4242')
mo1.group()

batRegex=re.compile(r'Bat(wo)+man')
mo=batRegex.search("The Advantures of Batman")
mo==None


phoneNumRegex=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
phoneNumRegex.findall('cell:415-555-9999 work:212-555-0000')
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('cell:415-555-9999 work:555-0000')

import re
xmasRegex=re.compile(r'\d+\s\w+')
xmasRegex.findall('12 dreumers, 11 pipers, 10 lords, 9 ladies, 8 maids,\
7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

beginWithHello=re.compile(r'^Hello')
beginWithHello.search('Hello woeld！')

endWithHello=re.compile(r'\d$')
endWithHello.search('Hello woeld! my number is 27')

wholeStringIsNum=re.compile(r'^\d+$')
wholeStringIsNum.findall('123dfadsdf4567890')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.findall('1234567890')

atRegex=re.compile(r'.at')#通配符
atRegex.findall('The cat in the hat sat on the flat mat.')
#用点星匹配所有字符
nameRegex=re.compile(r'First Name:(.*) Last Name:(.*)')
mo=nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)

regex1=re.compile('RoboCop')
regex2=re.compile('ROBOCOP')
regex3=re.compile('robOcop')
regex4=re.compile('RobocOp')
robocop=re.compile(r'robocop',re.I)
robocop.search('RoboCop is part man ,part machine, all cop.').group()
robocop.search('ROBOCOP is part man ,part machine, all cop.').group()
robocop.findall('ROBOCOP and RoboCop is part man ,part machine, all cop.')

nameRegex=re.compile(r'Agent \w+')
nameRegex.sub('CENSORED','Agent Alice gave the secret documents to Agent Bob.')
agentNameRegex=re.compile(r'Agent (\w)\w*')
agentNameRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve\
knew Agent Bob was a double agent.')

import os
os.getcwd()

os.makedirs('C:\\delicious\\walnut\\waffles')
os.path.abspath('.')
os.path.abspath('.\\mytest')

path='C:\\Windows\\System32\\calc.exe'
os.path.basename(path)
os.path.dirname(path)

calcFilePath='C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)
(os.path.dirname(calcFilePath),os.path.basename(calcFilePath))

a=os.path.sep
path='C:\\Windows\\System32\\calc.exe'
os.path.getsize(path)
os.path.getsize('C:\\Windows\\System32\\calc.exe')
os.listdir('C:\\Windows\\System32')#该文件下文件名字符串列表
totalSize=0
for filename in os.listdir('C:\\Windows\\System32'):
   # totalSize+=os.path.getsize('C:\\Windows\\System32\\'+foldername)
    totalSize+=os.path.getsize(os.path.join('C:\\Windows\\System32',filename))
print(totalSize)

os.path.isdir('C:\\Windows\\System32')
os.path.isdir(path)
os.path.isfile(path)

MyFile=open("F:\\360MoveData\\Users\\zhangyushun\\Desktop\\python_learning\\mytest\\test.py",'r',encoding='UTF-8')
MyFileContent=MyFile.read()
MyFileContent=MyFile.readline()
MyFileContent=MyFile.readlines()
MyFile.close()

os.getcwd()
baconFile=open('bacon.txt','w')
baconFile.write('Hello world!\n')
baconFile.close()

baconFile=open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable')
baconFile.close()

baconFile=open('bacon.txt','r')
baconFileContent=baconFile.read()
baconFile.close()
print(baconFileContent)


import shelve
shelfFile=shelve.open('mydata')
cats=['Zophie','Pooka','Simon']
shelfFile['cats']=cats
shelfFile.close()

shelfFile=shelve.open('mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()

import pprint
cats=[{'name':'Zophie','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
pprint.pformat(cats)

fileobj=open('mycats.py','w')
fileobj.write('cats='+pprint.pformat(cats)+'\n')
fileobj.close()
import mycats
mycats.cats
mycats.cats[0]
mycats.cats[0]['name']

import os,shutil
shutil.copy(".\\bacon.txt",'.\\mytest')#相对路径
shutil.copy('bar_char.py','.\\mytest\\bar_char1.py')
shutil.copytree('.\\mytest','.\\mytest1')#mytest1是原先没有的文件夹，程序跑完后会新创建

import shutil,os
shutil.move('.\\mytest\\test.py','.\\mytest1')
shutil.move('.\\mytest1\\test1.py','.\\eggs')

os.listdir()
os.unlink('.\\mytest1\\3.11.2.py')#删除文件
os.rmdir('.\\mytest1')#删除文件夹，该文件夹必须为空
shutil.rmtree('.\\mytest1')#删除文件夹和里面包含的所有文件和文件夹

import send2trash
baconFile=open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
send2trash.send2trash('bacon.txt')#送到垃圾箱里
#遍历目录树
import os
for foldername, subfolders, filenames in os.walk("."):
    print("当前文件夹"+foldername)
    for subfolder in subfolders:
        print("当前文件夹"+foldername+"下的子文件夹："+subfolder)
    for filename in filenames:
        print("当前文件"+foldername+'下的文件字符串：'+filename)
    
    print('')
    
    
import zipfile,os
exampleZip=zipfile.ZipFile('example.zip')
exampleZip.namelist()
abcInfo=exampleZip.getinfo("abc.bat")
abcInfo.file_size
abcInfo.compress_size

exampleZip.extractall('.\\mytest')#解压ZIP文件中的所有文件和文件夹
exampleZip.close()

exampleZip=zipfile.ZipFile('example.zip')
exampleZip.extract('abc.bat','.\\mytest')#只解压单个文件
exampleZip.close()

newzip=zipfile.ZipFile('new.zip','w')#原先没有new.zip将新建这个文件，哪怕有写模式将擦除zip文件中原有的内容
newzip.write('abc.bat',compress_type=zipfile.ZIP_DEFLATED)
newzip.close()
newzip=zipfile.ZipFile('new.zip','a')
newzip.write('bar_char.py')
newzip.close()

import traceback
try:
    raise Exception("This is the error message!")
except:
    errorFile=open('errorInfo.txt','w')    
    print(errorFile.write(traceback.format_exc()))
    errorFile.close()
    print("The traceback info was written to errorInfo.txt")

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctimi)s-%(levelname)s-%(message)s')
logging.debug("你好啊")


import logging  # 引入logging模块
# 将信息打印到控制台上
logging.debug(u"苍井空")
logging.info(u"麻生希")
logging.warning(u"小泽玛利亚")
logging.error(u"桃谷绘里香")
logging.critical(u"泷泽萝拉")
    
    

import logging  # 引入logging模块
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
#logging.disable(logging.CRITICAL)
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')    


##将日志记录到文件
import logging  # 引入logging模块
logging.basicConfig(filename='myProgramLog.log',level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
#logging.disable(logging.CRITICAL)
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')    

spam=9
assert spam>=10,"数据必须大于等于10,而当前数据小于10"

eggs="abc"
bacon="ABC"
assert eggs.lower()!=bacon.lower(),"eggs和bacon的字符串相同"

import random
guess=''
while guess not in ('heads','tails'):
    print("GUESS the coin !输入正或反")   
    guess=input()
#toss=random.randint(0,1)#0 is tails， 1 is heads
toss=random.choice(['heads','tails'])
if toss==guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess=input()
    if toss==guess:
        print("You got it!")
    else:
        print("Nope.You are really bad at this game.")
def printTable(tableData):
    row=len(tableData[0])#每一列有几个字符串
    column=len(tableData)#每一行有几个字符串
    colWidths=[0]*len(tableData)#存放每一列字符串的最大长度数
    for i in range(len(tableData)):
        for characters in tableData[i]:#遍历每一列的字符串得到该列的最长字符串的长度
            length=len(characters)
            if length>=colWidths[i]:
                colWidths[i]=length
    for i in range(row):
        for j in range(column):
            print(tableData[j][i].rjust(colWidths[j]),end=' ')
        print("\n",end='')    
            
tableData=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
printTable(tableData)

row=len(tableData[0])#每一列有几个字符串
column=len(tableData)#每一行有几个字符串
colWidths=[0]*len(tableData)#存放每一列字符串的最大长度数
for i in range(len(tableData)):
    for characters in tableData[i]:
        length=len(characters)
        if length>=colWidths[i]:
            colWidths[i]=length
for i in range(row):
    for j in range(column):
        print(tableData[j][i].rjust(colWidths[j]),end=' ')
    print("\n",end='')     
     
import webbrowser
webbrowser.open("http.//inventwithpython.com/") 


import requests
res=requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
type(res)
res.raise_for_status()
res.status_code==requests.codes.ok
len(res.text)
print(res.text[:250])

res=requests.get("http://inventwithpython.com/page_that_does_not_exit")
res.raise_for_status()

import requests
res=requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
res.raise_for_status()
playFile=open("RomeoAndJuliet.txt",'wb')#写二进制
for chunk in res.iter_content(100000):
    playFile.write(chunk)
    a=chunk
playFile.close()

myfile=open('1.txt','a')                 
myfile.write("HELLO")
myfile.write("GOODBYE")
myfile.close()
myfile=open('1.txt','w')                 
myfile.write("GOODBYE")
myfile.write("HELLO")
myfile.close()

import requests,bs4
res=requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
type(res)
res.raise_for_status()
noSarchSoup=bs4.BeautifulSoup(res.text)
type(noSarchSoup)#有了BeautifulSopu对象，就可以用它的方法，定位HTML文档中的特定部分

exampleFile=open("example.html")
exampleSoup=bs4.BeautifulSoup(exampleFile)#传递一个File对象，返回BeautifulSopu对象
type(exampleSoup)   
elems=exampleSoup.select("'#author'")
type(elems)
len(elems)
type(elems[0])


#处理PDF文件
import PyPDF2
pdfFileObj=open("meetingminutes.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj=pdfReader.getPage(0)
pageObj.extractText()

#解密PDF
import PyPDF2
pdfFileObj=open("encrypted.pdf",'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.isEncrypted

pdfReader.decrypt('rosebud')
pdfReader.numPages
pageObj=pdfReader.getPage(0)
pageObj.extractText()
pdfFileObj.close()
#合并两个或多个PDF文件
import PyPDF2
pdfFileObj1=open("Collaborative Representation based Classification for Face Recognition.pdf",'rb')
pdfFileObj2=open("Robust Face Recognition via Sparse Representation（已读）.pdf",'rb')
pdfReader1=PyPDF2.PdfFileReader(pdfFileObj1)
pdfReader2=PyPDF2.PdfFileReader(pdfFileObj2)

#pdfReader1.isEncrypted
#pdfReader2.isEncrypted
pdfWriter=PyPDF2.PdfFileWriter()#新建一个PdfFileWriter对象
for pageNum in range(pdfReader1.numPages):
    pageObj=pdfReader1.getPage(pageNum)
    pdfWriter.addPage(pageObj)
for pageNum in range(pdfReader2.numPages):
    pageObj=pdfReader2.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutputFile=open("combinedFiles.pdf",'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFileObj1.close()
pdfFileObj2.close()
#CSV文件
import csv
exampleFile=open('example.csv')
exampleReader=csv.reader(exampleFile)
#exampleData=list(exampleReader)
for row in exampleReader:
    print(str(row))
    print("Row#"+str(exampleReader.line_num)+" "+str(row))
exampleFile.close()
#写csv文件
import csv
outputFile=open("ouptput.csv",'w',newline='')
outputWriter=csv.writer(outputFile)
outputWriter.writerow(["spam",'eggs','bacon','han'])
outputWriter.writerow(["hello, world!",'eggs','bacon','han'])
outputWriter.writerow([1,2,3,1343,4])
outputWriter.writerow([1,",",1343,4])
outputWriter.writerow([1,",",1343,';'])
outputWriter.writerow([1,",",'13aa',"2345"])

outputFile.close()


import os,csv
os.makedirs('headerRemoved',exist_ok=True)

for csvFilename in os.listdir():
    if not csvFilename.endswith('.csv'):#判断后缀名是否是.csv
        continue
    #读csv文件
    print("Removing header form"+csvFilename+'...')
    csvRows=[]
    csvFileObj=open(csvFilename)
    readerObj=csv.reader(csvFileObj)
    for row in readerObj:
        print(str(readerObj.line_num))
        if readerObj.line_num==1:
            continue
        csvRows.append(row)#将当前打开的文件中的第二行到尾行的所有行写入csvRows
    csvFileObj.close()
    #写csv文件
    csvFileObj=open(os.path.join("headerRemoved",csvFilename),'w',newline='')
    csvWriter=csv.writer(csvFileObj)#创建Writer对象
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
        
        
#json模块
JsonData='{"name":"zomhie","iscat":true,"miceCaught":0,"felineIQ":null}'
import json
jsonvalue=json.loads(JsonData)
jsonvalue

#time模块
import time
time.time()

def calcprod():
    product=1
    for i in range(1,100000):
        product*=i
    return product

starttime=time.time()
prod=calcprod()
endtime=time.time()
print("结果是%s位数"%(len(str(prod))))
print("花费了%s秒钟"%(endtime-starttime))

import time
for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)


str = "the length of (%s) is %d" %('runoob',len('runoob'))
print(str)
round(4.1232,2)

import datetime
datetime.datetime.now()
dt=datetime.datetime(2015,10,21,16,29,0)#返回datetime对象
dt.year,dt.month,dt.day#得到当前时刻的年月日
dt.hour,dt.minute,dt.second#得带当前时刻的时分秒

datetime.datetiem.fromtimestamp(100000)
datetime.datetime.fromtimestamp(time.time())

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

datetime.datetime.strptime("October 21, 2015","%B %d, %Y")

#多线程
import threading, time
print("Start of program")
def takeANap():
    time.sleep(5)
    print("Wake up!")
threadObj=threading.Thread(target=takeANap)
threadObj.start()
print("End of program.")

#向线程的目标函数传递参数
print("Cats",'Dogs','Frogs',sep="&")
import threading
threadObj=threading.Thread(target=print,args=["Cats",'Dogs','Frogs'],kwargs={'sep':"&"})
threadObj.start()

from PIL import ImageColor
ImageColor.getcolor("red",'RGBA')


#用Pillow操作图像
from PIL import Image
catIm=Image.open("zophie.png")
catIm.size#图片的大小
width,height=catIm.size
catIm.save("zophie.jpg")

im=Image.new("RGBA",(100,200),'PURPLE')
im.save("purpleImage.png")#保存
im2=Image.new("RGBA",(20,20))
im2.save("transparentImage.png")
#裁剪图像
cropImage=catIm.crop((335,345,565,560))
cropImage.save("cropped.png")


#复制和粘贴图像到其他图像
catIm=Image.open("zophie.png")
catCopyIm=catIm.copy()
faceIm=catIm.crop((335,345,565,560))
faceIm.size
catCopyIm.paste(faceIm,(0,0))
catCopyIm.paste(faceIm,(400,500))
catCopyIm.save("pasted.png")

#调整大小
width,height=catIm.size
quartersizeIm=catIm.resize((int(width/2),int(height/2)))
quartersizeIm.save("quartersize.png")
svelteIm=catIm.resize((width,height+200))
svelteIm.save("svelte.png")
#旋转和翻转图像
catIm.rotate(90).save("rotated90.png")
catIm.rotate(6).save("rotate6.png")
catIm.rotate(6,expand=True).save("rotate6_expanded.png")
catIm.transpose(Image.FLIP_LEFT_RIGHT).save("水平翻转.png")
catIm.transpose(Image.FLIP_TOP_BOTTOM).save("上下翻转.png")

#在图像上绘图
from PIL import Image,ImageDraw
im=Image.new("RGBA",(200,200),'white')
draw=ImageDraw.Draw(im)#从Image对象得到ImageDraw对象
draw.line([(0,0),(199,0),(199,199),(0,199),(0,0)],fill="black")
draw.rectangle((20,30,60,60),fill="blue")
draw.ellipse((120,30,160,60),fill="red")
draw.polygon(((57,87),(79,62),(45,53)),fill="brown")
for i in range(100,200,10):
    draw.line([(i,0),(200,i-100)],fill="green")

im.save("drawing.png")
#绘制文本
from PIL import Image,ImageDraw,ImageFont
import os
im=Image.new("RGBA",(200,200),"white")
draw=ImageDraw.Draw(im)
draw.text((20,150),'Hello',fill="purple")
fontsFolder="FONT_FOLDER"
arialFont=ImageFont.truetype(os.path.join(fontsFolder,'arial.ttf'),32)
draw.text((100,150),'Howdy',fill='gray',font=arialFont)
im.save("text.png")
#

import pyautogui
pyautogui.size()
width,hegiht=pyautogui.size()
for i in range(10):
    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(200,100,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)
    pyautogui.moveTo(100,200,duration=0.25)

import pyautogui
for i in range(10):
    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(0,100,duration=0.25)
    pyautogui.moveTo(-100,0,duration=0.25)
    pyautogui.moveTo(0,-100,duration=0.25)

pyautogui.position()
pyautogui.position()
######################################
import scipy.stats as st
from scipy.misc import factorial
from scipy import integrate

lmbda, k = 2, 6
X = st.poisson(2)
                    # X ~ Poisson(2)
print(X.cdf(k))
                    # P(X<=k)

def possion_pdf(x, k):
    return x**k*np.exp(-x)/factorial(k)
print(integrate.quad(possion_pdf, lmbda, np.inf, args=(k))[0])
                # 0.995466194474
                # 0.9954661944737513
                # 两者达到完美的相等
for i in a:
    print(i)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
list(enumerate(seasons, start=0))       # 下标从 1 开始

import tensorflow as tf
import numpy as np
b=tf.Variable(tf.zeros([100])) # 生成100维的向量，初始化为0
W=tf.Variable(tf.random_uniform([784,100],-1,1)) # 生成784x100的随机矩阵W
x=tf.placeholder(tf.float32,shape=(100,1)) # 输入的Placeholder
relu=tf.nn.relu(tf.matmul(W, x)+b) # ReLU(Wx+b)
with tf.Session() as sess:
    sess.run(W.initializer)
    sess.run(b.initializer) #变量初始化
    input = np.float32(np.random.randn(100,1))
    print(sess.run(relu, feed_dict={x: input}))

