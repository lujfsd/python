#!/usr/bin/python
#coding=utf-8
#########################################
# File Name: func.py
# Author: Lu
# Created Time: 2013年12月27日 星期五 13时39分46秒
#########################################

#函数的练习使用
#return 不是必须的，可以不用写，不写的时候python返回return None -表示什么都没有，类似于NULL
#也可以返回多个值，值之间用,(逗号)隔开。return a,b,c 相当于是return (a,b,c),返回的是一个tuple(元组)

def square_sum(a,b):
    c = a**2 + b**2
    return c
print square_sum(3,4)

a = 1
def change_num(a):
    a += 1
    return a
print 'a=',a,"这里是初始的a"
print 'change_num(a) return=',change_num(a),"这里a的值被+1并返回a+1,但是全局的a并没有被改变,在参数传递是只是传递了a的值"
print 'a=',a,"这里的a还是全局的a=1"

#如果要使用全局的变量a 则需要在使用的地方用global来说明
def change_num_global():
    global a 
    a += 1
    return a
print 'a=',a,"这里是初始的a"
print 'change_num_global return=',change_num_global(),"这里a的值被+1并返回a+1"
print 'a=',a,"这里的全局的a被改变"

b = [1,2,3,4]
def change_list(b):
    b[0] += 1
    return b
print 'b=',b,"这里是初始的b"
print 'change_list return=',change_list(b),\
        "这里将list b 传进函数change_list，传的是b在内存中的地址,如果函数中对b有改变，则全局list b也会被改变"
print 'b=',b,"这里是全局的list b"


def is_leapyear(year):
    if ((year%4 == 0) and (year%100 != 0) or (year%400 == 0)):
        return True
    else:
        return False

year = 2000
if is_leapyear(year) == True:
    print "This is leap year"
else:
    print "This is not leap year"


