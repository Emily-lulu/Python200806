# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:23:11 2020

@author: user
"""

import os.path
if os.path.isfile('000.txt'):
    print('exist')
    h=open('000.txt','w')
    h.write("xxxxxxxx")
    h=open('000.txt','r')
    things=h.read()
    print(things)
    h=open('000.txt','a')
    h.write("0000000")
    h=open('000.txt','r')
    things=h.read()
    print(things)
    h.close()
    
    
else:
    print('does not exist')



