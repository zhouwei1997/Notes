#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/6/23
# @file  随机分配办公室.py
# description 8名老师，3个办公室，将8位老师随机分配到3个办公室
"""
import random

"""
步骤：
1、准备数据
    1.1、8位老师  --- 列表
    1.2、3个办公室  ---列表嵌套
2、分配老师到办公室
    2.1、随机分配
3、验证是否分配成功
    打印办公室详细信息，每个办公室的人数和对应老师的名字
"""

# 准备数据
teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
offices = [[], [], []]
# 分配老师到办公室
# 取到每个老师放到办公室列表
for name in teachers:
    ''' 列表追加数据 '''
    num = random.randint(0, 2)
    offices[num].append(name)
print(offices)

# 验证是否分配成功
# 办公室编号
i = 1
for office in offices:
    # 打印办公室人数
    print(f'办公室{i}的人数{len(office)}')
    # 打印老师的名字
    for name in office:
        print(name)
    i += 1
