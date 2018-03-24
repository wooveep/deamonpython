#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2018/3/19 13:47
# @Author    : Liyuntian
# @File      : demon2.py


# 整型 int
a = 10
print(a)
# print a python2 支持

# bool    True  false
#
#

# float
a = 3.141592653
m = round(a,4)
print(m)

# 字符串str
string  = "   abcdaefhahiajasgaa     "
print(string)

#find
print(string[0])
result = string.find('def')
print(result)
#replace 替换
print(string.replace('a',"AAA"))
#split() 分隔符
print(string.split('a'))
#join  可迭代对象  一般是一个list
newList = string.strip().split('a')
print(newList)
print("  ###  ".join(newList))
# strip 去除字符串前后空格

print("my string is : %s" %string)
print("my string is : {0}".format(string))


