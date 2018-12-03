## nginx反向代理端口获取
####Nginx默认反向后的端口为80，因此存在被代理后的端口为80的问题，这就导致访问出错。主要原因在Nginx的配置文件的host配置时没有设置响应的端口，设置$host:$server_port解决。
    location /{
                #root   html;
                #index  index.html index.htm;
                proxy_pass http://server;
                proxy_set_header Host $host:$server_port;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }