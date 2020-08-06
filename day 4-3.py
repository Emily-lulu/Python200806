# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:38:45 2020

@author: user
"""
import os.path
d={}
x=0
x=int(0)
y=0
y=int(0)
def buildmenu():
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢')
    print('4.離開')
    a=input('請選擇一項服務')
    a=int(a)
    return(a)
    
if not os.path.isfile('score.txt'):
    fo=open('score.txt','w')
    print("new file")
else:
    fo =open('score.txt','r')
    print('old file')
for row in fo.readlines():
    data=row.split(';')
    
    key=data[0]
    value=data[1]
    d[key]=value
print(d)
fo.close   
while x==0:
    if buildmenu()==1:
        while y==0:
            voc=input('請輸入名字(要退出請按0)')
            if voc=='0':
                break
            if voc not in d:
                m=input('請輸入分數')
                d[voc]=m
            if voc in d:
                print('已登記')
    if buildmenu()==2:
        print(d)
    if buildmenu()==3:
        voc=input('請輸入名字')
        for key in d.keys():
            if key==voc:
                m=d[voc]
                print(m)
                break
            if key not in d:
                print('查無此人')
    if buildmenu()==4:
        break