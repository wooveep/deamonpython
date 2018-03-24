#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/24 9:05
#@Author    : Liyuntian
#@File      : demonDict.py

#字典的定义
d1 = dict(name = "liyuntian",age = 23 )
d2 = {"id": 1001128 , "name":"liyuntian"}
d3 = dict([("ip","192.168.1.254"),("netmask","255.255.255.0")])
print(d1)
print(d2)
print(d3)

#方法
#get(key)  根据key获取vlue
print(d1.get("name"))
print(d1.setdefault("name"))
print(d1.setdefault("address"))


#key

print(d1.keys())

#python2 中 有items 和 iteritems

for x,y in d3.items():
    print("key = {0},value = {1}".format(x,y))



#update   就和list中加相似
m = dict()
n = dict(name = "zqq" , age = 18)
d1.update(n)
print(d1)


#pop  删除key 所对应的元素 返回key对应的返回值
keyDelete = d3.pop("ip")
print(keyDelete)
print(d3)