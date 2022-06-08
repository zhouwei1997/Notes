#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/8
# @file  for循环.py
# description for循环实现1-100之间能被5整除，同时为奇数的和
"""

sum = 0
for i in range(1, 101):
    if i % 5 == 0 and i % 2 == 1:
        print(i)
        sum += i
print(sum)
