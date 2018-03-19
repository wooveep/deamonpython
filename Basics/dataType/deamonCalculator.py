#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/19 14:19
#@Author    : Liyuntian
#@File      : deamonCalculator.py

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
    numbers += string.split("-").strip()
    result = int(numbers[0])
    numbers.pop(0)
    for num in  numbers:
         result -= num
    print("{0} = {1}".format(string,result))

def ride(string):
    total = 0
    numbers = []
    numbers += string.split("*")
    total = 0
    for num in numbers:
        total *= int(num.strip())
    print("{0} = {1}".format(string,total))

def division(string):
    result = 0
    numbers = []
    numbers += string.split("/").strip()
    result = int(numbers[0])
    numbers.pop(0)
    for num in numbers:
        result /= num
    print("{0} = {1}".format(string, result))


if __name__ == '__main__':
    print("#######################################")
    