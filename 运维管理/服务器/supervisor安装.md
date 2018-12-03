## supervisor安装

> apt-get install supervisor

####修改配置文件supervisord.conf
    [inet_http_server]         ; inet (TCP) server disabled by default
    port=127.0.0.1:8000        ; (ip_address:port specifier, *:port for all iface)
    username=username              ; (default is no username (open server))
    password=password               ; (default is no password (open server))

####设置为开机启动项
> chkconfig supervisord on
最新命令：
> sysstemctl start  supervisord.service 