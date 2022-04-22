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

##### 删除





## Linux用户管理

## 管道命令详解

## Linux网络配置与远程管理

## 权限管理

## 系统服务

## Linux进程检测与进程管理

## 阿里云与开源项目上线部署实战





