#!/usr/bin/python
#coding=utf-8
#########################################
# File Name: sequence.py
# Author: Lu
# Created Time: 2013年12月25日 星期三 17时26分44秒
#########################################
#序列是一组有顺序的对象的集合，对象可以是基本数据类型(整型，float,真值，字符串)，也可以是另一个序列
#序列有两种：tuple(定值表或者元组) 和 list(表)
#下面这是一个元组，一旦建立，它的各个元素不可再改变
tuple_s1 = (2,1.3,'Hello tuple_S1',True)
tuple_s2 = (5,tuple_s1)

print tuple_s1,type(tuple_s1)
print tuple_s2,type(tuple_s2)

#下面这是一个list，它的各个元素是可变的
list_s1 = [False,5,'Hello list_s1',5.6]
list_s2 = [1,list_s1]
list_s3 = [list_s2,tuple_s2]

print list_s1,type(list_s1)
print list_s2,type(list_s2)
print list_s3,type(list_s3)

#序列元素的引用，序列元素的下标从0开始
print tuple_s1[2],tuple_s2[0],tuple_s2[1][3]
print list_s1[2],list_s2[0],list_s2[1][3]
print list_s3[0][1][0],list_s3[1][1]

#tuple 中的对象是不可修改的，这里会报错
#TypeError: 'tuple' object does not support item assignment
#list_s3[1][1][0] = 3
list_s3[0][1][0] = 'List_s1'
print list_s3,type(list_s3)


#范围引用，基本格式[下限:上限:步长] 不会引用到上限的内容，也就是之引用到 上限-1
print tuple_s2[0:1:1]
print list_s1[1:3:1]
#从开始到第三个对象，第三个不会被引用
print list_s1[:3]
#引用最后一个对象
print list_s1[-1]
#引用倒数第二个对象
print list_s1[-2]

#字符串也是一个tuple
tuple_s3 = 'Hello World!'
print tuple_s3[:4]

