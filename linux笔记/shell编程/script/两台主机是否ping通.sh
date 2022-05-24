#!/bin/bash

# ping两台主机是否能ping 通
# 1.使用ping -c命令实现
# 2.根据命令执行结果状态来判断是否通
# 3.根据逻辑和结构来编写脚本

# 获取远程主机的IP地址
read -p "请输入远程主机的IP：" IP
# 使用ping命令判断是否和远程主机互通
ping -c1 $IP &>/dev/null
if [ $? -eq 0 ]; then
    echo "当前主机和远程主机$IP互通"
else
    echo "当前主机和远程主机$IP不互通"
fi
