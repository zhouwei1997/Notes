# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/11
# @file  搬家具.py
# @description 将小于房子剩余面积的家具摆放到房子中
"""

"""
需求涉及两个事物：房子和家具

房子类
    实例属性：
        房子地理位置
        房子占地面积
        房子剩余面积
        房子内家具列表
    实例方法：
        容纳家具
    显示房屋信息

家具类
    家具名称
    家具占地面积
"""


class Furniture():
    def __init__(self, name, area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area


class Home():
    def __init__(self, address, area):
        # 地理位置
        self.address = address
        # 房屋面积
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具列表
        self.furniture = []

    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area > item.area:
            self.furniture.append(item.name)
            # 家具搬入后，房屋剩余面积 = 之前剩余面积 - 该家具面积
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')

    def __str__(self):
        return f'房子坐落于{self.address},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'


bed = Furniture('双人床', 6)
sofa = Furniture('沙发', 10)

jia1 = Home('北京', 1000)
jia1.add_furniture(bed)
jia1.add_furniture(sofa)
print(jia1)
