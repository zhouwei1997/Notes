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

## 字符串

### 切片

~~~python
序列[开始位置下标:结束位置下标:步长]
~~~

> 1、不包含结束位置下标对应的数据，正负整数均可
>
> 2、步长是选取间隔，正负整数均可，默认步长为1

~~~python
name = "abcdefghijklmn"

print(name[2:5:1])  # cde
print(name[2:5])  # cde
print(name[:5])  # abcde
print(name[2:])  # cdefghijklmn
print(name[:])  # abcdefghijklmn

# 负数测试
print(name[::-1])  # nmlkjihgfedcba
# 下标-1表示最后一个数据，依次向前类推
print(name[-4:-1])  # klm
print(name[-4:-1:-1])
~~~

> 1、不写开始，默认从0开始选取
>
> 2、不写结束，表示选取到最后
>
> 3、如果不写开始和结束，表示选取所有
>
> 4、如果步长是负数，表示倒序选取
>
> 5、下标-1表示最后一个数据，依次向前类推

![image-20220621161610525](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211616626.png)

### 常用操作方法

#### 查找

字符串的查找方法即是查找子串在字符串中的位置或出现的次数

- find()：检测某个子串是否包含在这个字符串中，如果在返回这个子串开始位置的下标，否则返回-1

    ~~~
    字符串序列.find(子串，开始位置下标，结束位置下标)
    ~~~

  > 开始和结束位置下标可以省略，表示在整个字符串序列中查找

    ~~~python
    mystr = "hello world and itcast and itheima and python"
    
    print(mystr.find('and')) # 12
    print(mystr.find('and', 15, 30)) # 23
    print(mystr.find('ands')) # -1
    ~~~

  ![image-20220621162521990](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206211625086.png)

- index()：检测某个子串中是否包含在这个字符串中，如果在返回这个子串开始的位置下标，否则报异常

    ~~~
    字符串序列.index(子串，开始位置下标，结束位置下标)
    ~~~

  > 开始和结束位置下标可以省略，表示在整个字符串序列中查找

  ~~~python
  mystr = "hello world and itcast and itheima and python"
  
  print(mystr.index('and'))  # 12
  print(mystr.index('and', 15, 30))  # 23
  print(mystr.index('ands'))  # 报错
  ~~~

  ![image-20220621211320967](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212113092.png)

- rfind()：和find()功能相同，但查找方向从右侧开始

- rindex()：和index()功能相同，但查找方向从右侧开始

- count()：返回某个子串在字符串中出现的次数

    ~~~
    字符串序列.count(子串，开始位置下标，结束位置下标)
    ~~~

  > 开始和结束位置下标可以省略，表示在整个字符串序列中查找

    ~~~python
    mystr = "hello world and itcast and itheima and python"
    
    print(mystr.count('and'))  # 3
    print(mystr.count('and', 15, 30))  # 1
    print(mystr.count('ands'))  # 0
    ~~~

​    ![image-20220621211743635](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212117710.png)

#### 修改

- replace()：替换

  调用replace()函数后，原有字符串的数据并没有做到修改，修改后的数据是replace()函数的返回值。

    ~~~
    字符串序列.replace(旧子串，新子串，替换次数)
    ~~~

  > 替换次数如果超出子串出现次数，则表示替换所有的子串

    ~~~python
    mystr = "hello world and itcast and itheima and python"
    
    # 结果：hello world he itcast he itheima he python
    print(mystr.replace('and', 'he'))
    # 结果：hello world he itcast he itheima he python
    print(mystr.replace('and', 'he', 10))
    # 结果：hello world and itcast and itheima and python
    print(mystr)
    ~~~

  ![image-20220621212143736](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212121805.png)

- split()：按照指定字符分割字符串

    ~~~
    字符串序列.split(分割字符，num)
    ~~~

  > num表示的是分割字符出现的次数，即将来返回数据个数为num+1个

    ~~~python
    mystr = "hello world and itcast and itheima and python"
    
    # 结果：['hello world ', ' itcast ', ' itheima ', ' python']
    print(mystr.split('and'))
    # 结果：['hello world ', ' itcast ', ' itheima and python']
    print(mystr.split('and', 2))
    # 结果：['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'python']
    print(mystr.split(' '))
    # 结果：['hello', 'world', 'and itcast and itheima and python']
    print(mystr.split(' ', 2))
    ~~~

  ![image-20220621212535720](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212125793.png)

- join()：用一个字符或子串合并字符串，即将多个字符串合并为一个新的字符串

    ~~~
    字符或子串.join(多字符串组成的序列)
    ~~~

    ~~~python
    list1 = ['chuan', 'zhi', 'bo', 'ke']
    t1 = ['aa', 'bb', 'cc', 'ddd']
    # 结果：chuan_zhi_bo_ke
    print('_'.join(list1))
    ~~~

- capitalize()：将字符串第一个字符转换成大写

    ~~~python
    mystr = "hello world and itcast and itheima and python"
    
    # 结果为：Hello world and itcast and itheima and python
    print(mystr.capitalize())
    ~~~

  ![image-20220621213722315](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212137379.png)

- title()：将字符串每个单词首字母转换成大写

    ~~~Python
    mystr = "hello world and itcast and itheima and python"
    
    # 结果为：Hello World And Itcast And Itheima And Python
    print(mystr.title())
    ~~~

- lower()：将字符串中大写转换成小写

    ~~~python
    mystr = "hello world and itcast and itheima and PYTHON"
    
    # 结果为：hello world and itcast and itheima and python
    print(mystr.lower())
    ~~~

  ![image-20220621213901410](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212139475.png)

- upper()：将字符串中小写转换成大写

    ~~~python
    mystr = "hello world and itcast and itheima and PYTHON"
    
    # 结果为：HELLO WORLD AND ITCAST AND ITHEIMA AND PYTHON
    print(mystr.upper())
    ~~~

  ![image-20220621214050940](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212140002.png)

- lstrip()：删除字符串左侧空白字符

    ~~~python
    mystr = "     hello world and itcast and itheima and PYTHON"
    
    # 结果为：hello world and itcast and itheima and PYTHON
    print(mystr.lstrip())
    ~~~

- rstrip()：删除字符串右侧空白字符

    ~~~python
    mystr = "     hello world and itcast and itheima and PYTHON     "
    
    # 结果为：     hello world and itcast and itheima and PYTHON
    print(mystr.rstrip())
    ~~~

- strip()：删除字符串两侧空白字符

    ~~~Python
    mystr = "     hello world and itcast and itheima and PYTHON     "
    
    # 结果为：hello world and itcast and itheima and PYTHON
    print(mystr.strip())
    ~~~

- ljust()：返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串

    ~~~
    字符串序列.ljust(长度,填充字符)
    ~~~

  ![image-20220621214628757](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212146822.png)

- rjust()：返回一个原字符串右对齐，并使用指定字符（默认空格）填充至对应长度的新字符串

- center()：返回一个原字符串居中对齐，并使用指定字符（默认空格）填充至对应长度的新字符串

- startswitch()：检查字符串是否以指定子串开头，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查

    ~~~
    字符串序列.startswitch(子串,开始位置下标,结束位置下标)
    ~~~

    ~~~python
    mystr = "hello world and itcast and itheima and Python"
    
    print(mystr.startswith('hello')) # True
    print(mystr.startswith('hello', 5, 10)) # False
    ~~~

  ![image-20220621215156532](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212151616.png)

- endswitch()：检查字符串是否以指定子串结尾，是则返回True，否则返回False。如果设置开始和结束位置下标，则在指定范围内检查

     ~~~
     字符串序列.endswitch(子串,开始位置下标,结束位置下标)
     ~~~

    ```python
    mystr = "hello world and itcast and itheima and Python"
    
    print(mystr.endswith('Python'))  # True
    print(mystr.endswith('Python', 5, 10))  # False
    ```

​        ![image-20220621215414011](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212154099.png)

- isalpha()：如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False

    ~~~python
    mystr1 = "hello"
    mystr2 = "hello123456"
    
    print(mystr1.isalpha())  # True
    print(mystr2.isalpha())  # False
    ~~~

- isdigit()：如果字符串只包含数字则返回True，否则返回False

- isalnum()：如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False

- isspace()：如果字符串中只包含空白则返回True，否则返回False

## 列表

### 格式

~~~
[数据1,数据2,数据3,……]
~~~

列表可以一次性存储多个数据，且可以为不同的数据类型

### 常用操作

- index()：返回指定数据所在位置的下标

    - 如果查找的数据不存在则报错

- count()：统计指定数据在当前列表中出现的次数

- len()：访问列表长度，即列表中数据的个数

- in：判断指定数据在某个列表序列，如果存在则返回True，否则返回False

    ~~~python
    name_list = ['Tom', "Lily", "Rose"]
    
    print('Lily' in name_list)  # True
    print('Lilys' in name_list)  # False
    ~~~

  ![image-20220621220951869](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212209250.png)

- not in：判断指定数据不在某个列表序列，如果不存在则返回True，否则返回False

    ~~~python
    name_list = ['Tom', "Lily", "Rose"]
    
    print('Lily' not in name_list)  # False
    print('Lilys' not in name_list)  # True
    ~~~

  ![image-20220621221044697](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212210005.png)

- append()：列表结尾追加数据

    ~~~
    列表序列.append(数据)
    ~~~

    ~~~python
    name_list = ['Tom', "Lily", "Rose"]
    name_list.append('xiaoming')
    # 返回结果：['Tom', 'Lily', 'Rose', 'xiaoming']
    print(name_list)
    ~~~

  ![image-20220621221519489](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212215745.png)

- extend()：列表结尾追加数据，如果数据是一个序列，则将这个序列的数据逐一添加到列表

    ~~~
    列表序列.extend(数据)
    ~~~

    ~~~python 
    # 单个数据
    name_list = ['Tom', "Lily", "Rose"]
    name_list.extend('xiaoming')
    # 返回结果：['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
    print(name_list
    ~~~

  ![image-20220621221800484](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212218761.png)

    ~~~python 
    # 序列数据
    name_list = ['Tom', "Lily", "Rose"]
    name_list.extend(['xiaoming', 'xiaohong'])
    # 返回结果：['Tom', 'Lily', 'Rose', 'xiaoming', 'xiaohong']
    print(name_list)
    ~~~

  ![image-20220621222030323](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206212220582.png)

- insert()：

    ~~~
    列表序列.insert(位置下标，数据)
    ~~~

    ~~~python
    name_list = ['Tom', "Lily", "Rose"]
    name_list.insert(1, 'xioaming')
    # 返回结果：['Tom', 'xioaming', 'Lily', 'Rose']
    print(name_list)
    ~~~

  ![image-20220623153435069](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231534180.png)

- del()：删除列表

    ~~~
    del 目标
    ~~~

    ~~~python
    # 删除列表
    name_list = ['Tom', "Lily", "Rose"]
    del name_list
    
    print(name_list)
    ~~~

  ![image-20220623153720274](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231537361.png)

    ~~~python
    name_list = ['Tom', "Lily", "Rose"]
    del name_list[0]
    
    print(name_list)
    ~~~

  ![image-20220623153841175](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231538268.png)

- pop()：删除指定下标的数据（默认为最后一个），并返回该数据

    - 无论是按照下标还是删除最后一个，pop函数都会返回这个被删除的数据

    ~~~python 
    name_list = ['Tom', "Lily", "Rose"]
    del_name = name_list.pop()
    print(del_name)
    print(name_list)
    ~~~

  ![image-20220623154242400](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231542477.png)

- remove()

    ~~~python
    name_list = ['Tom', "Lily", "Rose"]
    del_name = name_list.remove("Lily")
    print(del_name)
    print(name_list)
    ~~~

  ![image-20220623154450855](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231544926.png)

- clear()：清空列表

  ~~~Python
  name_list = ['Tom', "Lily", "Rose"]
  name_list.clear()
  
  print(name_list)
  ~~~

  ![image-20220623154618091](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231546173.png)

- reverse()：逆序

    ~~~python 
    num_list = [1, 5, 6, 8, 9]
    num_list.reverse()
    print(num_list)
    ~~~

  ![image-20220623161626993](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231616067.png)

- sort()：排序

    ~~~
    列表序列.sort(key=None,reverse=False)
    ~~~

  > reverse表示排序规则，reverse=True：降序 everse=False：升序（默认）

## 元组

一个元组可以存储多个数据，元组内的数据是不能修改的

定义元组使用小括号，且用逗号隔开各个数据，数据可以是不同的数据类型

~~~python
# 多个数据元组
t1 = (10, 20, 30)
# 单个数据元组
t2 = (10,)
~~~

> 如果定义的元组只有一个数据，那么整个数据后面最好添加逗号，否则数据类型为唯一数据的这个数据类型

## 字典

字典里面的数据是以键值对形式出现，字典数据和数据顺序没有关系，即字典不支持下标，后期无论数据如何变化，只需要按照对应的键的名字查找数据即可。

### 特点

- 符号为大括号
- 数据为键值对形式出现
- 各个键值对之间用逗号隔开

### 语法

~~~Python
# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 空字典
dict2 = {}
dict3 = dict()
~~~

### 新增

写法：字段序列[key]=值

> 如果key存在则修改这个key对应的值
>
> 如果key不存在则新增此键值对

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['name'] = 'Rose'
# {'name': 'Rose', 'age': 20, 'gender': '男'}
print(dict1)

dict1['id'] = 110
# {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}
print(dict1)
~~~

![image-20220623173019218](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206231730317.png)

### 修改

写法：字段序列[key]=值

> 如果key存在则修改这个key对应的值，如果key不存在则新增此键值对

### 查找

#### key值查找

~~~python 
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name']) # Tom
print(dict1['id']) # 报错
~~~

![image-20220624163803797](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241640397.png)

> 如果当前查找的key存在，则返回对应的值；否则报错

#### get()

- 语法

    ~~~python
    字典序列.get(key,默认值)
    ~~~

    > 如果当前查找的key不存在则返回第二个参数（默认值），如果省略第二个参数，则返回None

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name'))  # Tom
# 110
print(dict1.get('id', 110))
# None
print(dict1.get(' id'))
~~~

![image-20220624164459775](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241644859.png)

#### keys()

查找字典中所有的key，返回可迭代对象

~~~python 
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict_keys(['name', 'age', 'gender'])
print(dict1.keys())
~~~

![image-20220624164657320](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241646408.png)

#### values()

查找字典中所有的value，返回可迭代对象

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict_values(['Tom', 20, '男'])
print(dict1.values())
~~~

![image-20220624164848576](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241648662.png)

#### items()

查找字典中所有的键值对，返回可迭代对象，元组数据1是字典的key，元组数据2是字典的value

~~~python 
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])
print(dict1.items())
~~~

![image-20220624164942602](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241649702.png)

### 删除

- del()/del：删除字典或删除字典中指定的键值对

    ~~~python
    dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
    del dict1['gender']
    # {'name': 'Tom', 'age': 20}
    print(dict1)
    ~~~

    ![image-20220624150143518](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241501645.png)

- clear()：清空字典

    ~~~python
    dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
    dict1.clear()
    # {}
    print(dict1)
    ~~~

    ![image-20220624150231516](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241502623.png)

### 循环遍历

#### 循环遍历-key

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(key)
~~~

![image-20220624165254516](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241656539.png)

#### 循环遍历-value

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for value in dict1.values():
    print(value)
~~~

![image-20220624165334714](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241653806.png)

#### 循环遍历-键值对

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for item in dict1.items():
    print(item)
~~~

![image-20220624165550673](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206241655758.png)

#### 循环遍历-键值对（拆包）

~~~python
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key, value in dict1.items():
    print(f'{key}={value}')
~~~

![image-20220628103639133](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281036232.png)

## 集合

### 创建

创建集合使用`{}`或者`set()`，但是如果要创建空集合，只能使用`set()`，因为`{}`用来创建空字典

~~~python
s3 = set('abcdefg')
~~~

### 新增

#### add()

~~~python
s1 = {10, 20}
s1.add(100)
s1.add(10)
# {100, 10, 20}
print(s1)
~~~

​		![image-20220628104403772](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281044843.png)

> 集合具有去重功能，所以，当向集合内追加的数据是当前集合已有数据的话，则不进行任何操作

	#### update()

追加的数据是序列

~~~Python
s1 = {10, 20}
s1.update([100, 200])
s1.update('abc')
# {100, 'c', 'a', 200, 10, 20, 'b'}
print(s1)
~~~

![image-20220628104717280](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281047365.png)

### 删除

#### remove()

删除集合中指定数据，如果数据不存在则报错

~~~python
s1 = {10, 20}
s1.remove(10)
print(s1)
~~~

![image-20220628104906245](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281049332.png)

#### discard()

删除集合中指定数据，如果数据不存在也不会报错

~~~Python
s1 = {10, 20}
s1.discard(20)
print(s1)
~~~

![image-20220628105011979](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281050050.png)

#### pop()

随机删除集合中的某个数据，并返回这个数据

~~~Python
s1 = {10, 20, 30, 40, 50}
del_num = s1.pop()
print(del_num)
~~~

![image-20220628105100228](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281051299.png)

### 查找

- in：判断数据在集合序列
- not in：判断数据不在集合序列

~~~python
s1 = {10, 20, 30, 40, 50}
print(10 in s1)
print(10 not in s1)
~~~

![image-20220628105353950](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281053025.png)

## 公共函数

| 函数                          | 描述                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| len()                         | 计算容器中元素个数                                           |
| del 或 del()                  | 删除                                                         |
| max()                         | 返回容器中元素最大值                                         |
| min()                         | 返回容器中元素最小值                                         |
| range(start,end,step)         | 生成从start到end的数字，步长为step，供for循环使用。range()生成的序列不包含end数字 |
| enumerate(可遍历对象,start=0) | 函数用于将一个可遍历的数据对象（列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，一般用在for循环中.start参数用来设置遍历数据的下标的起始值，默认为0 |

~~~Python
list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1):
    print(i)

for index, char in enumerate(list1, start=1):
    print(f'下标是{index}，对应的字符是{char}')
~~~

![image-20220628111216987](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281112085.png)

## 推导式

### 列表推导式

作用：用一个表达式创建一个有规律的列表或控制一个有规律的列表

列表推导式又叫列表生成式

~~~Python
# 需求：创建一个0-10的列表

list1 = [i for i in range(10)]
print(list1)
~~~

![image-20220628112153322](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206281121423.png)

### 字典推导式

~~~Python
# 创建一个字典，字典key是1-5数字，value是这个数字的2次方
dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)
~~~

![image-20220629141730998](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206291417111.png)

~~~Python
# 将两个列表合并成一个字典
list1 = ['name', 'age', 'gender']
list2 = ['Tom', 20, 'man']
dict1 = {list1[i]: list2[i] for i in range(len(list1))}
print(dict1)
~~~

![image-20220629142240591](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206291422681.png)

> 1、如果两个列表的数据个数相同，len统计任何一个列表的长度都可以
>
> 2、如果两个列表的数据格式不相同，len统计数据多的列表数据个数会报错，len统计数量少的列表数据不会报错

~~~Python
# 提取字典中目标数据
counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}

# 提取上述电脑数量大于等于200的字典数据
count1 = {key: value for key, value in counts.items() if value > 200}
print(count1)
~~~

![image-20220630094926773](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206300949016.png)

### 集合推导式

~~~python
list1 = [1, 1, 2]
set1 = {i ** 2 for i in list1}
print(set1)
~~~

![image-20220630095501495](https://raw.githubusercontent.com/zhouwei1997/Image/master/202206300955583.png)

> 集合有数据去重功能

## 函数

### 定义函数

~~~python
def 函数名(参数):
    代码1
    代码2
    ……
~~~

### 调用函数

~~~python
函数名(参数)
~~~

> 1、在不同的需求中，参数可有可无
>
> 2、在python中，函数必须先定义后调用







## Lamdba

## 文件操作

