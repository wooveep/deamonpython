#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2018/3/24 9:20
# @Author    : Liyuntian
# @File      : demonMethod.py


# help() ctrl + zuo
s = "ahdsflanwofnaovndsa"

# help(s.split)
# result = s.startswith("ah")
# print(result)
#
# # dir()
#
# print(dir(s))
#
# # type 查看属于什么类型
# a = "123"
# print(type(a))
#

# len(s)  统计字符串长度
print(len(s))

# isinstance()  返回值是一个 bool 类型
print(isinstance(s,str))
print(isinstance(s,dict))


# print 2  print 支持 print s  就是不回车
# python 3  print 包装为一个函数  print（s,end""） 这个是不回车
#
#
# python 2 存在  xrange（） range（） d.iteritems() d.items()

#python3 中 只存在 range（） items（）

# for i in range(1,10):
#     pass

# python2 input 必须为整数  raw_input 自动把输入改为字符串类型
# python3 中 输入 自动都转化为字符串类型



