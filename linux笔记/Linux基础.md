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



## 管道命令详解



## Linux网络配置与远程管理



## 权限管理



## 系统服务



## Linux进程检测与进程管理



## 阿里云与开源项目上线部署实战





