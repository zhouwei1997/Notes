# 配置https

~~~nginx
server{
    listen  443 ssl;
    # 绑定好的域名
    server_name localhost;
    
    # 指定证书相关位置
    ssl_certificate cert.pem;
    ssl_certificate_key cert.key;
    
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout 5m;
    
    ssl_ciphers  HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers  on;
    
    location / {
        root html;
        index index.html index.htm;
    } 
}
~~~



~~~nginx
# http跳转到https
server {
    listen 80;
    server_name web1.heimadevops.top;
    rewrite / https://web1.heimadevops.top permanent;
}
~~~

