#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/25 13:45
#@Author    : Liyuntian
#@File      : demonCountnums.py

status =1
while status:
    strings = input("please input a string('quit' will exit):")
    if strings == "quit":
        exit(1)
    digit = pha = space = other = 0
    for i in strings:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            pha += 1
        elif i.isspace():
            space += 1
        else:
            other += 1

    print("数字有{0}个，字母有{1}个，空格有{2}个，其他有{3}个".format(digit,pha,space,other))
