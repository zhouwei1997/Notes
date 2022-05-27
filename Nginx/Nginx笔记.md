# Nginx

## 常见用法

- web服务器软件 http和httpd协议
- 代理服务器 反向代理
- 邮箱代理服务器 IMAP POP3 SMTP
- 负载均衡功能 LB loadblance

## Nginx架构特点

- 高可用  
    - 稳定性，master进程管理调度请求分发到哪一个worker ==> worker进程响应请求
- 热部署
    - 平滑升级
    - 快速重载配置
- 高并发
- 响应快
- 低消耗
- 分布式支持
    - 反向代理

## 编译参数

| 参数                           | 说明                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| --prefix                       | 编译安装到的软件目录                                         |
| --user                         | worker进程运行用户                                           |
| --group                        | worker进程运行用户组                                         |
| --with-http_ssl_module         | 支持https。需要pcel-devel依赖                                |
| --whth-http_stub_status_module | 基本状态信息显示，查看请求数、连接数                         |
| --with-http_realip_module      | 定义客户端地址和端口为header头信息，常用于反向代理后的真实ip获取 |

## 目录作用

| 目录 | 作用                                 |
| ---- | ------------------------------------ |
| conf | 配置文件                             |
| html | 网站默认目录                         |
| logs | 日志                                 |
| sbin | 可执行文件（软件的启动 停止 重启等） |

## 配置文件

`/usr/local/nginx/conf/nginx.conf`

~~~nginx
# nginx子进程的启动用户
#user  nobody;
# 子进程的个数，一般调整为cpu核数或者倍数
worker_processes  5;

# 错误日志定义
#error_log  logs/error.log;
#error_log  logs/error.log  notice;
#error_log  logs/error.log  info;

# 进程pid存储文件
#pid        logs/nginx.pid;

# 事件
events {
	# 每个子进程的连接数
    worker_connections  1024;
}

# http协议段
http {
	# 引用  文件扩展名和与文件类型映射表
    include       mime.types;
    # 默认文件类型
    default_type  application/octet-stream;

	# 访问access日志的格式
    #log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    #                  '$status $body_bytes_sent "$http_referer" '
    #                  '"$http_user_agent" "$http_x_forwarded_for"';

    #access_log  logs/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

	# 长链接超时时间 默认为秒
    #keepalive_timeout  0;  # 不过期
    keepalive_timeout  65;

	# gzip压缩
    #gzip  on;

    server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

        #error_page  404              /404.html;

        # redirect server error pages to the static page /50x.html
        #
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }

        # proxy the PHP scripts to Apache listening on 127.0.0.1:80
        #
        #location ~ \.php$ {
        #    proxy_pass   http://127.0.0.1;
        #}

        # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
        #
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}

        # deny access to .htaccess files, if Apache's document root
        # concurs with nginx's one
        #
        #location ~ /\.ht {
        #    deny  all;
        #}
    }


    # another virtual host using mix of IP-, name-, and port-based configuration
    #
    #server {
    #    listen       8000;
    #    listen       somename:8080;
    #    server_name  somename  alias  another.alias;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}


    # HTTPS server
    #
    #server {
    #    listen       443 ssl;
    #    server_name  localhost;

    #    ssl_certificate      cert.pem;
    #    ssl_certificate_key  cert.key;

    #    ssl_session_cache    shared:SSL:1m;
    #    ssl_session_timeout  5m;

    #    ssl_ciphers  HIGH:!aNULL:!MD5;
    #    ssl_prefer_server_ciphers  on;

    #    location / {
    #        root   html;
    #        index  index.html index.htm;
    #    }
    #}

}

~~~

## server配置

### server虚拟主机配置

一台web服务器，需要使用到多个网站部署，搭建vhost虚拟主机实现不同域名解析绑定到不同的目录

~~~nginx
# 基于http的web模块
server{
	# 监听端口
	listen 80
	# 配置虚拟机
	server_name shop.devops.com
	root html/tp5shop;
	location / {
		index index.php index.html index.htm;
	}
	location ~ \.php$ {
		fastcgi_pass 127.0.0.1:9000;
		fastcgi_index index.php;
		fastcgi_param SCRIPT_FILENAME  /scripts$fastcgi_script_name;
		include fastcgi_params;
	}
}
~~~

> 一般server虚拟主机配置有三类：
>
> 1、基于域名  将域名配置到server_name上
>
> 2、基于IP  将IP配置到server_name上
>
> 3、基于端口  将端口配置到listen上

## Gzip压缩

~~~nginx
# 配置到http段里面，使整个http服务都启用gzip压缩
# 开启gzip压缩
gzip on;
# http协议版本
gzip_http_version 1.0;
# IE浏览器不开启gzip压缩，IE6以下会出现乱码
gzip_disable 'MSIE[1-6].';
# 开启gzip文件格式
gzip_types image/jpeg image/jpg image/png text/plain text/css
~~~

## 客户端缓存

用于告知浏览器获取的信息是在某个区间时间段是有效的

~~~nginx
location ~ \.(js|css)${
	# 单位参数 d-->day H-->hour
	expires 1h;
}
# 在整个http段中生效，配置在http段里
expires 1h;
~~~



## 基于IP的访问控制

基于ngx_http_access_module模块，默认可以使用

>语法：
>
>deny ip   禁止ip访问
>
>allow ip   允许访问

~~~conf
location / {
    deny  192.168.1.1;
    allow 192.168.1.0/24;
    allow 10.1.1.0/16;
    allow 2001:0db8::/32;
    deny  all;
}
~~~



## 基于用户的访问控制

基于ngx_http_auth_basic_module模块，默认可用

> auth_basic           "提示信息"; 
>
> auth_basic_user_file conf/htpasswd;  # 加载用户名称和密码校验文件

~~~ng
location / {
    auth_basic           "closed site"; 
    auth_basic_user_file conf/passwd.db;
}
~~~

#### 配置实现

##### 创建用户名和密码存储文件

~~~shell
cd /usr/local/nginx/conf
# htpasswd如果不存在则使用 yum install -y httpd-tools安装
htpasswd -c ./passwd.db lnmp
# 输入密码并再次确认密码
# 查看passwd.db是否存在
~~~

##### 在配置文件中配置

~~~shell
vim /usr/local/nginx/conf/nginx.conf
~~~

## 目录列表显示

显示文件列表，或者需要做一个下载页面

~~~nginx
# 开启目录列表显示
autoindex on;
# index  当index默认找不到时，才会使用目录列表
index index;
~~~

> 如果目录中没有配置默认index访问项，而autoindex又没有开启，不能够查看访问目录就会403错误

## 反向代理

![image-20220526174104849](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205261741927.png)

特点：用户无感知，反向代理服务器是和真实访问的服务器在一起的，有关联的

作用：

​		1、根据实际业务需求，分发代理页面到不同的解释器

​		2、可以隐藏真实服务器路径

### 配置反向代理

1、安装httpd，修改端口为8080

~~~shell
yum install -y httpd
vim /etc/httpd/conf/httpd.conf
~~~

![image-20220526213702170](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205262137235.png)

2、配置nginx代理

~~~nginx
location / {
	proxy_pass http://192.168.31.105:8080
}
~~~

![image-20220526214147802](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205262141862.png)

## location

### 匹配规则

![image-20220526220302051](https://raw.githubusercontent.com/zhouwei1997/Image/master/202205262203171.png)

#### = 精准匹配

~~~nginx
location = / {
  # 规则
}

# 匹配到 http://www.example.com/这类请求
~~~

#### ~ 大小写敏感

~~~nginx
location ~ /Example/ {
    # 规则
}

~~~

> http://www.example.com/Example/   成功
>
> http://www.example.com/example/   失败

#### ~* 大小写忽略

~~~nginx
location ~* /Example/ {
    # 规则
}
~~~

> http://www.example.com/Example/   成功
>
> http://www.example.com/example/   成功

#### ^~ 只匹配到以uri开头

~~~shell
location ^~ /img/ {
    # 规则
}
~~~

>请求实例
>
>以/img/开头的请求，都会匹配上
>
>http://www.example.com/img/a.jpg   成功
>
>http://www.example.com/img/b.mp4   成功
>
>http://www.example.com/bing/a.jpg   失败
>
>http://www.example.com/Img/a.jpg   失败

如果路径是资源文件，会优先获取资源文件

#### / 通用选项

~~~nginx
location / {
  # 规则
}
~~~

其他匹配都不成功，则匹配此项

>location匹配优先级
>
>(location =) > (location 完整路径) > (location ^~路径 ) > (location ~,~ 正则表顺序) > (location  部分路径) > (/)

### 匹配跳转

@+name

在nginx内部进行跳转

~~~nginx
# 以/img/开头的请求，如果链接的状态是404，则会匹配到@img_err这条规则上
location /img/ {
    error_page 404 = @img_err;
}

location @img_err {
    # 规则
    return 503；
}
~~~

## URL重写

> `ngx_http_rewrite_module`模块用于使用PCRE正则表达式更改请求URI，返回重定向，以及有条件的选择配置

### return

该命令用于结束规则的执行并返回状态码给客户端

~~~nginx
# 可以匹配到server location if中，推荐配置到location中
return 403;
~~~

### rewrite

rewrite匹配到请求URI，重写到新的URI

>rewrite语法匹配到，替换为其他内容
>
>语法 rewrite 匹配内容 替代内容 标记

| 标记      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| last      | 本条规则匹配完成后，继续向下匹配新的location URI规则，客户端URL地址不会发生跳转 |
| break     | 本条规则匹配完成即终止，不在匹配后面任何规则，客户端URL地址不会发生跳转 |
| redirect  | 返回302临时重定向，浏览器地址会显示跳转后的URL地址           |
| permanent | 返回301永久重定向，浏览器地址会显示跳转后的URL地址           |

> 匹配规则：多条rewrite，从上到下匹配，匹配到之后就不在匹配其他的rewrite规则