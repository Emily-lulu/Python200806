# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:40:22 2020

@author: user
"""
import time
import turtle


while time.strftime("%S",time.localtime())<='60':
     print(time.strftime("%S",time.localtime()))
    
     if time.strftime("%S",time.localtime())=='01':
         green=turtle.Turtle()
         green.color('green')
         green.shape('turtle') 
         print('please pass')
     if time.strftime("%S",time.localtime())=='31':
         green=turtle.Turtle()
         green.color('red')
         green.shape('turtle') 
         print('please wait')
         
        





