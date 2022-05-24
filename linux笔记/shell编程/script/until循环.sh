#!/bin/bash

# 使用until语句批量创建10个用户，要求stu1-stu5用户的UID分别是1001-1005；stu6-stu10用户的家目录分别在/rhome/stu6-stu10

i=1
until [ $i -gt 10 ]; do
    if [ $i -le 5 ]; then
        useradd -u 100$i stu$i && echo 123 | passwd --stdin stu$i
    else
        [ ! -d /rhome ] && mkdir /rhome
        useradd -d /rhome/stu$i && cho 123 | passwd --stdin stu$i
    fi
    let i++
done
