# Nginx平滑升级

> ①、旧的版本不停
>
> ②、新的版本可以启动
>
> ③、旧的和新的同时提供服务，旧的请求完成之后，就停掉旧进程
>
> -USR2  平滑启动一个进程（平滑升级）
>
> -WINCH  关闭子进程
>
> -QUIT  关闭主进程

①、安装编译新版本

~~~shell
tar zxvf nginx-1.16.1.tar.gz
cd nginx-1.16.1
./configure --prefix=/usr/local/nginx --user=root --group=root --with-http_ssl_module --with-http_stub_status_module --with-http_realip_module
make -j && make install
~~~

升级新版本后，需要把软件的安装路径，指定到就版本上

> 以上操作完成后，会把原来的旧版本备份为nginx.old

![image-20220526141610819](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205261416912.png)

②、新旧版本同时运行

~~~shell
ps aux | grep nginx 
kill -USR2 主进程号
~~~

![image-20220526141807265](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205261418332.png)

③、停掉旧进程

查看就的主进程号，并使用kill -WINCH关闭子进程，在关闭旧的主进程

~~~shell
kill -WINCH 旧的子进程号
kill -QUIT 旧的主进程号
~~~

![image-20220526142030429](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205261420480.png)