# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/13
# @file  managerSystem.py
# @description 管理系统文件
"""
from Python.学生管理系统.面向对象版本.student import Student

'''
- 存储数据的位置：文件(student.data)
    - 加载文件数据
    - 修改数据后保存到文件
- 存储数据的形式：列表存储学员对象
- 系统功能：
    - 添加学员
    - 删除学员
    - 修改学员
    - 查询学员信息
    - 显示所有学员信息
    - 保存学员信息
'''


class StudentManager(object):
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 程序入口函数，启动程序后执行的函数
    def run(self):
        # 1、加载学员信息
        self.load_student()
        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入功能序号
            menu_num = int(input('请输入您需要的功能序号：'))
            # 根据用户输入的功能序号执行不同的功能
            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()
            elif menu_num == 4:
                # 查询学员信息
                self.search_student()
            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 7:
                # 退出系统
                break

    def load_student(self):
        try:
            file = open('student.data', 'r')
        except:
            file = open('student.data', 'w')
        else:
            data = file.read()
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]
        finally:
            file.close()

    def save_student(self):
        """
        将修改后的学员数据保存到存储数据的文件中
        步骤：
            1、打开文件
            2、文件写入数据
            3、关闭文件
        :return:
        """
        file = open('student.data', 'w')
        '''
        文件写入学员数据
        文件写入的数据不能是学员对象的内存地址，需要把学员数据转换成列表字典数据再做存储
        '''
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        # 文件内数据要求为字符串类型，需要先转移数据类型为字符串才能写入数据
        file.write(str(new_list))
        file.close()

    def show_student(self):
        print('姓名\t性别\t手机号')
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    def search_student(self):
        search_name = input('请输入要查询的学员姓名：')
        for i in self.student_list:
            if i.name == search_name:
                print(f'姓名：{i.name},性别：{i.gender},手机号：{i.tel}')
                break
            else:
                print(f'系统查无此人！！！')

    def modify_student(self):
        """
        用户输入目标学员姓名，如果用户存在则修改该学员信息
        步骤：
            1、用户输入目标学员姓名
            2、遍历学员数据列表，如果用户输入的学员姓名存在则修改学员的姓名、性别、手机号数据。否则提示该学员不存在
        :return:
        """
        modify_name = input('请输入要修改的学员的姓名：')
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员手机号：')
                print(f'修改该学员信息成功，姓名：{i.name},性别：{i.gender},手机号：{i.tel}')
                break
            else:
                print(f'系统查无此人！！！')

    def del_student(self):
        """
        用户输入目标学员姓名，如果学员存在则删除该学员
        步骤：
            1、用户输入目标学员姓名
            2、遍历学员数据列表，如果用户输入的学员姓名存在，则删除，否则提示该学员不存在
        :return:
        """
        del_name = input('请输入要删除的学员姓名：')
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
            else:
                print(f'系统查无此人！！！')

        print(self.student_list)

    def add_student(self):
        """
        用户输入学员姓名、性别、手机号，将学员添加到系统
        步骤：
            1、用户输入姓名、性别、手机号
            2、创建该学员对象
            3、将该学员对象添加到列表
        :return:
        """
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号：')
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(self.student_list)
        print(student)

    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1:添加学员')
        print('2:删除学员')
        print('3:修改学员信息')
        print('4:查询学员信息')
        print('5:显示所有学员信息')
        print('6:保存学员信息')
        print('7:退出系统')
