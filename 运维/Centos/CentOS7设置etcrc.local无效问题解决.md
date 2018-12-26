# CentOS7设置etcrc.local无效问题解决

安装centos7以后按照以往习惯修改rc.local添加开机启动命令，但重启后发现无效，再次重启发现依然如故
检查系统rc.local服务运行情况 
1 systemctl | grep "rc.local"
2 # rc-local.service
loaded active running /etc/rc.d/rc.local Compatibility 
发现运行正常
随后查看rc.local文件
vim /etc/rc.local
发现这么一句话
Please note that you must run 'chmod +x /etc/rc.d/rc.local' to ensure
由于/etc/rc.local是/etc/rc.d/rc.local的软连接，所以必须确保/etc/rc.local和/etc/rc.d/rc.local都有x权限(可执行)
执行命令
chmod +x /etc/rc.d/rc.local
重启，一切正常，问题解决。