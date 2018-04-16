#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time      : 2018/3/25 13:00
#@Author    : Liyuntian
#@File      : demonOperation.py

# ABCD*9=DCBA    A=? B=? C=? D=?

for A  in  range(1,10):
    for B  in range(0,10):
        for C in range(0,10):
            for D in range(1,10):
                start = 1000 * A + 100 * B + 10 * C + D
                end = 1000 * D + 100 * C + 10 * B + A
                if start * 9 == end:
                    print("A = {0}".format(A))
                    print("B = {0}".format(B))
                    print("C = {0}".format(C))
                    print("D = {0}".format(D))
                    print("{0} * 9 = {1}".format(start,end))