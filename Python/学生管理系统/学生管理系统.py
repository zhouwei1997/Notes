#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/4
# @file  学生管理系统.py
# description  学生管理系统
"""

'''
所有功能函数都是操作学员信息，所有存储的学员信息应该是一个全局变量，数据类型为列表
'''
info = []


# 定义功能界面函数
def info_print():
    print('请选择功能--------------------')
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员')
    print('4、查询学员')
    print('5、显示所有学员')
    print('6、退出')
    print('-' * 20)


# 添加学员
def add_info():
    """
    添加学员
    - 接受用户输入学员信息，并保存
    - 判断是否添加学员信息
        - 如果学员姓名已经存在，则报错提示
        - 如果学员姓名不存在，则准备空字典，将用户输入的数据追加到字典，在列表追加字典数据
    - 对应的if条件成立的位置调用该函数
    """
    # 接受用户输入的学员信息
    new_id = input('请输入学号：')
    new_name = input('请输入姓名：')
    new_tel = input('请输入手机号：')

    # 声明info是全局变量
    global info

    # 检测用户输入的姓名是否存在，存在则报错
    for i in info:
        if new_name == i['name']:
            print('该用户已经存在！')
            return
        # 如果用户输入的姓名不存在，则添加该学员信息
        info_dict = {}
        # 将用户输入的数据追加到字典
        info_dict['id'] = new_id
        info_dict['name'] = new_name
        info_dict['tel'] = new_tel
        # 将学员信息的字典数据追加到列表
        info.append(info_dict)
        print(info)


# 删除学员
def del_info():
    """
    1、用户输入目标学员姓名
    2、检查这个学员是否存在
        2.1、如果存在，则列表删除这个数据
        2.2、如果不存在，则提示“该用户不存在”
    3、对应的if条件成立的位置调用该函数
    :return: 
    """
    # 1、用户输入要删除学员的姓名
    del_name = input('请输入要删除的学员的姓名：')
    global info
    # 2、判断学员是否存在：如果存在，则删除。如果不存在则报错提示
    for i in info:
        if del_name == i['name']:
            info.remove(i)
            break
        else:
            print('该学员不存在！')
        print(info)


# 修改学员
def modify_info():
    """
    1、用户输入要修改的学员姓名
    2、检查这个学员是否存在
        2.1、学员存在，修改该学员的信息
        2.2、学员不存在，则报错
    3、对应的if条件成立的位置调用该函数
    :return:
    """
    modify_name = input('请输入学员姓名：')
    global info
    for i in info:
        if modify_name == i['name']:
            i['tel'] = input('请输入新的手机号：')
            break
        else:
            print('该学员不存在')
        print(info)


# 查询学员信息
def search_info():
    """
    1、用户输入需要查找学员的姓名
    2、检查这个学员是否存在
        2.1、学员存在，打印这个学员的信息
        2.2、学员不存在，报错
    3、对应的if条件成立的位置调用该函数
    :return:
    """
    search_name = input('请输入学员姓名：')
    global info
    for i in info:
        if search_name == i['name']:
            print('查找到的学员信息如下：----------')
            print(f"该学员的学号是：{i['id']}, 姓名是：{i['name']},手机号是：{i['tel']}")
            break
        else:
            print('该学员不存在。。。。')


# 显示所有学员信息
def print_all():
    print('学号\t姓名\t手机号')
    for i in info:
        print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')


# 退出系统


# 系统功能需要循环使用，直到用户输入6，才退出循环
while True:

    # 1、显示功能界面
    info_print()

    # 2、用户输入功能序号
    user_num = int(input('请输入功能序号：'))

    # 3、按照用户输入的功能序号，执行不同的功能
    if user_num == 1:
        # print('添加')
        add_info()
    elif user_num == 2:
        # print('删除')
        del_info()
    elif user_num == 3:
        # print('修改')
        modify_info()
    elif user_num == 4:
        # print('查询')
        search_info()
    elif user_num == 5:
        # print('显示所有学员')
        print_all()
    elif user_num == 6:
        exit_flag = input('确定要退出吗？yes or no')
        if exit_flag == 'yes':
            break
    else:
        print('输入有误，请重新输入')
