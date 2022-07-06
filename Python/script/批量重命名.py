#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/6
# @file  批量重命名.py
# description 批量修改文件名，既可添加指定字符串，又能删除指定字符串
"""
import os

"""
步骤：
    1、设置添加删除字符串的标识
    2、获取指定目录的所有文件
    3、将原有文件名添加/删除指定字符串，构成新名称
    4、os.rename()重命名
"""

# 设置重命名标识：1 ---> 添加指定字符，2 ---> 删除指定字符
flag = 1
# 获取指定目录
dir_name = './'

# 获取指定目录的文件列表
file_list = os.listdir(dir_name)

# 遍历文件列表内的文件
for name in file_list:
    # 添加指定字符
    if flag == 1:
        new_name = 'Python-' + name
    # 删除指定字符
    elif flag == 2:
        num = len('Python-')
        new_name = name[num:]
    # 打印新文件名
    print(new_name)

    # 重命名
    os.rename(dir_name, dir_name + new_name)
