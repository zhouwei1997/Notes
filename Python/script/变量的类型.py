#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/7
# @file  变量的类型.py.py
# description
"""

# str类型
name = "zhangsan"
# 25没有加引号，则是int类型，加了引号则是str类型
age = 25
# float类型
height = 1.8
# bool类型
marry = True

"""
通过type()内置函数得知变量的类型
"""
print(type(name))
print(type(age))
print(type(height))
print(type(marry))
