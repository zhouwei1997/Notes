# Linux基础
[TOC]
## 系统文件架构

![image-20220420134500962](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204201345059.png)

| 一级目录     | 功能（作用）                                                 |
| ------------ | ------------------------------------------------------------ |
| /bin/        | 存放系统命令，普通用户和root都可以执行。放在/bin下的命令在单用户模式下也可以执行 |
| /boot/       | 系统启动目录，保存与系统启动相关的文件，如内核文件和启动引导程序（grub）文件等 |
| /dev/        | 设备文件保存位置                                             |
| /etc/        | 配置文件保存位置。系统内所有采用默认安装方式（rpm安装）的服务配置文件全部保存在此目录中，如用户信息、服务的启动脚本、常用服务的配置文件等 |
| /home/       | 普通用户的主目录（家目录）。在创建用户时，每个用户要有一个默认登录和保存自己数据的位置，就是用户的主目录，所有普通用户的主目录都是在/home/下建立一个和用户名相同的目录 |
| /lib/        | 系统调用的函数库保存位置                                     |
| /media/      | 挂载目录。系统建议用来挂载媒体设备，如软盘和光驱             |
| /mnt/        | 挂载目录。早期Linux中只有这一个挂载目录，并没有细分。系统建议这个目录用来挂载额外的设备。例如U盘、移动硬盘和其他操作系统的分区 |
| /misc/       | 挂载目录，系统建议用来挂载NFS服务的目录。                    |
| /opt/        | 第三方安装的软件保存位置。这个目录是放置和安装其他软件的位置，手工安装的源码包软件都可以安装在这个目录下 |
| /root/       | root的主目录                                                 |
| /sbin/       | 保存与系统环境变量设置相关的目录，只有root可以使用这些命令进行系统环境设置 |
| /usr/        | 服务数据目录。一些系统服务启动之后，可以在这个目录中保存所使用的数据 |
| /tmp/        | 临时目录，系统存放临时文件的目录，在该目录下，所有用户都可以访问和读写 |
| /lost+found/ | 当系统意外崩溃或意外关机时，产生的一些文件碎片会存放在这里。系统启动的过程中，fsck工具会检查这里，并修复以及损坏的文件系统。这个目录只有在每个分区中出现 |
| /proc/       | 虚拟文件系统，该目录中的数据并不保存在硬盘上，而是保存在内存中。主要保存系统的内核、进程、外呼设备状态和网络状态等 |
| /sys/        | 虚拟文件系统。和/proc/目录相似，该目录中的数据都保存在内存中，主要保存与内核相关的信息 |

## Linux入门命令

### uname查看操作系统信息

命令：uname [参数]

作用：获取计算机操作系统相关信息

参数：-a , 选项 -a代表all，表示获取全部的系统信息（类型、全部主机名、内核版本、发布时间、开源计划）

![image-20220420155307410](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204201553502.png)

~~~shell
用法一：直接输入uname或者uname -a
含义：获取操作系统的信息
# uname
# uname -a
~~~

### su切换用户命令

命令：su [-] 用户名称

作用：切换用户

> 横杆【-】的作用是表示在切换用户的同时切换用户的家目录

### ls命令

主要功能：以平铺的形式显示当前目录下文件信息

基本语法：ls [参数] [目录]

| 选项 | 说明                                                  |
| ---- | ----------------------------------------------------- |
| -l   | ls -l  以详细列表的形式显示当前或其他目录下的文件信息 |
| -h   | ls -lh  代表以较高可读性显示文件的大小                |
| -a   | ls -a  显示所有的文件信息（包含隐含文件）             |

### pwd命令

主要功能：打印当前工作目录

基本语法：pwd

![image-20220420162152158](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204201621218.png)

### cd命令

主要功能：切换目录

基本语法：cd [路径]

~~~shell
# 切换到/usr/local目录下
cd /usr/local

# 切换到当前用户的家目录
cd
cd ~

# 切换到上一级目录
cd ../
~~~

### clear命令

主要功能：清屏

基本语法：clear

### whoami命令

主要功能：用户获取当前用户的用户名

基本语法：whoami

### reboot命令

主要功能：立即重启服务器

基本语法：reboot

### shutdown命令

主要功能：立即关机或延迟关机

~~~shell
# 立即关机
shutdown -h 0
shutdown -h now
-h halt缩写，代表关机
~~~

> 在Linux系统中，立即关机除了使用shutdowun -h 0以外还可以是用halt -p

~~~shell
# 延迟关机
shutdown -h 分钟数   # 代表多少分钟后，自动关机
shutdown -h 10
~~~

~~~shell
# 取消关机
ctrl + c

~~~



### type命令

命令：type

作用：查看一个命令是内部命令还是外部命令

![image-20220421134644470](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204211346551.png)

### hostnamectl命令

主要功能：主要用于设置计算机的主机名称

~~~shell
#获取计算机的主机名
hostname
hostnamectl
~~~

> CentOS7中主机名分为3类，静态的（static）、瞬态的（transient）和灵活的（pretty）
>
> 1. 静态static主机名称：电脑关机或重启后，设置的主机名称依然有效
> 2. 瞬态transient主机名：临时主机名称，电脑关机或重启后，设置的名称就失效了
> 3. 灵活pretty主机名称：可以包含一些特殊的字符



> 修改主机名称永久生效
>
> 1、使用静态的主机名
>
> 2、修改/etc/hostname文件

![image-20220422104628289](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221046374.png)

#### 瞬态主机名设置

~~~shell
# hostnamectl  --transient set-hostname 主机名
hostnamectl  --transient set-hostname yunwei-01
# 立即生效
su
~~~

![image-20220422105303044](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221053117.png)

#### 静态主机名称

~~~shell
# hostnamectl  --static set-hostname 主机名
# --static 可以省略
hostnamectl  --static set-hostname zhouwei-01
# 立即生效
su
~~~

![image-20220422105454122](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221054191.png)

#### 灵活主机名称

~~~shell
# hostnamectl  --pretty set-hostname 主机名
hostnamectl  --pretty set-hostname itcast@#
# 立即生效
su
# 查看灵活的主机名称
hostnamectl --pretty
~~~

![image-20220422105934374](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221059433.png)

## Linux文件管理

### 文件管理命令

#### 目录的创建与删除

##### mkdir创建目录

命令：mkdir 目录名

语法：mkdir [选项] [目录名]

常见参数：

| 参数 | 作用             |
| ---- | ---------------- |
| -p   | 递归创建所有目录 |

![image-20220422111300309](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221113415.png)

##### rmdir删除目录

基本语法：rmdir 目录名称

常见参数：

| 参数 | 作用           |
| ---- | -------------- |
| -p   | 递归删除空目录 |

![image-20220422111855462](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221118535.png)

#### 文件操作

##### 创建

命令：touch

语法：touch 文件路径 [文件路径2 文件路径3...]

~~~shell
# 在当前目录下创建一个readme.txt文件
touch readme.txt
~~~

![image-20220422162946933](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221629027.png)

~~~shell
# 根据序号同时创建多个文件，在当前路径下生成1.txt/2.txt/...5.txt
# 1 表示开始的数字
# .. 表示连续的
# 5 表示结束的数字
touch {1..5}.txt
~~~

![image-20220422165056357](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221650455.png)

##### 删除

命令：rm

作用：删除文件或文件夹

语法：rm [参数选项] 文件或文件夹

选项：

| 选项 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -r   | 递归删除。只要用于删除目录，可删除指定目录及包含的所有内容，包括所有子目录和文件 |
| -f   | 强制删除。不提示任何选项                                     |

![image-20220422171506790](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204221715866.png)

##### 复制

基本语法：cp [选项] 源文件或文件夹   目录地址

选项说明：

| 选项 | 说明                     |
| ---- | ------------------------ |
| -r   | 递归复制，主要针对文件夹 |

![image-20220428105754157](https://raw.githubusercontent.com/zhouwei1997/Image/master/202204281057281.png)

~~~shell
# cp复制并重命名文件
# cp [选项] 源文件或文件夹   目录路径/新文件或新文件夹名称
~~~

##### 剪切与重命名

命令：mv

作用：可以在不同的目录之间移动文件或目录，也可以对文件和目录进行重命名

语法：mv [参数] 源文件 目标路径（不指定文件名）

~~~shell
# 剪切操作
mv /root/readme.txt /home/readme.txt

# 重命名
mv readme.txt rea.txt
~~~

### 打包压缩与解压缩

#### tar压缩与解压缩

基本语法：tar [选项] 打包后的名称.tar 多个文件或文件夹

选项说明：

| 选项 | 说明                   |
| ---- | ---------------------- |
| -c   | 打包                   |
| -f   | 打包后的文件名称       |
| -v   | 显示打包的进度         |
| -u   | 更新原打包文件中的文件 |
| -t   | 查看打包的文件内容     |
| -z   | 压缩为gz格式           |
| -x   | 释放tar包中的文件      |
| -j   | 压缩为bz2格式          |
| -J   | 压缩为xz格式           |

~~~shell
# 把 a.txt b.txt c.txt文件打包的abc.tar文件中
tar -cvf abc.tar a.txt b.txt c.txt

# 查看tar包后的文件信息
# tar -tf 打包后的文件名称
tar -tf abc.tar

# 更新打包后的文件
# tar -uf 打包后的文件名称
tar -uf abc.tar d.txt

# 释放tar中的文件
# tar -xf 打包后的文件名称
tar -xf abc.tar
~~~

~~~shell 
# 打包并压缩
# tar [选项] 压缩后的压缩包名称  要压缩的文件或文件夹
tar -zcvf 123.tar.gz 1.txt 2.txt 3.txt
tar -jcvf 123.tar.bz2 1.txt 2.txt 3.txt
tar -Jcvf 123.tar.xz 1.txt 2.txt 3.txt
~~~

>压缩速度：gzip >bzip2>xz
>
>压缩率：xz>bzip2>gzip

~~~shell 
# 解压缩操作
tar -zxvf 123.tar.gz 
tar -jxvf 123.tar.bz2 
tar -Jxvf 123.tar.xz 
~~~

#### zip压缩

命令：zip

作用：兼容类Unix和windows，可以压缩多个文件或目录

语法：zip [参数] 压缩后的文件 需要压缩的文件（可以是多个文件）

参数说明：

| 参数 | 说明                   |
| ---- | ---------------------- |
| -r   | 递归压缩（压缩文件夹） |

~~~shell
# 文件压缩
zip 1.zip 1.txt
~~~

#### unzip解压缩

基本语法：unzip 压缩包名称  [选项] [指定解压路径]

选项说明：

| 选项 | 说明             |
| ---- | ---------------- |
| -d   | 解压到指定路径下 |

```shell
# unzip解压缩
unzip 1.zip -d /home/nginx/
```

### wc命令

命令：wc

作用：用于统计文件内容信息（包含行数、单词数、字节数）

语法：wc [参数选项]  文件名

参数选项：

| 参数 | 作用                               |
| ---- | ---------------------------------- |
| -l   | 行数（以回车/换行符为标准）        |
| -w   | 单词数（依照空格数来判断单词数量） |
| -c   | 字节数（空格、回车、换行）         |

~~~shell
# wc -lwc 文件名
# 统计/var/log/boot.log文件的行数，单词数，字节数
wc -lwc /var/log/boot.log
# wc命令选项可以混在一起搭配使用，但选项的顺序不影响删除的结果，第一个是行数，第二个是单词数，第三个是字节数
~~~

![image-20220506100713518](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061007590.png)

### du命令

命令：du

作用：查看文件或目录（递归显示子目录）占用磁盘大小

语法：du [参数选项] 文件名或目录名

参数：

| 参数 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -s   | 只显示汇总的大小，统计文件夹的大小                           |
| -h   | 表示以高可读性的形式进行显示，如果不使用-h，默认使用KB的形式显示文件大小 |

```shell
# du 文件名
# 统计/var/log/boot.log文件大小
du /var/log/boot.log

# du -h 文件名
# 统计/var/log/boot.log文件大小，以高可读性显示
du -h /var/log/boot.log
```

![image-20220506101936719](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061019800.png)

### find命令

命令：find

作用：用于查找文档

语法：find 路径范围 选项1 选项1的值 [选项2 选项2的值...]

常用参数：

| 参数  | 说明                                                         |
| ----- | ------------------------------------------------------------ |
| -name | 按照文档名称进行搜索（支持模糊搜索）                         |
| -type | 按照文档类型进行搜索，文档类型的值 f-->表示文件，d-->表示文件夹 |

~~~shell
# 在/var/目录下，查找名称为boot.log，类型是文件的文档
find /var/ -name boot.log -type f
~~~

![image-20220506103421782](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061034850.png)

~~~shell
# 全盘搜索ssh目录
find /* -name "ssh" -type d
~~~

![image-20220506103706755](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061037827.png)

~~~shell 
# 搜索/var/log/目录下所有以".log"结尾的文件信息
find /* -name *.log -type f
~~~

![image-20220506104049133](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061040228.png)

### grep命令

命令：grep

作用：在文件中直接查找到包含指定信息的那些行，并把这些信息高亮显示出来

语法：grep [选项] 要查找的内容 文件名

选项说明：

| 选项 | 说明                         |
| ---- | ---------------------------- |
| -n   | 代表显示包含关键词的行号信息 |
| -r   | 递归查找                     |

~~~shell
# grep 查找的内容 文件名
# 在boot.log文件中，查找包含network的行
grep network boot.log
~~~

![image-20220506104635002](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061046091.png)

~~~shell
# grep -r 查找的内容 多个文件
grep -r network /var/log/*
~~~

![](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061049087.png)

## Linux用户管理

### 多账号作用

1. 针对不同用户分配不同的权限，不同权限可以限制用户可以访问到的系统资源

2. 提高系统的安全性

3. 帮助系统管理员对使用系统的用户进行跟踪

### 用户及用户组

Linux系统中的每个用户在创建时都应该有一个对应的用户组，这个组就称之为用户的主组。同时，有些情况下，某个用户需要临时使用某个组的权限，那这个组就称之为这个用户的附加组或附属组。

>主组只能拥有一个，但是附属组可以有多个

#### 用户组管理

##### 用户组添加

命令：groupadd

作用：添加用户组

语法：groudadd [参数选项  选项值] 用户组名

选项：

| 选项 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -g   | 设置用户组ID  数字，如果不指定，则默认从1000之后添加。自定义组必须从1000开始，不能重复 |

~~~shell
# groupadd 组名
# 新增一个组叫hr
groupadd hr

# 新增一个组叫test并指定编号为1100
groupadd -g 1100 test
~~~

![image-20220506145846776](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061458851.png)

> 默认情况下，新增的用户组都会存放在`/etc/group`文件中

~~~shell
test:x:1100:
# 第一列：代表用户组的组名称
# 第二列：用户组的组密码，使用一个x占位符
# 第三列：用户组的组ID编号，1-999代表系统用户组的组编号，1000以后的代表自定义组的组编号
# 第四列：用户组内的用户信息（如果一个用户的附属组或附加组为这个组名，则显示在此位置）
~~~

##### 用户组修改

命令：groupmod

作用：修改用户组

语法：groudmod [参数选项  选项值] 用户组名

选项：

| 选项 | 说明                                |
| ---- | ----------------------------------- |
| -g   | gid的缩写，设置一个自定义的用户组ID |
| -n   | name的缩写，设置新的用户组的名称    |

~~~shell
# 修改hr的用户组，将组id改为1101并将名称改为bjhr
groupmod -g 1101 -n bjhr hr
~~~

![image-20220506150916238](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061509297.png)

![image-20220506150928411](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061509467.png)

##### 用户组删除

命令：groupdel

作用：删除用户组

语法：groupdel 用户组名

~~~shell
groupdel test
~~~

#### 用户管理

##### useradd添加用户

命令：useradd

作用：添加用户

语法：useradd [选项1 选项的值1 选项2 选项的值2...] 用户名

选项：

| 选项 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| -g   | 表示指定用户的用户主组，选择值可以是用户组ID，也可以是组名   |
| -G   | 表示指定用户的用户附加组，选择值可以是用户组ID，也可以是主名。可以指定多个，用逗号隔开 |
| -u   | uid，用户的id(用户的标识符)，系统默认会从1000之后按照顺序分配uid，如果不想使用系统分配的，可以通过该选项自定义 |
| -c   | comment  添加注释                                            |
| -s   | 指定用户登入后所使用的shell解释器，默认`/bin/bash`如果不想让其登录，则可以设置为`/sbin/nologin` |
| -d   | 指定用户登录时开始的目录（家目录的位置）                     |
| -n   | 取消建立以用户名称为名的群组                                 |

~~~shell
# 创建一个linuxuser的账号
useradd linuxuser
~~~

> 在创建账号时，如果没有明确指定用户所属的主组，默认情况下会自动在用户组中创建一个与用户同名的用户组，这个组就是这个用户的主组

~~~shell
# 创建一个用户zhangsan,指定用户所属的主组为test
useradd -g 1100 zhangsan
~~~

![image-20220506165807003](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061658085.png)

~~~shell
# 创建一个账号lisi，指定用户只能被软件所使用，不能用于登录操作系统
useradd -g 1101 -s /sbin/nologin lisi
~~~

##### /etc/passwd存储用户信息的文件

每创建一个用户，则在此文件中创建一行

![image-20220507095211582](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205070952680.png)

>第一列：用户名称
>
>第二列：用户密码，使用x占位符，真实密码存储在`/etc/shadow`中
>
>第三列：用户的ID编号
>
>第四列：用户的主组ID编号
>
>第五列：代表注释信息
>
>第六列：用户的家目录
>
>第七列：用户可以使用的shell类型

##### id查看用户信息

基本语法：id  用户名称

作用：查询某个用户的信息

~~~shell
id lisi
~~~

![image-20220506171049597](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205061710678.png)

##### usermod修改用户

基本语法：usermod [选项 选项的值] 用户名称

| 选项 | 说明                             |
| ---- | -------------------------------- |
| -g   | 修改用户所属的主组的编号         |
| -G   | 修改用户的附属组的编号           |
| -l   | 修改的用户的名称                 |
| -s   | 修改用户使用的shell类型          |
| -d   | 修改用户的家目录                 |
| -c   | 修改用户的备注信息               |
| -L   | 锁定用户，锁定后用户无法登录系统 |
| -U   | 解锁用户                         |

~~~shell
# 修改zhangsan的账号信息，改名为zs
usermod -l zs zhangsan

# 修改wangwu的账号信息，用户主组的编号更新为1000
usermod -g 1000 wangwu

# 禁止linuxuser账号登录系统
usermod -s /sbin/login linuxuser
~~~

##### userdel删除用户

基本语法：userdel [选项] 用户名称

| 选项 | 说明                             |
| ---- | -------------------------------- |
| -r   | 删除用户的同时，删除用户的家目录 |

## 管道

### 管道符

管道符：|

作用：管道是一种通信机制，通常用于进程间的通信。他表现出来的形式将前面每一个进程的输出直接作为下一个进程的输入

![image-20220507154635793](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071546879.png)

>0：标准输入。进程需要外部的某些程序传递相应的参数，才能正常运行
>
>1：标准输出。程序或命令正确的执行结果
>
>2：标准错误。程序或命令错误的执行结果

### 过滤（筛选）功能

基本语法：前一个命令 | 后一个命令

~~~shell
# 获取根目录下包含关键字"y"的文件信息
ls / | grep "y"
~~~

~~~shell
# 检索系统已安装文件，只筛选mariadb信息
rpm -qa | grep mariadb
~~~

![image-20220507155716653](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071557729.png)

### 统计功能

~~~shell
# 统计根目录下一共有多少个文件
ls / | wc -l
~~~

![image-20220507160656121](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071606208.png)

~~~shell 
# 查看/etc/group文件多少行
cat /etc/group | wc -l
~~~

![image-20220507160928136](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071609218.png)

### xargs命令

>由于部分命令不支持管道符，所以需要使用xargs命令来进行补充

~~~shell
# 搜索etc目录下所有conf结尾的信息，然后以详细列表显示
find /etc -name "*.conf" | xargs ls -l
~~~

![image-20220507161224113](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071612230.png)

## 网络配置与远程管理









## 权限管理









## 系统服务









## Linux进程检测与进程管理













## 阿里云与开源项目上线部署实战





