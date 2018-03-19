#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2018/3/19 12:31
# @Author    : Liyuntian
# @File      : demon1.py
import sys

name = input("please input your name: ")
print("hello {0}".format(name))

print(sys.argv[1])

# python2 input 输入的是整型   raw_input    输入的是字符串
# python3 只有input   输入的是字符串
