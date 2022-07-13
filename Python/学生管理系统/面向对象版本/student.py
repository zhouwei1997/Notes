# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/13
# @file  student.py
# @description 学员文件
"""

"""
学员信息包含：姓名、性别、手机号
添加__str__方法，方便查看学员对象信息
"""


class Student(object):
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'


if __name__ == '__main__':
    testStudent = Student('zhangsan', 'male', 15027130472)
    print(testStudent)
