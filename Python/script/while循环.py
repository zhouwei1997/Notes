#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/8
# @file  while循环.py
# description 打印1-100的奇数
"""

# 定义初始值
i = 1
# 循环打印
while i <= 100:
    if i % 2 == 1:
        print(i, end=" ")
    i += 1
