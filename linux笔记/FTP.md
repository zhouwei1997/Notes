# FTP

[TOC]

## 概述

FTP（File Transfer Protocol）是一种应用广泛的互联网传输协议

![image-20220517231946906](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205172321147.png)



- 主要用于互联网中文件的双向传输（上传/下载）、文件共享

- 跨平台使用

- FTP是C/S架构，拥有一个客户端和服务端，使用TCP协议作为底层传输协议，提供可靠的数据传输

- FTP默认使用21号端口（命令端口）和20号端口（数据端口）

## FTP的两种工作模式

### 主动模式

![image-20220517232433903](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205172324999.png)

1. 客户端打开大于1023的随机命令端口和大于1023的随机数据端口向服务的21端口发起请求
2. 服务端的21命令端口响应客户端的随机命令端口
3. 服务端的20号端口主动请求连接客户端的随机数据端口
4. 客户端的随机数据端口进行确认

### 被动模式

<img src="https://raw.githubusercontent.com/zhouwei1997/Image/master/202205172331025.png" alt="image-20220517233136936" style="zoom:80%;" />


1. 客户端打开大于1023的随机命令端口和大于1023的随机数据端口向服务的21号端口发起请求
1. 服务端的21号端口响应客户端的随机命令端口
1. 客户端主动连接服务端打开的大于1023的随机数据端口
1. 服务端进行确认

## FTP搭建

1. 关闭防火墙和SELinux

    ~~~shell
    systemctl stop firewalld
    systemctl disable firewalld
    setenforce 0
    ~~~

    修改`/etc/selinux/config`文件中的`SELINUX=disabled`

    ![image-20220517234523659](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205172345745.png)

2. 配置yum源

    ~~~shell 
    mount /dev/sr0 /mnt
    yum clean all
    yum makecache
    ~~~

3. 安装vsftpd软件

    ~~~shell
    yum install -y vsftpd
    ~~~

4. 启动ftp服务并加入开机启动项中

    ~~~shell
    systemctl start vsftpd
    systemctl enable vsftpd
    ~~~

5. 测试ftp是否安装成功

    ![image-20220517235113261](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205172351332.png)

## FTP配置文件

| 配置文件                  | 说明     |
| ------------------------- | -------- |
| `/etc/rc.d/init.d/vsftpd` | 启动脚本 |
|  `/etc/vsftpd` |       配置文件的目录   |
|  `/etc/vsftpd/ftpusers` |       用户列表文件，黑名单  |
|  `/etc/vsftpd/user_list` |  用户列表文件，可黑可白（默认是黑名单） |
|  `/etc/vsftpd/vsftpd.conf` | 配置文件|
|  `/usr/sbin/vsftpd` |     程序本身（二进制命令）   |
|  `/var/ftp` |       匿名用户的默认数据根目录|
|  `/var/ftp/pub` |       匿名用户的扩展数据目录|

### vsftpd.conf配置文件

| 配置项 | 说明 | 备注 |
| ------ | ---- | ------ |
| anonymous_enable=YES|支持匿名用户访问 |  |
| local_enable=YES | 非匿名用户 |  |
|write_enable=YES| 写总开关 | YES：普通用户可以上传文件 |
|local_umask=022 | 反掩码，file:644  dir:755 |  |
|dirmessage_enable=YES | 启用消息功能 |  |
|xferlog_enable=YES | 开启或启用xferlog日志 |  |
|connect_from_port_20=YES | 支持主动模式（默认被动模式） |  |
|xferlog_std_format=YES | xferlog日志格式 |  |
|listen=NO | ftp服务独立模式下的监听 | YES：在启动后自动占用计算机的资源（21号端口） |
|listen_ipv6=YES | |  |
|pam_service_name=vsftpd  | 指定认证文件 |  |
|userlist_enable=YES | 启用用户列表 |  |
|tcp_wrappers=YES | 支持tcp_wrapper功能 | ftp限速操作 |



