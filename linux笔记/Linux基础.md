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

## 网络配置

### ifconfig查看网络信息

命令：ifconfig

作用：查看网卡信息

![image-20220507163044111](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071630212.png)

### 网卡配置文件

Linux的网卡配置文件`/etc/sysconfig/network-scripts/ifcfg-ens33`

~~~shell 
vim /etc/sysconfig/network-scripts/ifcfg-ens33

TYPE="Ethernet"   # 网络类型 Ethernet-->以太网
PROXY_METHOD="none"
BROWSER_ONLY="no"
BOOTPROTO="none"   # IP获取方式,DHCP-->动态获取  static/none--> 手工设置
DEFROUTE="yes"
IPV4_FAILURE_FATAL="no"
IPV6INIT="yes"
IPV6_AUTOCONF="yes"
IPV6_DEFROUTE="yes"
IPV6_FAILURE_FATAL="no"
IPV6_ADDR_GEN_MODE="stable-privacy"
NAME="ens33"  # 网卡名称
UUID="9e3abe7f-ed72-4ce8-bcae-1a926e81984c" # 代表网卡的UUID编号（必须唯一）
DEVICE="ens33" # 设备名称
ONBOOT="yes" # 网卡是否开机启动
IPADDR="192.168.31.105"
PREFIX="24"
GATEWAY="192.168.31.2"
DNS1="223.5.5.5"
DNS2="223.6.6.6"
IPV6_PRIVACY="no"
~~~

### 查看网卡状态

~~~shell
# 查询网卡状态
systemctl status network

# 网卡启动/停止/重启
systemctl start|stop|restart network
~~~

## 远程管理

#### SSH协议

SSH是用于计算机质检的加密登录协议

#### sshd服务

~~~shell
systemctl status sshd
~~~

![image-20220507165043978](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205071650109.png)

## 权限管理

在多用户计算机系统的管理中，权限是指某个特定用户具有特定的系统资源使用权限。

|       | 权限针对文件                                              | 权限针对目录                                                 |
| ----- | --------------------------------------------------------- | ------------------------------------------------------------ |
| 读r   | 表示可以查看文件内容；cat                                 | 表示可以（ls）查看目录中存在的文件名称                       |
| 写w   | 表示可以更改文件的内容；vim修改，保存退出                 | 表示是否可以删除目录中的子文件或者新建子目录（rm/touch/mkdir） |
| 执行x | 表示是否可以开启文件当中记录的程序，一般指二进制文件(.sh) | 表示是否可以进入目录（cd）                                   |

> 一般给予目录读权限，也会给予执行权限

### 普通权限管理

![image-20220509104702343](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205091047457.png)

~~~shell
-rwxr-xr-x. 1 root root 4364 4月  28 2021 poweroff-vm-default
第一列：文件类型和权限
第二列：文件的节点数
第三列：文件的拥有者
第四列：文件的所属组
第五列：文件大小
第六列：文件的最后修改时间
第七列：文件的名称
~~~

![image-20220509105759821](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205091057918.png)

### 设置文件/目录权限

命令：chmod

语法：chmod [选项] 权限模式 文件/目录

作用：增加或减少当前文件所有者的权限

| 选项 | 说明                                 |
| ---- | ------------------------------------ |
| -R   | 递归设置权限（当为文件夹的时候使用） |

>要给文件设置权限，操作者只能是root或文件的所有者

#### 字母形式

1. 确认要给那个身份设置权限。u-拥有者/g-所属组/o-其他/ugo(a)-所有
2. 确认是添加权限（+）、删除权限（-）、赋予权限（=）
3. 确认给这个用户针对这个文件或文件夹设置什么样的权限 r/w/x

~~~shell
# 给readme.txt文件的拥有者增加一个可执行文件
chmod u+x readme.txt
# 给readme.txt文件的拥有者的可执行权限去除
chmod u-x readme.txt
# 给readme.txt文件的所属组内的用户赋予rw权限
chmod g=rw readme.txt
# 给shop目录及内部的文件统一添加w可写权限
chmod -R ugo+w shop
chmod -R a+w
~~~

#### 数字形式

| 权限 | 对应数字 | 含义     |
| ---- | -------- | -------- |
| r    | 4        | 可读     |
| w    | 2        | 可写     |
| x    | 1        | 可执行   |
| -    | 0        | 没有权限 |

~~~shell
# 给readme.txt文件设置权限，文件拥有者rwx、组内用户rw、其他用户r
chmod 764 readme.txt
# 给shop文件夹设置777权限
chmod -R 777 shop
~~~

### 文件拥有者和所属组

#### 文件拥有者设置

基本语法：chown [选项] 新文件拥有者 文件名称

| 选项 | 说明                       |
| ---- | -------------------------- |
| -R   | 递归修改（主要针对文件夹） |

~~~shell
# 把/root/readme.txt文件的拥有者更改为linuxuser
chown linuxuser /root/readme.txt
# 把/root/shop文件夹的拥有者更改为linuxuser
chown -R linuxuser /root/shop
~~~

#### 文件所属组的设置

基本语法：chgrp [选项] 新文件所属组 文件名称

| 选项 | 说明                       |
| ---- | -------------------------- |
| -R   | 递归修改（主要针对文件夹） |

~~~shell
# 把/root/readme.txt文件的所属组更改为itheima
chgrp itheima /root/readme.txt
# 把/root/shop文件夹的拥有组更改为itheima
chgrp -R linuxuser /root/shop
~~~

#### 同时修改属组和属主

基本语法：

chown [选项] 文件拥有者: 文件所属组 文件名称

chown [选项] 文件拥有者 . 文件所属组 文件名称

| 选项 | 说明                       |
| ---- | -------------------------- |
| -R   | 递归修改（主要针对文件夹） |

~~~shell
# 把/root/shop文件夹的拥有组更改为root
chmod -R root:root /root/shop
chmod -R root.root /root/shop
~~~

### 特殊位S

作用：让一般使用者临时具有该文件的属组/主的执行权限

> 只要针对二进制文件

![image-20220509140733610](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205091407698.png)

~~~powershell
# 去除s位权限
chmod u-s /usr/bin/passwd
chmod 0755 /usr/bin/passwd

# 添加s位权限
chmod u+s /usr/bin/passwd
chmod 4755 /usr/bin/passwd
~~~

### 粘滞位T

作用：只允许文件的创建者和root用户删除文件

| 选项 | 说明       |
| ---- | ---------- |
| o+t  | 添加粘滞位 |
| o-t  | 去除粘滞位 |

> 主要针对文件夹

~~~shell
# 语法
chmod -R o+t 文件夹的名称
chmod -R 1777 文件夹的名称
~~~

![image-20220509143547636](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205091435736.png)

### ACL权限控制

ACL（Access Control List）访问控制列表，在Linux系统中，ACL可实现对单一用户设定访问文件权限。

> ACL权限可以针对某个用户，也可以针对某个组
>
> ACL优势就是让权限控制更加精准

#### 获取某个文件的ACL权限

基本语法：getfacl 文件/目录名称

~~~shell
getfacl /root/shop
~~~

![image-20220509144712097](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205091447197.png)

#### 给某个文件设置ACL权限

基本语法：setfacl [选项]  u/g: 用户名 : 权限 文件/目录名称

| 选项 | 说明                  |
| ---- | --------------------- |
| -m   | 修改ACL策略           |
| -x   | 去掉某个用户/组的权限 |
| -b   | 删除所有的ACL策略     |
| -R   | 递归，常用于文件夹    |

~~~shell
# 针对readme.txt文件给Linuxuser设置一个可读权限
setfacl -m u:linuxuser:r readme.txt
# 针对readme.txt文件给bjhr组设置一个可读可写权限
setfacl -m g:bjhr:rw readme.txt
~~~

## 系统服务

### systemctl管理服务

命令：systemctl 

作用：管理服务

语法：systemctl [选项] 服务名

| 选项    | 说明                       |
| ------- | -------------------------- |
| status  | 检查指定服务的运行状态     |
| start   | 启动指定服务               |
| stop    | 停止指定服务               |
| restart | 重启指定服务               |
| reload  | 出现加载指定服务的配置文件 |
| enable  | 指定服务开机自启动         |
| disable | 取消指定服务开机自启动     |

#### 显示系统服务

语法：systemctl [选项]

| 选项                            | 说明                               |
| ------------------------------- | ---------------------------------- |
| list-units --type service --all | 列出所有服务（包括已启动和未启的） |
| list-units --type service       | 列出所有启动的服务                 |

~~~shell
# 列出linux的所有服务
systemctl list-units --type service --all
# 列出linux的启动的服务
systemctl list-units --type service
# 筛选出想要的服务信息
systemctl list-units --type service | grep sshd
~~~

### NTP时间同步服务

NTP（Network Time Protocol）网络时间协议，是用来同步网络中各个计算机时间的协议

#### NTP时间同步操作

##### 手工同步

命令：ntpdate 时间服务器IP/域名

~~~shell
# 从服务器cn.ntp.org.cn同步标准时间
ntpdate cn.ntp.org.cn
~~~

> 从网络同步时间，要确保自己的服务器可以访问互联网

##### 自动同步

~~~shell
# 启动ntpd服务，并设置为开机启动
systemctl start ntpd
systemctl enable ntpd
~~~

NTP服务的配置文件位置`/etc/ntp.conf`

### 防火墙

#### firewalld防火墙

firewalld增加了区域（zone）的概念，指的是firewalld预先准备了几套防火墙策略的集合。

| 区域     | 默认策略                                                     |
| -------- | ------------------------------------------------------------ |
| trusted  | 允许所有数据包                                               |
| home     | 拒绝流入的流量，除非与流出的流量相关，允许ssh/mdns/ipp-client/amba-client/dhcpv6-client服务通过 |
| internal | 等同于home                                                   |
| work     | 拒绝流入的流量，除非与流出的流量相关，允许ssh/ipp-client/dhcpv6-client服务通过 |
| public   | 拒绝流入的流量，除非与流出的流量相关，允许ssh/dhcpv6-client服务通过 |
| external | 拒绝流入的流量，除非与流出的流量相关，允许ssh服务通过        |
| dmz      | 拒绝流入的流量，除非与流出的流量相关，允许ssh服务通过        |
| block    | 拒绝流入的流量，除非与流出的流量相关，非法流量采取拒绝操作   |
| drop     | 拒绝流入的流量，除非与流出的流量相关，非法流量采取拒绝操作   |

#### 运行模式和永久模式

运行模式：此模式下，配置的防火墙策略立即生效，但是不写入配置文件

永久模型：此模式下，配置的防火墙策略写入配置文件，但是需要reload重新加载才能生效

#### firewalld防火墙规则

命令：firewall-cmd

作用：管理firewalld具体配置

语法：firewall-cmd [参数选项1]...[参数选项n]

##### 查看防火墙默认的区域

~~~shell
firewall-cmd --get-default-zone
~~~

![image-20220511101736648](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205111017746.png)

##### 查看所有支持的区域

~~~shell 
firewall-cmd --get-zones
~~~

![image-20220511101915635](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205111019721.png)

##### 列出当前使用区域配置

~~~shell
firewall-cmd --list-all
~~~

![image-20220511102143726](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205111021807.png)

##### 列出所有区域的配置

~~~shell 
firewall-cmd --list-all-zones
~~~

![image-20220511103647676](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205111036773.png)

##### 添加允许通过的服务或端口

语法：firewall-cmd --zone=public --add-prot/service=端口/服务名

~~~shell 
# 在public区域，添加允许tcp协议的1024端口通过的规则
firewall-cmd --zone=public --add-port=1024/tcp

# 在public区域，添加允许ftp服务的规则
# 服务必须在/usr/lib/firewalld/services
firewall-cmd --zone=public --add-service=ftp
~~~

![image-20220511104412503](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205111044606.png)

> 添加规则后需要时候使用firewall-cmd --reload重新加载下防火墙

##### 去除允许通过的服务或端口

~~~shell
# 在public区域，移除允许tcp协议的1024端口通过的规则
firewall-cmd --zone=public --remove-port=1024/tcp

# 在public区域，移除允许ftp服务的规则
# 服务必须在/usr/lib/firewalld/services
firewall-cmd --zone=public --remove-service=ftp
~~~

![image-20220511105246123](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205111052222.png)

##### 永久模式参数permanent

~~~shell
# 根据服务名称添加规则
firewall-cmd --zone=public --add-service=ftp --permanent
# 根据端口号添加规则
firewall-cmd --zone=public --add-port=80/tcp --permanent

firewall-cmd --reload
~~~

### 计划任务

语法：crontab 选项

| 选项 | 说明                                   |
| ---- | -------------------------------------- |
| -l   | 列出指定用户的计划任务列表             |
| -e   | 编辑指定用户的计划任务列表             |
| -u   | 指定用户名，如果不指定，则表示当前用户 |
| -r   | 删除指定用户的计划任务列表             |

![image-20220511220111440](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205112201556.png)

> 四个符号：
>
> *：表示取值范围中的每个数字
>
> -：连续区间表达式，要表示1到5   1-5
>
> /：表示每多少个，例如：每10分钟一次，可以写成*/10
>
> ，：表示多个取值，比如在1点、2点和5点执行，则可以写成1,2,5

~~~shell
# 每月1/10/22日的4:45分重启network
45 4 1,10,22 * * /usr/bin/systemctl restart network

# 每周六、周日的1:10重启network
10 1 * * 6,7  /usr/bin/systemctl restart network

# 每天18:00至23:00之间每隔30分钟重启network服务
*/30 18-23 * * *  /usr/bin/systemctl restart network

# 每隔2天的8点到11点的第3和第15分钟执行一次重启
3,15 8-11 */2 * *  /usr/sbin/reboot
~~~

#### crontab的权限问题

corntab是任何用户都可以创建的计划任务，但是root用户可以通过配置来设置某些用户不允许设置计划任务

黑名单：`/etc/cron.deny`

白名单：`/etc/cron.allow`

> 白名单不存在，需要自己创建

>白名单的优先级高于黑名单，如果一个用户同时存在两个名单文件中，则会被默认允许创建计划任务

#### 计划任务文件路径

计划任务文件保存在`/var/spool/cron/用户名文件`

#### 查看计划任务日志信息

查看定时任务运行情况文件`/var/log/cron`

#### 一次性计划任务（at命令）

at：一次性定时执行任务

##### 安装at命令

CentOS 7版本自带at，其他的版本需要手动安装

~~~shell
yum install -y at
~~~

##### 启动底层服务

~~~shell
systemctl start atd
systemctl enable atd
~~~



~~~shell
# 三天后下午5点执行/bin/ls
at 5pm+3 days
/bin/ls
at>ctrl+D(退出)
~~~

![image-20220513103550799](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131035903.png)

~~~shell
# 查看at的计划任务
atq
~~~

![image-20220513103654646](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131036721.png)

~~~shell 
# 删除at的计划任务
atrm 任务号
~~~

![image-20220513103938126](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131039206.png)

## 进程检测与管理

**进程**是正在执行的一个程序或命令，每个进程都是一个运行的实体，并占用一定的系统资源。

**程序**是人使用计算语音编写的可以实现特定目标或解决特定问题的代码集合

### top命令

#### top查看CPU使用情况

命令：top

作用：查看服务器的进程占用资源（100%使用）

语法：top

交换操作快捷键

| 快捷键    | 说明                                          |
| --------- | --------------------------------------------- |
| W(大写)   | 表示将结果按照内存（MEM）从高到底进行降序排列 |
| P（大写） | 表示将结果按照CPU使用率从高到低进行降序配列   |

![image-20220513132311594](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131323710.png)

##### 第一行

![image-20220513133933044](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131339130.png)

| 内容                            | 说明                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| 13:23:02                        | 系统当前时间                                                 |
| up 5 min                        | 系统的运行时间                                               |
| 1 user                          | 当前系统登录了2个用户                                        |
| load averages 0.44 , 0.16, 0.06 | 系统在之前的1分钟，5分钟，15分钟的平均负载；如果CPU是单核的，则数字超过1就是高负载，如果CPU是4核的，则数字超过4就是高负载 |

> 查看CPU的总核心数
>
> grep 'core id' /proc/cpuinfo | sort -u | wc -l

##### 第二行

![image-20220513134003348](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131340428.png)

| 内容         | 说明                                            |
| ------------ | ----------------------------------------------- |
| Tasks        | 系统中的进程总数                                |
| 1 running    | 正在运行的进程数                                |
| 101 sleeping | 睡眠的进程数                                    |
| 0 stopped    | 正在停止的进程数                                |
| 0 zombie     | 僵尸进程数，如果不是0，则需要手动检查下僵尸进程 |

##### 第三行

![image-20220513134022397](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131340478.png)

| 内容 | 说明                                                         |
| ---- | ------------------------------------------------------------ |
| %CPU |                                                              |
| us   | 用户模式占用的CPU百分比                                      |
| sy   | 系统模式占用的CPU百分比                                      |
| ni   | 改变过优先级的用户进程占用的CPU百分比                        |
| id   | 空闲CPU占用的CPU百分比                                       |
| wa   | 等待输入/输出的进程占用的CPU百分比                           |
| hi   | 硬中断请求服务占用的CPU百分比                                |
| si   | 软中断请求服务占用的CPU百分比                                |
| st   | 虚拟时间百分比，就是当有虚拟机时，虚拟CPU等待实际CPU时间的百分比 |

##### 第四行

![image-20220513134039533](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131340613.png)

| 内容       | 说明           |
| ---------- | -------------- |
| KiB Mem    | 内存           |
| total      | 物理内存的总量 |
| free       | 空闲内容总量   |
| used       | 已使用内存总量 |
| buff/cache | 缓存           |

##### 第五行

![image-20220513134054332](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131340413.png)

| 内容       | 说明           |
| ---------- | -------------- |
| KiB SWAP   | swap交换内存   |
| total      | 物理内存的总量 |
| free       | 空闲内容总量   |
| used       | 已使用内存总量 |
| buff/cache | 缓存           |

#### top查看系统进程信息

![image-20220513154134358](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131541476.png)

| 内容   | 说明                                                         |
| ------ | ------------------------------------------------------------ |
| PID    | 进程的id号                                                   |
| USER   | 该进程所属的用户                                             |
| PR     | 优先级，数值越小优先级越高                                   |
| NI     | NICE优先级，数值越小优先级越高，取值范围-20到19，默认为0     |
| VIRT   | 该进程使用的虚拟内存的大小，单位KB                           |
| RES    | 该进程使用的物理内存的大小，单位KB                           |
| SHR    | 共享内存大小，单位KB。<br>计算一个进程实际使用使用的内存=常驻内存（RES）-共享内存（SHR） |
| S      | 进程状态。其中S表示睡眠，R表示运行                           |
| %CPU   | 该进程占用CPU的百分比                                        |
| %MEM   | 该进程占用内存的百分比                                       |
| TIME+  | 该进程共占用CPU的时间                                        |
| COMMON | 进程名称                                                     |

### ps命令

命令：ps

语法：ps [参数选项]

作用：查看服务器的进程信息

| 选项 | 作用           |
| ---- | -------------- |
| -e   | 列出全部的进程 |
| -f   | 显示全部的类   |

![image-20220513160647121](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131606249.png)

| 列    | 说明                                                         |
| ----- | ------------------------------------------------------------ |
| UID   | 该进程执行的用户ID                                           |
| PID   | 进程ID                                                       |
| PPID  | 该进程的父进程ID，如果找不到，则该进程就被称之为僵尸进程     |
| C     | CPU的占用率，百分数显示                                      |
| STIME | 进程的启动时间                                               |
| TTY   | 终端设备，发起该进程的设备识别符号，如果显示为？则表示该进程并不是由终端设备发起的 |
| TIME  | 进程实际使用CPU的时间                                        |
| CMD   | 该进程的名称或者对应的路径                                   |

~~~shell
ps aux
~~~

![image-20220513161431093](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131614220.png)

### df命令

作用：查看磁盘的剩余空间

~~~shell
df -h
~~~

![image-20220513160333262](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131603351.png)

### free命令

命令：free

作用：查看内存使用情况

![image-20220513160119835](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131601923.png)

### kill命令

命令：kill

作用：kill命令会向操作系统内核发送一个信号（多为终止信号）和目标进程的PID，然后系统内核根据收到信号类型，对指定进程进行相应的操作

语法：kill [信号] PID

| 信号 | 说明                     |
| ---- | ------------------------ |
| 9    | 杀死进程，即强制结束进程 |
| 15   | 正常结束进程             |

~~~shell
kill -9  623
kill -15 6235
~~~

### killall命令

命令：killall

语法：kill [信号] 进程名称

~~~shell
killall crond
killall httpd
~~~

### netstat命令

命令：netstat

作用：查看网络连接状态

语法：netstat -nlpt

| 选项 | 说明                                                       |
| ---- | ---------------------------------------------------------- |
| -t   | 只列出tcp协议连接                                          |
| -n   | 表示将地址从字母组合转化为ip地址，将协议转化为端口号来显示 |
| -l   | 表示过滤出‘state（状态）’列中其值为LISTEN的连接            |
| -p   | 表示显示发起连接的进程pid和进程名称                        |

![image-20220513161740175](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131617273.png)

### 进程优先级管理

#### 查看进程的优先级

PR优先级：数值越小优先级越高

NI优先级：数值越小优先级越高，可以人为修改

####  调整优先级

##### 使用top按r来调整

1. 运行top命令获取需要调整的进程信息（PID编号）

    ~~~shell
    top -bn 1
    ~~~

    ![image-20220513164117964](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131641106.png)

2. 运行top命令，然后按"r"，输入需要调整进程的PID

    ~~~shell
    top
    # 输入后按r
    # 输入需要调整的PID号
    ~~~

    ![image-20220513164357438](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131643556.png)

3. 根据提示，重置NICE值

    ![image-20220513164506644](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131645740.png)

4. 按q退出top模式，使用`top -p PID`编号，只查询某个进程

##### 命令行使用renice命令调整进程的优先级

基本语法：renice [NI优先级设置的数字] 想调整的进程ID

~~~shell
# 使用renice调整atd的优先级
renice -5 696
~~~

![image-20220513164859242](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205131648356.png)





