# Redis

[TOC]

## 核心配置文件

- 绑定ip：如果需要远程访问，可将此行注释，或者绑定一个真实的ip

    ~~~shell
    bind 127.0.0.1
    ~~~

    ![image-20220716175148967](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207161751182.png)

- 端口，默认端口6379

    ~~~shell
    port 6379
    ~~~

    ![image-20220716175239267](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207161752339.png)

- 是否以守护进程运行

    - 如果以守护进程运行，则不会在命令行阻塞，类似于服务
    - 如果以非守护进程运行，则在当前终端被阻塞
    - 设置为yes表示守护进程，设置为no为非守护进程

    ~~~shell
    daemonize yes
    ~~~

- 数据文件

    ~~~shell
    dbfilename dump.rdb
    ~~~

    ![image-20220716175629847](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207161756960.png)

## 数据结构

- Redis是key-value的数据结构，每条数据都是一个键值对
- 键的类型是字符串
- 键不能重复

### string

String类型的可以接受如何格式的数据。在Redis中字符串类型的Value最多可以容纳的数据长度是512MB

#### 保存

- 设置键值

    ~~~Redis
    set key value
    
    # 设置key
    set name itcast
    # 查看key
    get name
    # 删除key
    del name
    ~~~

    ![image-20220716180557260](https://raw.githubusercontent.com/zhouwei1997/Image/master/202207161805314.png)

- 设置键值及过期时间，以秒为单位

    ~~~shell
    setex key seconds value
    setex school 10 zhangsan
    ~~~

### hash

- hash用于存储对象，对象的结构为属性、值

- 值的类型为String

#### 增加、修改

- 设置单个属性
    - hset key field value
        - hset user name itheima
- 获取单个属性
    - hget key field
        - hget user name
- 设置多个属性
    - hmset key field1value1 field2 value2...
        - hmset person name zhangsan age 14 address beijing
- 获取多个属性的值
    - hmget field1 field2...
        - hmget person name age address
- 获取所有属性的值
    - hvals key
        - hvals person

#### 删除

- 删除某一个field（属性的值也会被一起删除）
    - hdel key field
        - hdel person name

### list

- list的元素类型为string
- 按照插入顺序排序

#### 增加

- 从左侧插入
    - lpush key value1 value2...
        - lpush a1 a b c
- 从右侧插入
    - rpush key value1 value2...
        - rpush a1 d e f

### set



### zset

