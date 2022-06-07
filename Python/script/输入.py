#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/7
# @file  输入.py
# description
"""

name = input("请输入您的名字：")
age = int(input("请输入您的年龄："))
print(name + ",您5年后为" + str(age + 5) + "岁了")
print("%s,您5年后%d岁了" % (name, age + 5))
print("{},您5年后{}岁了".format(name, age + 5))
