# Shell循环

[TOC]

## for循环

### 语法结构

#### 列表循环

列表for循环：用于将一组命令执行已知的次数

~~~shell
for variable in {list};
	do
		command
		command
		...
	done
~~~

~~~shell 
for variable in a b c;
	do
		command
		command
		...
	done
~~~

~~~shell 
#!/bin/bash
for i in {1..5};
	do 
		echo $i
	done	
~~~

#### 不带列表循环

不带列表的for循环执行时由用户指定参数和参数的个数

~~~shell
for variable
	do 
		command
		command
		...
	done
~~~

~~~shell 
#!/bin/bash
for var
	do
		echo $var
	done 
	echo "脚本后面有$#个参数"
~~~

#### 类C风格的for循环

~~~shell
for((expr1;expr2;expr3 ))
	do
		command
		command
		...
	done

# expr1：定义变量并赋初始值
# expr2：决定是否进行循环
# expr3：决定循环变量如何改变，决定循环什么时候退出
~~~

~~~shell
#!/bin/bash
for ((i=1;i<=5;i++));
	do
		echo $i
	done
~~~

## 循环控制

循环体：do....done之间内容

- continue：继续，表示循环体内下面的代码不执行，重新开始下一次循环
- break：打断，马上停止执行本次循环，执行循环体后面的代码
- exit：表示直接跳出程序

~~~shell
#!/bin/bash
for i in {1..5}
do
	test $i -eq 2 && break || touch /tmp/file$i
done
echo hello hahahaha
~~~


## while循环