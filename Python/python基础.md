# Python基础

[TOC]

## 输出

作用：程序输出内容给用户

### 格式化输出

#### 格式化符号

| 格式化符号 |         转换         |
| :--------: | :------------------: |
|     %s     |        字符串        |
|     %d     |  有符号的十进制整数  |
|     %f     |        浮点数        |
|     %c     |         字符         |
|     %u     |   无符号十进制整数   |
|     %o     |      八进制整数      |
|     %x     | 十六进制整数(小写ox) |
|     %X     | 十六进制整数(大写OX) |
|     %e     |   科学计数法('e')    |
|     %E     |   科学计数法('E')    |
|     %g     |     %f和%e的简写     |
|     %G     |     %f和%E的简写     |

> 技巧：
>
>- %06d，表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出
>- %.2f，表示小数点后显示小数位数

~~~python
age = 18
name = 'Tom'
weight = 75.5
stu_id = 1001
# 1、今年我的年龄是x岁
print('今年我的年龄是%d岁' % age)

# 2、我的名字是x
print('我的名字是%s' % name)

# 3、我的体重是x公斤
print('我的体重是%0.2f公斤' % weight)

# 4、我的学号是x
print('我的学号是%d' % stu_id)

# 5、我的名字是x,今年x岁
print('我的名字是%s,今年%d岁' % (name, age))

# 6、我的名字是x,今年x岁,体重是x公斤,学号是x
print('我的名字是%s,今年%d岁,体重是%.2f公斤,学号是%06d' % (name, age, weight, stu_id))
~~~

![image-20220620204600385](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206202046516.png)

### 结束符

~~~python
print('输入的内容', end="\n")
~~~

> 在python中，print()函数自带`end="\n"`这个换行符，所以导致每两个print直接会换行展示

## 输入

~~~python
input("提示信息")
~~~

### 特点

- 当程序执行到`input`，等待用户输入，输入完成后才会向下继续执行
- 在python中，`input`接收用户输入后，一般存储到变量，方便使用
- 在python中，`input`会把接收到的任意用户输入的数据都当成字符串处理

~~~python
password = input("请输入您的密码：")
print(f'您输入的密码是{password}')
print(f'password的类型是{type(password)}')
~~~

![image-20220620213914983](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206202139063.png)

## 转换数据类型

### 转换数据类型的函数

|         函数          |                         说明                         |
| :-------------------: | :--------------------------------------------------: |
|    int(x[,base ])     |                  将x转换为一个整数                   |
|       float(x)        |                 将x转换为一个浮点数                  |
| complex(real [,imag]) |         创建一个复数，real为实部，imag为虚部         |
|        str(x)         |                 将对象x转换为字符串                  |
|        repr(x)        |              将对象x转换为表达式字符串               |
|       eval(str)       | 用于计算在字符串中的有效python表达式，并返回一个对象 |
|       tuple(s)        |                将序列s转换为一个元组                 |
|        list(s)        |                将序列s转换为一个列表                 |
|        chr(x)         |           将一个整数转换为一个Unicode字符            |
|        ord(x)         |          将一个字符串转换为它的ASCII整数值           |
|        hex(x)         |         将一个整数转换为一个十六进制的字符串         |

## 运算符

### 算数运算符

| 运算符 | 描述 | 实例 | | :----: | :--: | :--: | | + | 加 | 1 + 1 输出结果为2 | | - | 减 | 1 - 1 输出结果为0 | | * | 乘 | 2 * 2 输出结果为4 | |
/ | 除 | 10 / 5 输出结果为2 | | // | 整除 | 9 // 4 输出结果为2 | | % | 取余 | 9 % 4 输出结果为1 | | **   | 指数 | 2 ** 4 输出结果为16 | | ()   |
小括号 | 小括号用来提高运算优先级，即(1 + 2) * 3 输出结果为9 |

> - 混合运算优先级顺序：() 高于 ** 高于 * / // % 高于 + -

### 赋值运算符

| 运算符 | 描述 | 实例 | |:---:| :--: | :--: | | = | 赋值 | 将 = 右侧的结果赋值给等号左侧的变量 |

~~~python
# 单个变量赋值
num = 1
print(num)

# 多个变量赋值
num1, float1, str1 = 10, 0.5, 'hello world'
print(num1)
print(float1)
print(str1)

# 多变量赋相同值
a = b = 10
print(a)
print(b)
~~~

### 复合赋值运算符

| 运算符 | 描述 | 实例 |
| ------ | ---- | ---- |
| +=   | 加法赋值运算符 | c += a 等价于 c=c+a |
| -=   | 减法赋值运算符 | c -= a 等价于 c=c-a |
| *=   | 乘法赋值运算符 | c *= a 等价于 c = c * a |
| /=   | 除法赋值运算符   | c /= a 等价于 c = c / a |
| //= | 整除赋值运算符 | c //= a 等价于 c = c // a |
| %= | 取余赋值运算符 | c %= a 等价于 c = c % a |
| **= | 幂赋值运算符 | c ** = a 等价于 c = c ** a |

### 比较运算符

| 运算符 | 描述                                              | 实例                                                    |
|----|-------------------------------------------------|-------------------------------------------------------|
| == | 判断相等。如果两个操作数的结果相同，则条件结果为真(True)，否则条件结果为假(False) | 如：a=3,b=3,则(a == b)为True                              |
| != | 不等于。如果两个操作数的结果不相同，则条件结果为真(True)，否则条件结果为假(False) | 如：a=1,b=3,则(a != b)为True                              |
| >  | 运算符左侧操作数结果是否大于右侧操作数结果，如果大于，则条件为真，否则为假           | 如：a=7,b=3,则(a > b)为True                               |
| <  | 运算符左侧操作数结果是否小于右侧操作数结果，如果小于，则条件为真，否则为假           | 如：a=7,b=3,则(a < b)为True                               |
| > = | 运算符左侧操作数结果是否大于等于右侧操作数结果，如果大于等于，则条件为真，否则为假       | 如：a=7,b=3,则(a < b)为False。如：a = 3,b = 3,则(a >= b)为True |
| <= | 运算符左侧操作数结果是否小于等于右侧操作数结果，如果小于等于，则条件为真，否则为假       | 如：a = 3,b = 3,则(a <= b)为True                          |

### 逻辑运算符

| 运算符 | 逻辑表达式 | 描述 | 实例 |
| ------ | ---------- | ---- | ---- |
| and  | x and y | 布尔"与"：如果 x 为 False，x and y返回 False，否则它返回y的值 | True and False,则返回False。 |
| or   | x or y | 布尔"或"：如果 x 为 True，x or y返回 True，否则它返回y的值 | False or True,则返回True。 |
| not  | not x | 布尔"非"：如果 x 为 True，x not y返回False，如果 x 为 False，它返回 True | not True,返回False，not False，返回 True |

~~~python
a = 1
b = 2
c = 3
print((a < b) and (b < c))  # True
print((a > b) and (b < c))  # False
print((a > b) or (b < c))  # True
print(not (a > b))  # True
~~~

## if条件语句

### if语法

~~~python
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ......
~~~

### if...else...语句

~~~python
if 条件:
    条件成立执行的代码1
    条件成立执行的代码2
    ……
    else:
    条件不成立执行的代码1
    条件不成立执行的代码2
    ……
~~~

~~~python
age = int(input("请输入您的年龄："))
if age > 18:
    print(f'您的年龄是{age},已经成年，可以上网')
else:
    print(f'您的年龄是{age},未成年，请自行回家写作业')
print("系统关闭")
~~~

### 多重判断

~~~python
if 条件1:
    条件1成立执行的代码1
    条件1成立执行的代码2
    ……
    elif 条件2:
    条件2成立执行的代码1
    条件2成立执行的代码2
    ……
    ……
    else:
    条件不成立执行的代码1
~~~

> 多重判断也可以和else配合使用，一般else放到整个if语句的最后，表示以上条件都不成立的时候执行的代码

## 三目运算符

~~~python
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
~~~

~~~python
a = 1
b = 2
c = a if a > b else b
print(c)
~~~

## 循环

### for循环

~~~python
for 临时变量 in 序列:
    重复执行代码1
    重复执行代码2
    ……
~~~

~~~python
str1 = 'itheima'
for i in str1:
    print(i)
~~~

#### for循环嵌套

### while循环

~~~python
while 条件:
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    ……
~~~

~~~python
# 计算1-100的累加和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
~~~

![image-20220621103751726](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211037854.png)

~~~python
# 1-100的偶数和
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)
~~~

![image-20220621104427486](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211044567.png)

#### while循环嵌套

~~~python
while 条件1:
    条件1成立执行的代码
    ……
    while 条件2:
        条件2成立执行的代码
        ……
~~~

~~~python
j = 1
while j <= 9:
    # 重复打印9行表达式
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i * j}', end='\t')
        i += 1
    # 一行的表达式结束
    print()
    j += 1
~~~

![image-20220621144733835](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211447945.png)

### break和continue

break和continue是循环中满足一定条件退出循环的两种方式

break控制循环流程即终止此循环

continue控制循环流程即退出当前一次循环继而执行下一场循环

#### break

当某些条件成立时，退出整个循环

~~~python
# 循环吃5个苹果，吃完第3个吃饱了，第4和第5不吃了 --- 循环不执行了
i = 1
while i <= 5:
    if i == 4:
        print(f'吃了{i}个苹果，吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
print("不吃了")
~~~

![image-20220621105542567](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211055664.png)

#### continue

当某些条件成立，退出当前循环，执行下一次循环

~~~python
# 吃到第3个吃出了一个虫子，第三个不吃了，没吃饱，继续吃第四个和第五个苹果
# 只有第三个苹果不吃

i = 1
while i <= 5:
    if i == 3:
        print("吃出一个大虫子，这个苹果不吃了")
        # 如果使用continue，在continue之前一定要修改计数器，否则进入死循环
        i += 1
        continue
    print("吃了第{}个苹果".format(i))
    i += 1
~~~

> 如果使用continue，在continue之前一定要修改计数器，否则进入死循环

![image-20220621111122760](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211111853.png)

### 循环中的else

else下方缩进的代码指的是当循环正常结束之后要执行的代码

#### while...else

~~~python 
while 条件:
    条件成立执行的代码
else:
    循环正常结束之后要执行的代码
~~~

#### for...else 

~~~python
for 临时变量 in 序列:
    重复执行代码
else:
    循环正常结束之后要执行的代码
~~~

## 
