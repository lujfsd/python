#!/usr/bin/python
#coding=utf-8
#########################################
# File Name: object.py
# Author: Lu
# Created Time: 2013年12月27日 星期五 15时26分22秒
#########################################

#类和对象的使用练习，其中count __init__，show() ,len() 都是类的属性，同时该类的对象也都拥有这些属性
#但是其中的count是所有对象共享的一个属性，如果在某个对象中被修改，则会影响到所以的对象

class people_common:
    count = 0
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        people_common.count += 1
    def show(self):
        print "Name:%s Age:%s Sex:%s"%(self.name,self.age,self.sex)
    def len(self):
        print "All has",people_common.count,"people"

lu = people_common('Lu',24,'male')
lu.show()
wang = people_common('Wang','24','woman')
lu.show()
wang.show()

lu.len()
wang.len()
