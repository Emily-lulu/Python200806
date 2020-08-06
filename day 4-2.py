# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:59:06 2020

@author: user
"""
a=open('下載.jpg','rb')
b=a.read()
a.close()
a=open('下.jpg','wb')
a.write(b)
a.close()

