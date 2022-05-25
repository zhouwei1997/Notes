# sed

[TOC]

## sed的工作流

![image-20220524164115392](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205241641742.png)

- 首先sed把当前正在处理的行保存在一个临时缓存区中，然后处理临时缓存区中的行，完成后把该行发送到屏幕上
- sed把每一行都存在临时缓存区中，对这个副本进行编辑，所以不会修改原文件
- sed主要用来自动编辑一个或多个文件，简化对文件的反复操作，编写转换程序等

## sed使用方法

sed常见的语法格式有两种，一种叫命令行模式，另一种叫脚本模式

### 命令行模式

~~~shell
sed [option] 'sed的命令|地址定位' filename

说明：引用shell script中变量应该使用双引号
~~~

| 选项 | 说明                                          |
| ---- | --------------------------------------------- |
| -e   | 进行多项编辑，即对输入行引用多条sed命令时使用 |
| -n   | 取消默认的输出                                |
| -f   | 指定sed脚本的文件名                           |
| -r   | 使用扩展正则表达式                            |
| -i   | inplace 原地编辑（修改源文件）                |

#### 常用命令

| 命令 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| p    | 打印行                                                       |
| d    | 删除行                                                       |
| i    | 在当前行之前插入文本，多行时除最后一行外，每行末尾使用"\\"换行 |
| a    | 在当前行后添加一行或多行。多行时除最后一行外，每行末尾使用"\\"换行 |
| c    | 用此符号后的新文件替换当前行中的文本，多行时除最后一行外，每行末尾使用"\\"续行，整行替换 |
| r    | 从文件中读取输入行                                           |
| w    | 将所选的行写入文件                                           |
| s    | 用一个字符串替换另一个                                       |
| g    | 在行内进行全局搜索                                           |



~~~shell 
# 打印
sed 'p' 2.txt
# 取消打印
sed -n 'p' 2.txt
~~~

![image-20220525141936077](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251419270.png)

~~~shell
# 最后一行末尾添加
sed '$a9999' 2.txt
~~~

![image-20220525142532429](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251425484.png)

~~~shell 
# 每行末尾添加
sed 'a99999999' 2.txt
~~~

![image-20220525142617042](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251426102.png)

~~~shell
# 替换第五行为hello world
sed '5chello world' 2.txt
# 将每一行替换为hello world
sed 'chello world' 2.txt
~~~

![image-20220525142749648](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251427708.png)

~~~shell
sed -r '/([0-9]{1,3}\.){3}[0-9]{1,3}/w b.txt' 2.txt
# 将/etc/hosts文件中的的第一行加入到2.txt
sed '1r /etc/hosts' 2.txt
~~~

![image-20220525144832803](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251448875.png)

~~~shell 
# 把2.txt的1-3行另存为到a.txt中
sed '1,3w a.txt' 2.txt
~~~

![image-20220525144951373](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251449431.png)

~~~shell
# 将2.txt文件中的root替换成ROOT
sed -n 's/root/ROOT/p' 2.txt
# 将2.txt文件中的root全部替换成ROOT
sed -n 's/root/ROOT/gp' 2.txt
# 注释1-5行内容
sed -n '1,5s/^/#/p' 2.txt
~~~

![image-20220525145701290](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205251457346.png)

#### 应用

~~~shell
# 过滤出ifcfg-ens33文件中的IP、子网掩码、广播地址
sed -n -r '/([0-9]{1,3}\.){3}[0-9]{1,3}/p' /etc/sysconfig/network-scripts/ifcfg-ens33 | sed -n 's/[A-Z]=]//gp'
~~~


