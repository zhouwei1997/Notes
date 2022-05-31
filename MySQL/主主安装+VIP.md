# MySQL主主安装

mysql版本：mysql-5.7.27-1.el7.x86_64.rpm-bundle.tar

| 服务器IP       | 端口 | 角色     |
| -------------- | ---- | -------- |
| 192.168.31.105 | 3306 | master A |
| 192.168.31.115 | 3306 | master B |
| 192.168.31.160 | 3306 | VIP      |

## 安装

①、卸载系统的MariaDB

~~~shell
for i in `rpm -qa|grep -i -e mysql -e mariadb`;do rpm -e $i --nodeps; done
rm -rf /var/lib/mysql/*
rm -rf /var/log/mysqld.log
~~~

②、解压mysql 

~~~shell 
tar -xf mysql-5.7.27-1.el7.x86_64.rpm-bundle.tar
~~~

③、安装mysql

~~~shell 
for i in `ls mysql-community*`;do rpm -ivh $i --nodeps; done
~~~

④、修改配置文件

~~~mysql
[mysqld]
# 设置字符集
character_set_server=utf8mb4
collation-server=utf8mb4_unicode_ci

# 登录不验证密码
#skip-grant-tables

datadir=/var/lib/mysql
socket=/var/lib/mysql/mysql.sock

symbolic-links=0

log-error=/var/log/mysqld.log
pid-file=/var/lib/mysql/mysqld.pid
init_connect='SET NAMES utf8mb4'
max_allowed_packet=100M


[client]
default-character-set=utf8mb4
[mysql]
default-character-set=utf8mb4
~~~

⑤、启动mysql并设置为开机自启

~~~shell
systemctl start mysqld
systemctl enable mysqld
~~~

⑥、修改密码并新建用户

~~~shell
# 修改密码
pass=`grep 'temporary password' /var/log/mysqld.log|awk '{print $11}'`
mysql --connect-expired-password -uroot -p$pass

# 修改root用户的密码
alter user 'root'@'localhost' identified by 'Hcicloud^135';
# 设置root可以远程登录
use mysql;
update user set host = '%' where user = 'root';
# 新建hcicloud用户并赋权
CREATE USER 'hcicloud'@'%' IDENTIFIED BY 'Hcicloud^135';
GRANT ALL PRIVILEGES ON *.* TO 'hcicloud'@'%' IDENTIFIED BY 'Hcicloud^135' WITH GRANT OPTION;
flush privileges;
# 退出
quit;
~~~

## master_A配置

①、修改配置文件，在`my.cnf`文件中添加

~~~mysql
server-id=1                             #server的唯一标识
auto_increment_offset=1                  #自增id起始值
auto_increment_increment=2                #每次自增数字

log-bin = mysql-bin                           #打开二进制功能,MASTER主服务器必须打开此项
max_binlog_size=1024M                          #binlog单文件最大值

#忽略不同步主从的数据库
replicate-ignore-db = mysql                    
replicate-ignore-db = information_schema
replicate-ignore-db = performance_schema
replicate-ignore-db = sys
~~~

![image-20220531101933202](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311019217.png)

②、重启mysql

~~~shell
systemctl restart mysqld
~~~

## master_B配置

~~~mysql
server-id=2                             #server的唯一标识
auto_increment_offset=2                  #自增id起始值
auto_increment_increment=2                #每次自增数字

log-bin = mysql-bin                           #打开二进制功能,MASTER主服务器必须打开此项
max_binlog_size=1024M                          #binlog单文件最大值

#忽略不同步主从的数据库
replicate-ignore-db = mysql                    
replicate-ignore-db = information_schema
replicate-ignore-db = performance_schema
replicate-ignore-db = sys
~~~

![image-20220531102050699](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311020769.png)

②、重启mysql

~~~shell
systemctl restart mysqld
~~~

## 主从配置

### 添加主从账户

①、master_A

~~~mysql
GRANT replication SLAVE ON *.* TO 'repl' @'192.168.31.115' IDENTIFIED BY 'Hcicloud^123';
~~~

![image-20220531102450357](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311024428.png)

②、master_B

~~~mysql
GRANT replication SLAVE ON *.* TO 'repl' @'192.168.31.105' IDENTIFIED BY 'Hcicloud^123';
~~~

![image-20220531102515443](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311025503.png)

###  查看主库的状态

①、master_A

~~~mysql
SHOW MASTER STATUS;
~~~

![image-20220531102640718](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311026785.png)

②、master_B

~~~mysql
SHOW MASTER STATUS;
~~~

![image-20220531102801862](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311028924.png)

### 配置主从同步

①、master_A

~~~mysql
CHANGE MASTER TO master_host = '192.168.31.115',
master_port = 3306,
master_user = 'repl',
master_password = 'Hcicloud^123',
master_log_file = 'mysql-bin.000001',
master_log_pos = 154;

START SLAVE;

SHOW SLAVE STATUS\G;
~~~

![image-20220531104540523](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205311045615.png)

②、master_B

~~~mysq
CHANGE MASTER TO master_host = '192.168.31.105',
master_port = 3306,
master_user = 'repl',
master_password = 'Hcicloud^123',
master_log_file = 'mysql-bin.000001',
master_log_pos = 1816;

START SLAVE;

SHOW SLAVE STATUS\G;
~~~

