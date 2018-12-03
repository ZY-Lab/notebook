## 修改ssh登陆端口

#### 一、修改ssh端口号
进入系统后在root用户下  
键入vi /etc/ssh/sshd_config  
找到# port 22  
去掉前面的#号，在下面添加一行port 5432  
键入vi /etc/sysconfig/iptables  
在原来的22端口下，添加5432端口的防火墙规则  

查看端口范围
>sysctl -a|grep ip_local_port_range 

重启ssh服务
>service sshd restart

查看版本号
>lsb_release -a