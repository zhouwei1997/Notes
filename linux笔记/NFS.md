# NFS

[TOC]

## 环境准备

> 端口占用：TCP 111和2049

| 角色      | IP             |
| --------- | -------------- |
| NFS服务端 | 192.168.31.120 |
| NFS客户端 | 192.168.31.125 |

## NFS服务端

1. 安装NFS服务器

    ~~~shell
    yum install -y rpcbind nfs-utils
    ~~~

2. 关闭防火墙和selinux

    ~~~shell 
    systemctl stop firewalld
    setenforce 0
    ~~~
   
3. 创建共享目录
   
   ~~~shell
   mkdir /home/data
   chmod -Rf 777 /home/data
   ~~~


4. 修改NFS的配置文件

    ~~~shell
    vim /etc/exports
    
    /home/data 192.168.31.0/24(rw,sync,root_squash)
    ~~~

    | 参数           | 说明                                                         |
    | -------------- | ------------------------------------------------------------ |
    | ro             | 只读                                                         |
    | rw             | 读写                                                         |
    | root_squash    | 当NFS客户端以root管理员访问时，映射为NFS服务器的匿名用户     |
    | no_root_squash | 当NFS客户端以root管理员访问时，映射为NFS服务器的root用户     |
    | all_squash     | 无论NFS客户端使用什么账户访问，均映射为NFS服务器的匿名用户   |
    | sync           | 同时将数据写入到内存与硬盘中，保证不丢失数据                 |
    | async          | 优先将数据保存到内存，然后再写入硬盘；这样效率更高，但可能会丢失数据 |
    
    ![image-20220518163843707](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205181638763.png)

5. 启动nfs服务

    ~~~shell
    systemctl start rpcbind
    systemctl enable rpcbind 
    systemctl start nfs-server
    systemctl enable nfs-server
    ~~~

6. 查看是否有节点

    ~~~shell
    showmount -e 192.168.31.120
    ~~~

## NFS客户端

1. 安装NFS服务器

    ~~~shell
    yum install -y rpcbind  nfs-utils
    ~~~

2. 关闭防火墙和selinux

    ~~~shell 
    systemctl stop firewalld
    setenforce 0
    ~~~

3. 启动rpcbind

    ~~~shell 
    systemctl enable rpcbind.service
    systemctl start rpcbind.service
    ~~~

4. 检查是否能找到NFS-Server

    ~~~shell
    showmount -e 192.168.31.120
    ~~~

    ![image-20220518164632223](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205181646283.png)

5. 挂载nfs

    ~~~shell
    mount -t nfs 192.168.31.120:/home/data /home/test
    ~~~

6. 开机自动挂载

    ~~~shell
    # 在/etc/fstab中添加挂载信息
    192.168.31.120:/home/data   /home/test      nfs  defaults 0  0
    
    # 在rc.local中添加（rc.local需要有可执行权限）
    mount -t nfs 192.168.31.120:/home/data /home/test
    ~~~

    
