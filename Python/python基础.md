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

<table>
    <tr>
        <td>分类</td>
        <td>类型</td>
        <td>备注</td>
    </tr>
    <tr>
        <td rowspan="4">数字</td>
        <td>int</td>
        <td>整形</td>
    </tr>
    <tr>
    	<td>float</td>
        <td>浮点型</td>
    </tr>
     <tr>
    	<td>bool</td>
        <td>布尔型[True/False]</td>
    </tr>
     <tr>
    	<td>complex</td>
        <td>复数（不常用）</td>
    </tr>
    <tr>
    	<td>字符串</td>
        <td>str</td>
        <td>单引号，双引号和三引号内表示内容为字符串</td>
    </tr>
     <tr>
    	<td>列表</td>
        <td>list</td>
        <td>使用中括号表示[1,2,3]</td>
    </tr>
      <tr>
    	<td>元组</td>
        <td>tuple</td>
        <td>使用小括号表示(1,2,3)</td>
    </tr>
      <tr>
    	<td>字典</td>
        <td>dict</td>
        <td>使用大括号表示，可以存放key-value键值对{"a":1,"b":2}</td>
    </tr>
      <tr>
    	<td>集合</td>
        <td>set</td>
        <td>使用大括号表示，{"a","b"}</td>
    </tr>
</table>

### 类型转换

| 转换函数   | 说明                             |
| ---------- | -------------------------------- |
| int(xxx)   | 将xxx转换为整数                  |
| float(xxx) | 将xxx转换为浮点型                |
| str(xxx)   | 将xxx转换为字符串                |
| list(xxx)  | 将xxx转换为列表                  |
| tuple(xxx) | 将xxx转换为元组                  |
| dict(xxx)  | 将xxx转换为字典                  |
| set(xxx)   | 将xxx转换为集合                  |
| chr(xxx)   | 把整数[0-255]转换为对应的ASCII码 |
| ord(xxx)   | 把ASCII码转换成对应的整数[0-255] |

~~~python 
age = 25
print(type(age))
age = str(age)
print(type(age))
~~~

![image-20220607112323366](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206071123423.png)

## 输入输出

### 输入

python3中可以是用input()函数等待用户输入

~~~python
name = input("请输入您的名字：")
age = int(input("请输入您的年龄："))
print(name + ",您5年后为" + str(age + 5) + "岁了")
~~~

![image-20220607145015713](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206071450780.png)

>用单引号、双引号、三引号、str()函数转换的和input()输入的都为字符串类型

### 输出

#### 格式化输出

| 操作符 | 说明   |
| ------ | ------ |
| %s     | 字符串 |
| %d     | 整数   |
| %f     | 浮点数 |
| %%     | 输出%  |

~~~python
name = input("请输入您的名字：")
age = int(input("请输入您的年龄："))
print(name + ",您5年后为" + str(age + 5) + "岁了")
# %s或%d相当于是一个占位符，按顺序一一对应后面()里面的变量（需要类型对应）
print("%s,您5年后%d岁了" % (name, age + 5))
# {}相当于是一个占位符，按顺序一一对应后面format()里面的变量
print("{},您5年后{}岁了".format(name, age + 5))
~~~

![image-20220607171649774](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206071716873.png)
