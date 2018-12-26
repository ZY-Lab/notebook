# 初始化相关

## 开启root用户ssh登录  

> vi /etc/ssh/sshd_config

```bash
PermitRootLogin yes
```

## 设置固定IP

> vim /etc/network/interfaces

```bash
# iface enp0s3 inet dhcp  
iface enp0s3 inet static  
address 192.168.3.202  
netmask 255.255.255.0  
gateway 192.168.3.1  
```

> service networking restart