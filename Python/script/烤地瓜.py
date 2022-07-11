# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/11
# @file  烤地瓜.py
# @description  烤地瓜
"""

"""
需求：
    1.被烤的时间和对应的状态
        0-3分钟：生的
        3-5分钟：半生不熟
        5-8分钟：熟了
        超过8分钟：烤糊了
    2.用户可以按照自己的意愿添加调料
"""


# 1、定义类：初始化属性、定义方法、显示对象信息的str
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            self.cook_state = '烤糊了'

    def add_condiments(self, condiment):
        """添加调料"""
        self.condiments.append(condiment)

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_state}，添加的调料有{self.condiments}'


# 2、创建对象并调用对应的实例方法
digua1 = SweetPotato()
print(digua1)
digua1.cook(5)
digua1.add_condiments('酱油')
print(digua1)
