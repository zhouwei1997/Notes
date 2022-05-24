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

> 特点：条件为真就进入死循环，条件为假就退出循环

### 语法结构

~~~shell
while 表达式
	do
		command
	done
	
while expression [ 1 -eq 1 ]
	do
		command
	d
~~~

~~~shell
# 计算1-50的偶数和

#!/bin/bash
sum=0
i=2
# 循环打印1-50的偶数和，计算后重新赋值给sum
while [ $i -le 50 ]
do
	let sum=sum+i
	let i+=2
done
echo "1-50的偶数和为：$sum"
~~~

### 应用场景

写一个30秒同步一次时间，向同步时间服务器10.1.1.250的脚本，如果同步失败，则进行邮件告警，每次失败都告警。同步成功，夜景下邮件通知。但是成功100次才通知一次

~~~shell
#!/bin/bash
count=0
ntp_server=10.1.1.250
while true; do
    rdate -s $ntp_server &>/dev/null
    if [ $? -ne 0 ]; then
        echo "system date failed" | mail -s 'check system date' root@localhost
    else
        let count++
        if [ $(($count % 100)) -eq 0 ]; then
            echo "system date successful" | mail -s 'check system date' root@localhost && count=0
        fi
    fi
    sleep 30
done

~~~

## until循环

### 语法结构

~~~shell
until expression [ 1 -eq 1 ]
  do
    command
  done
~~~

### 应用场景

使用until语句批量创建10个用户，要求stu1-stu5用户的UID分别是1001-1005；stu6-stu10用户的家目录分别在/rhome/stu6-stu10

~~~shell
#!/bin/bash
i=1
until [ $i -gt 10 ]; do
    if [ $i -le 5 ]; then
        useradd -u 100$i stu$i && echo 123 | passwd --stdin stu$i
    else
        [ ! -d /rhome ] && mkdir /rhome
        useradd -d /rhome/stu$i && cho 123 | passwd --stdin stu$i
    fi
    let i++
done
~~~