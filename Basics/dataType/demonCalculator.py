#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/19 14:19
#@Author    : Liyuntian
#@File      : demonCalculator.py

#a+b+c+d
#a-b-c-d
def add(string):
    total = 0
    numbers = []
    numbers += string.split("+")
    total = 0
    for num in numbers:
        total += int(num.strip())
    print("{0} = {1}".format(string,total))

def reduce(string):
    result = 0
    numbers = []
    numbers += string.split("-")
    result = int(numbers[0].strip())
    numbers.pop(0)
    for num in  numbers:
         result -= int(num.strip())
    print("{0} = {1}".format(string,result))

def ride(string):
    total = 1
    numbers = []
    numbers += string.split("*")
    total = 1
    for num in numbers:
        total *= int(num.strip())
    print("{0} = {1}".format(string,total))

def division(string):
    result = 0
    numbers = []
    numbers += string.split("/")
    result = int(numbers[0].strip())
    numbers.pop(0)
    for num in numbers:
        result /= int(num.strip())
    print("{0} = {1}".format(string, result))


if __name__ == '__main__':
    print("#######################################")
    print("1: 加法")
    print("2: 减法")
    print("3: 乘法")
    print("4: 除法")
    print("#######################################")
    method = input("Please input number (1/2/3/4/):")
    if method == "1":
        string = input("请输入您的表达式：")
        add(string)
    elif method == "2":
        string = input("请输入您的表达式：")
        reduce(string)
    elif method == "3":
        string = input("请输入您的表达式：")
        ride(string)
    elif method == "4":
        string = input("请输入您的表达式：")
        division(string)
    else:
        print("the  string  of you  input  is error!")

