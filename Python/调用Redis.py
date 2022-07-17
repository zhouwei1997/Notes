# -*- coding:utf-8 -*-
"""
# @author ZhouWei
# @date  2022/7/17
# @file  调用Redis.py
# @description 调用Redis模块
"""
# 导入Redis模块
import redis

if __name__ == '__main__':
    try:
        # 创建Redis的实例
        rs = redis.Redis(host='127.0.0.1', port=6379, db=1, password='zhouwei1997', socket_timeout=3000)
    except Exception as e:
        print(e)
    # 操作String
    # 添加key
    result = rs.set('name', 'zhangsan')
    print(result)

    # 获取
    name = rs.get('name')
    print(name)
