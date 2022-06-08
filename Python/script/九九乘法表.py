#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/8
# @file  九九乘法表.py
# description
"""

for line in range(1, 10):
    for row in range(1, line + 1):
        print('{}*{}={}\t'.format(row, line, line * row), end='')
    print()
