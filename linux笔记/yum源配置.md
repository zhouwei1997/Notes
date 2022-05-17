# yum源配置

[TOC]

## yum源概述

yum源就是一个软件包管理器

![image-20220516162100258](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205161621333.png)

### 优点

1. 能够解决软件包之间的依赖关系

## 本地yum源备份

1. 切换到`/etc/yum.repos.d`

    ~~~shell
    cd /etc/yum.repos.d/
    ~~~

2. 对所有的仓库文件进行备份

    ~~~shell
    tar -zcf repo.tar.gz *.repo
    ~~~

3. 删除所有以.repo结尾的仓库文件

    ~~~shell
    rm -rf *.repo
    ~~~

## 本地yum源配置

1. 挂载iso光盘文件

~~~shell
rm -rf /mnt
mount -o ro /dev/sr0 /mnt
~~~

![image-20220516160141584](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205161601665.png)

2. 将光盘挂载添加到开机启动文件中

~~~shell
chmod +x /etc/rc.local
echo 'mount -o ro /dev/sr0 /mnt' >> /etc/rc.local
~~~

![image-20220516160457254](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205161604333.png)

3. 编写本地yum仓库文件

~~~shell
cd /etc/yum.repos.d/
# 创建一个以*.repo的文件
touch local.repo
~~~

>yum仓库的标准格式
>
>[仓库名称]   名称任意，一个文件中可以拥有多个标识
>
>name= 仓库名称
>
>baseurl= 仓库的路径，支持多种格式，file://本地路径，ftp://，http://或者https://
>
>gpgcheck=gpg秘钥，值可以是0（代表不检测），1（代表检测，如果是1，下方还需要定义一个gpakey=秘钥连接）
>
>enabled=是否启用当前仓库，值可以是0，也可以是1，默认为1，代表启用仓库

~~~repo
[local]
name=local yum
baseurl=file:///mnt
gpgcheck=0
enable=1
~~~

4. 清理缓存

~~~shell
# 查看当前的yum查看
[local]
yum repolist all
~~~

![image-20220516161644012](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205161616089.png)
        
~~~shell
# 清除缓存
yum clean all
# 新建缓存文件
yum makecache
~~~


## 网络yum源配置

如果配置的是外网源，当前主机必须能访问到互联网

### 修改配置文件指向网络仓库

#### 特定软件网络源

~~~shell
# vim /etc/yum.repos.d/nginx.repo

[nginx]
name= nginx repo
baseurl=http://nginx.org/packages/centos/7/x86_64/
gpgcheck=0
enabled=1

# 说明
baseurl=http://nginx.org/packages/centos/7/$basearch/
$basearch 表示当前系统cpu架构，如果系统是32位会找32位软件包，如果是64位会找64位软件包
~~~

## EPEL源配置

EPEL是对官网源的一个扩展

~~~shell
yum install -y epel-release -y
~~~

## 自建yum源仓库

1. 缓存安装软件包

    ~~~shell
    # 修改配置文件/etc/yum.conf
    
    [main]
    cachedir=/var/cache/yum/$basearch/$releasever # 定义软件包的位置
    keepcache=0  # 1开启缓存 0关闭缓存
    ~~~

    ![image-20220517134720200](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205171347309.png)

2. 把软件及依赖全部下载到某个路径下

    ~~~shell
    yum install --downloadonly --downloaddir=保存路径 软件名称
    ~~~

    ~~~shell
    # 下载samba软件及依赖软件
    mkdir /home/soft
    yum install --downloadonly --downloaddir=/home/soft samba
    ~~~

    ![image-20220517135219229](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205171352296.png)

3. 打包软件所在目录生成repodata目录

    ~~~shell
    yum install -y createrepo
    createrepo /home/soft
    ~~~

    ![image-20220517135448567](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205171354663.png)

4. 关闭本地仓库和所有网络仓库，配置自己的创建的yum仓库

    ~~~shell
    # 根据配置，打开本地和网络源配置文件，将enabled=1改为enabled=0
    # 创建自建源配置文件
    vim /etc/yum.repos.d/myself.repo
    
    [myself]
    name=myself yum
    enabled=1
    baseurl=file:///home/soft
    gpgcheck=0
    ~~~

    













