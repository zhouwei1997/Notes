# Python基础

[TOC]

## 变量

在内存中开辟一块空间，临时保存数据。

### 特点

- 可以反复存储数据
- 可以反复取出数据
- 可以反复更改数据

### 命名规则

- 变量名只能是字母、数字或下划线的任意组合
- 变量名的第一个字符不能是数字
- 变量名要有含义
- 变量名要区分大小写
- 关键字不能声明为变量

~~~python
"""
导入keyword模块
"""
import keyword

# 打印出所有的关键字
print(keyword.kwlist)
~~~

### 类型

Python是强类型的动态解释语言。

> 强类型：不允许不同类型相加
>
> 动态：不用显示声明数据类型，确定一个变量的类型是在第一次给他赋值的时候，也就是说：变量的类型是有值决定的

~~~python
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
~~~

![image-20220607101510831](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206071015917.png)
