#!/usr/bin/python
#coding=utf-8
#########################################
# File Name: control.py
# Author: Lu
# Created Time: 2013年12月27日 星期五 13时10分09秒
#########################################

#使用缩进进行模块的划分
i = 1
if i == 1:
    print 'i = 1'
elif i > 1:
    print 'i > 1'
else:
    print 'i < 1'

#range(n) 新建一个List ,表中元素都是整数，范围0~(n-1)
# i**2 表示i的平方
for i in range(10):
    print i,i**2
   
#pyhton 中不能使用 i++ 这一类的自加或者自减操作
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print i,
    if i == 3:
        print i,'break'
        break


