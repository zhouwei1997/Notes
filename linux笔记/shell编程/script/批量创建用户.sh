#!/bin/bash

# 批量新增5个新用户，用户名分别是u1到u5,并统一加一个新组class,统一密码诶123

# 判断class组是否存在
cut -d: -f1 /etc/group | grep -w class &>/dev/null
[ $? -ne 0 ] && grepuadd class
# 判断/rhome是否存在
[ -f /rhome ] && mv /rhome /rhome.bak
test !-f /rhome -a ! -d /rhome && mkdir /rhome
# 批量创建5个用户
for i in {1..5}; do
    useradd -d /rhome/u$i -G class u$i
    echo 123 | passwd --stdin u$i
done
