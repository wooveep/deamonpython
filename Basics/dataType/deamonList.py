#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/19 14:07
#@Author    : Liyuntian
#@File      : deamonList.py

l =[1,2,3,3.141592653,'a','b','c',True,{"name":"liyuntian"}]
print(l)
#append  追加一个元素
l.append('hello')
print(l)
#pop 删除一个元素
m=l.pop(3)
print("m = {0}".format(m))
l.pop()
print(l)

#remove  删除元素 value
l.remove("c")

#index（value）
print(l.index("a"))

#sort()排序
#reverse () 反序

n = [1,34,345,545,34,123,78,89,123]
print(n)
n.sort()
print(n)
n.reverse()
print(n)

# insert 插入新元素 insert（index，value）
n.insert(1,999)
print(n)


