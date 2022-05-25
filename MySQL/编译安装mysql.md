# 编译安装MySQL

## 相关参数介绍

### 编译参数的说明

| 参数                            | 说明                       |
| ------------------------------- | -------------------------- |
| -DCMAKE_INSTALL_PREFIX          | 安装到的软件目录           |
| -DMYSQL_DATADIR                 | 数据文件存储的路径         |
| -DSYSCONFDIR                    | 配置文件路径（my.cnf）     |
| -DENABLED_LOCAL_INFILE=1        | 使用localmysql客户端的配置 |
| -DWITH_PARTITION_STORAGE_ENGINE | 使用mysql支持分表          |
| -DEXTRA_CHARSETS                | 安装支持的字符集           |
| -DDEFAULT_CHARSET               | 默认字符集使用，默认utf-8  |
| -DDEFAULT_COLLATION             | 连接字符集                 |
| -DWITH_SSL                      | 开启mysql的ssl使用         |


### 初始化参数

| 参数      | 说明             |
| --------- | ---------------- |
| --basedir | 安装到的软件目录 |
| --datadir | 数据文件存储路径 |
| --user    | mysql使用的用户  |





