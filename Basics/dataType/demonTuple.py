#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/24 8:49
#@Author    : Liyuntian
#@File      : demonTuple.py

l  = list()
print(l)
t = tuple()
print(t)
#tuple 是一种特殊的list  不能进行增删改， 可以查询，统计
#tuple  单元素时，一定要有“，” 否则无法识别为tuple类型
a1 = (1)
a2 = (1,)
print(type(a1))
print(type(a2))

m = (1,2,3,4,5,6,7,7,8,2,12,4,3)
#count  统计value的个数
print(m.count(3))
#count  返回第一个value的下标
print(m.index(5))
