#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2018/3/25 13:12
# @Author    : Liyuntian
# @File      : demonFactorial.py

def one(n):
    total = 1
    if n == 0:
        total = 1
    else:
        for i in range(1,n+1):
            total *= i
    return total


status = 1
while status:
    result = 0
    n = input("please input a  number >=0:")
    for i in n:
        if not i.isdigit():
            print("the number of you input is not int number.")
            exit(1)
    if int(n) < 0:
        print("the number of you input is error.")
        break
    for i in range(0,int(n)+1):
        result += one(i)
    print("0!+...+n!={0}".format(result))
