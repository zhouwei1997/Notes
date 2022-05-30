#!/bin/bash
nginx_status=$(ps -C nginx --no-header | wc -l)
if [ $nginx_status -eq 0 ];then
	systemctl stop keepalived
fi