##centos安装相关

创建/etc/yum.repos.d/mongodb-org-3.6.repo输入以下信息
```
[mongodb-org-3.6]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.6/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc
```
安装命令
>sudo yum install -y mongodb-org

默认配置文件位置/etc/mongod.conf

启动命令
>sudo service mongod start

设置开机自启动
>sudo chkconfig mongod on

停止命令
>sudo service mongod stop

重启命令
>sudo service mongod restart