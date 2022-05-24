#!/bin/bash

# 写一个30秒同步一次时间，向同步时间服务器10.1.1.250的脚本，如果同步失败，则进行邮件告警，每次失败都告警。同步成功，夜景下邮件通知。但是成功100次才通知一次

# 每30s同步一次时间，该脚本是一个死循环
# 同步失败，发送邮件
# 同步成功100次才发送已经邮件

count=0
ntp_server=10.1.1.250
while true; do
    rdate -s $ntp_server &>/dev/null
    if [ $? -ne 0 ]; then
        echo "system date failed" | mail -s 'check system date' root@localhost
    else
        let count++
        if [ $(($count % 100)) -eq 0 ]; then
            echo "system date successful" | mail -s 'check system date' root@localhost && count=0
        fi
    fi
    sleep 30
done
