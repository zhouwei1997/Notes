# keepalived+nginx高可用

## 安装keepalived

~~~shell 
# 下载最新版本并安装
cd /usr/local/src
wget http://www.keepalived.org/software/keepalived-2.0.7.tar.gz
tar zxvf keepalived-2.0.7.tar.gz
cd keepalived-2.0.7
./configure --prefix=/usr/local/keepalived
make && make install
~~~

~~~shell
# keepalived启动脚本变量引用文件，默认文件路径是/etc/sysconfig/，也可以不做软链接，直接修改启动脚本中文件路径即可（安装目录下）
cp /usr/local/keepalived/etc/sysconfig/keepalived  /etc/sysconfig/keepalived 
 
# 将keepalived主程序加入到环境变量（安装目录下）
cp /usr/local/keepalived/sbin/keepalived /usr/sbin/keepalived
 
# keepalived启动脚本（源码目录下），放到/etc/init.d/目录下就可以使用service命令便捷调用
cp /usr/local/src/keepalived-2.0.7/keepalived/etc/init.d/keepalived  /etc/init.d/keepalived
 
# 将配置文件放到默认路径下
mkdir /etc/keepalived
cp /usr/local/keepalived/etc/keepalived/keepalived.conf /etc/keepalived/keepalived.conf
~~~

~~~shell 
# 添加到系统服务中
chkconfig --add keepalived
# 设置开机自启动
chkconfig keepalived on
# 查看是否加入成功
systemctl list-unit-files | grep keepalived
systemctl start|stop|restart|status keepalived
~~~

| 文件或目录                      | 作用           |
| ------------------------------- | -------------- |
| `/etc/keeplived/keeplived.conf` | 生效的配置文件 |
| `/etc/init.d/keeplived`         | 服务器管理脚本 |
| `/var/logs/message`             | 日志信息       |

## 配置keepalived

### 配置文件说明

~~~conf
! Configuration File for keepalived

# 发送邮件的配置
global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

# vrrp协议的配置
vrrp_instance VI_1 {
	# 工作模式
    state MASTER
    # 监听的网卡
    interface eth0
    # 虚拟路由id，需要和备服务器一致
    virtual_router_id 51
    # 权重  优先级
    priority 100
    # vrrp包的发送周期  1s
    advert_int 1
    # 权限验证
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    # 需要绑定切换的VIP
    virtual_ipaddress {
        192.168.200.16
        192.168.200.17
        192.168.200.18
    }
}

virtual_server 192.168.200.100 443 {
    delay_loop 6
    lb_algo rr
    lb_kind NAT
    persistence_timeout 50
    protocol TCP

    real_server 192.168.201.100 443 {
        weight 1
        SSL_GET {
            url {
              path /
              digest ff20ad2481f97b1754ef3e12ecd3a9cc
            }
            url {
              path /mrtg/
              digest 9b3a0c85a887a256d6939da88aabd8cd
            }
            connect_timeout 3
            retry 3
            delay_before_retry 3
        }
    }
}

virtual_server 10.10.10.2 1358 {
    delay_loop 6
    lb_algo rr
    lb_kind NAT
    persistence_timeout 50
    protocol TCP

    sorry_server 192.168.200.200 1358

    real_server 192.168.200.2 1358 {
        weight 1
        HTTP_GET {
            url {
              path /testurl/test.jsp
              digest 640205b7b0fc66c1ea91c463fac6334d
            }
            url {
              path /testurl2/test.jsp
              digest 640205b7b0fc66c1ea91c463fac6334d
            }
            url {
              path /testurl3/test.jsp
              digest 640205b7b0fc66c1ea91c463fac6334d
            }
            connect_timeout 3
            retry 3
            delay_before_retry 3
        }
    }

    real_server 192.168.200.3 1358 {
        weight 1
        HTTP_GET {
            url {
              path /testurl/test.jsp
              digest 640205b7b0fc66c1ea91c463fac6334c
            }
            url {
              path /testurl2/test.jsp
              digest 640205b7b0fc66c1ea91c463fac6334c
            }
            connect_timeout 3
            retry 3
            delay_before_retry 3
        }
    }
}
~~~



### 备份主备服务器的配置文件

~~~shell 
cd /etc/keepalived
cp keepalived.conf keepalived.conf_bak
~~~

### 主服务器

~~~conf
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

# 检测nginx进程是否存在
vrrp_script chk_nginx {
	script "/etc/keepalived/check_nginx.sh" ## 检测 nginx 状态的脚本路径
	interval 2 ## 检测时间间隔
	weight -20 ## 如果条件成立，权重-20
}

# vrrp协议的配置
vrrp_instance VI_1 {
    state MASTER
    interface ens33
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    # 需要绑定切换的VIP
    virtual_ipaddress {
        192.168.31.160/24
    }
    #脚本引用
     track_script { 
           chk_nginx 
    } 
}
~~~

### 备服务器

~~~conf
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

# 检测nginx进程是否存在
vrrp_script chk_nginx {
	script "/etc/keepalived/check_nginx.sh" ## 检测 nginx 状态的脚本路径
	interval 2 ## 检测时间间隔
	weight -20 ## 如果条件成立，权重-20
}

# vrrp协议的配置
vrrp_instance VI_1 {
    state BACKUP
    interface ens33
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    # 需要绑定切换的VIP
    virtual_ipaddress {
        192.168.31.160/24
    }
    #脚本引用
     track_script { 
           chk_nginx 
    } 
}
~~~

### 编写nginx的检测脚本

当检测nginx服务不可用时，则关闭当前主机的keepalived

在keepalive的配置文件中调用检测脚本

~~~shell
vim /etc/keepalived/check_nginx.sh

#!/bin/bash
nginx_status=$(ps -C nginx --no-header | wc -l)
if [ $nginx_status -eq 0 ];then
	systemctl stop keepalived
fi
~~~

给测试脚本执行权限

~~~shell
chmod a+x /etc/keepalived/check_nginx.sh
~~~

## 问题排查

### 两台都出现VIP的情况

两台同时出现vip的情况，检查服务器是否关闭。如果防火墙没有关闭，或者不能关闭防火墙的情况，则需要开放112端口

~~~shell
systemctl status firewalld

firewall-cmd --zone=public --add-port=122/tcp --permanent
firewall-cmd --add-rich-rule="rule family="ipv4" source address="192.168.31.105" port protocol="tcp" port="122" accept"  --permanent
firewall-cmd --reload
~~~

### keepalived中检测脚本不生效

1、手动执行nginx的脚本，查看是否生效

2、关不selinux

~~~shell
# 临时关闭
setenforce 0
# 永久关闭
sed -i "s/^SELINUX=.*/SELINUX=disabled/g" /etc/selinux/config
~~~

3、在虚拟ip下添加检测脚本

~~~shell
#脚本引用
track_script { 
     chk_nginx   # 与vrrp_script 名称一致
} 
~~~

![image-20220527171436536](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205271714641.png)

### VIP无法访问页面

需要将keepalived.conf中注释掉vrrp_strict

![image-20220527174213327](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205271742398.png)