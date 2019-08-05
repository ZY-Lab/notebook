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

## 密钥登陆配置
```
密钥登录步骤（免密码登录）
ssh登录提供两种认证方式：口令(密码)认证方式和密钥认证方式。其中口令(密码)认证方式是我们最常用的一种，出于安全方面的考虑，介绍密钥认证方式登录到linux/unix的方法。 
使用密钥登录分为3步： 
1、生成密钥（公钥与私钥）； 
2、放置公钥到服务器~/.ssh/authorized_key文件中； 
3、配置ssh客户端使用密钥登录。
--------------------- 

一、通过ssh-keygen命令生成密钥对，密钥类型为RSA，也可以通过其他软件生产密钥对。
==========================================================================
pipci@ubuntu:~$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/pipci/.ssh/id_rsa):            <==这里输入私钥名，直接回车就可以名字就为括号中默认的名字
Enter passphrase (empty for no passphrase):                               <==输入密码，自动登录设置为空，直接回车就可以                         
Enter same passphrase again:                                              <==输入确认密码，直接回车就可以
Your identification has been saved in /home/pipci/.ssh/id_rsa.            <==生成的私钥名和位置
Your public key has been saved in /home/pipci/.ssh/id_rsa.pub.            <==生成的公钥名和位置
The key fingerprint is:
SHA256:Hsi5oo0Yr1a9eXtgNeLlu/UAJx1EiH34Gghv96FeXEs pipci@ubuntu
The key's randomart image is:
+---[RSA 2048]----+                                                       <==密钥的位数 
|        o +o     |
|     . . +..     |
|      o . o.     |
|     . B *.o.E   |
|    . * SoBo+ .  |
|   . . * =++ .   |
|. . . = + oo     |
| = + + . +. o    |
|+.+ . ..o..  .   |
+----[SHA256]-----+
pipci@ubuntu:~$ 
===================================================================

查看生成的密钥文件：
===================================================================
pipci@ubuntu:~$ ls -l .ssh/
-rw------- 1 pipci pipci 1679 10月 19 11:45 id_rsa
-rw-r--r-- 1 pipci pipci  394 10月 19 11:45 id_rsa.pub
pipci@ubuntu:~$ 
===================================================================

注意两点：

1、生成密钥对输入密码的作用是保护本地私有密钥的密码，也就是说，即使有人到用了你的计算机或私钥文件，没有这个密码依然不能使用你的私钥，在使用密钥登录时候也会要求你输入密码，这个密码就是生成密钥对时候输入的密码，用来解锁私钥文件，密码最低5个字符。

2、生成密钥对的私钥权限必须是600公钥权限是644,即只能本人可以查看私钥文件，除了本人以外的任何用户都不能产看，别人可以查看也就意味着任何人都可以通过这个私钥登录了，显然这是不安全的，公钥可以随便查看，但是不能修改内容，修改了还怎么配对登录。同时密钥对的父目录.ssh的权限必须是700即只有本人可以查看和进入。如果是通过命令新创建的.ssh默认就是700权限，创建完查看下就可以，如果不是更改权限。如果不是上面说的权限，客户端登录时候可能会出错。


二、通过scp命令将id_rsa.pub公钥文件复制到远程服务器：
====================================================================
pipci@ubuntu:~$ scp /home/pipci/.ssh/id_rsa.pub  laopi@192.168.1.166:/home/laopi/.ssh/
laopi@192.168.1.166's password: 
id_rsa.pub                                    100%  394     0.4KB/s   00:00    
pipci@ubuntu:~$ 
=====================================================================
通过scp命令复制，前提是远程服务器已经开启ssh密码登录，将公钥文件复制到用来管理用户主目录下面的.ssh目录如果不存在先创建这个目录。这个.ssh的目录权限
也要设置成700不让其他用户进入更改，上面的例子远程服务器的ip地址为192.168.1.166用户名为laopi（普通用户）


三、远程服务器的配置

1、将上传的公钥文件导成或重命名成authorized_keys文件或
laopi@debian:~$ cat .ssh/id_rsa.pub >> .ssh/authorized_keys    #导成

2、编辑ssh的配置文件。

vim /etc/ssh/sshd_config 

要确保下面这两项目前面没有#使之生效
---------------------------------------------------------------
PubkeyAuthentication yes                      #允许公钥认证                    

AuthorizedKeysFile .ssh/authorized_keys       #指定包含用于用户身份验证的公钥的文件 
---------------------------------------------------------------
为了安全考虑禁用root账户登录
PermitRootLogin no                            #选项前面可以加#号注释掉，同样会禁用root用户

有了证书登录了，就禁用密码登录吧，安全要紧
PasswordAuthentication no                     #选项前面可以加#号注释掉，同样会禁用密码登录

重启一下ssh服务，这样ssh配置才能生效：

root@debian:~# systemctl restart sshd.service 

四、ssh-keygen 命令常用参数

$ ssh-keygen 参数

常用参数：
-t 指定要创建的密钥类型，如：-t dsa(SSH-2) | ecdsa | ed25519 | rsa(SSH-2)| rsa1(SSH-1) 

-b bits 指定密钥长度。对于 RSA 密钥，最小要求 768 位，默认是 2048 位

-C comment 提供一个注释。

-N new_passphrase 提供一个新的密语。

-F hostname
在 known_hosts 文件中搜索指定的 hostname ，并列出所有的匹配项。 这个选项主要用于查找散列过的主机名/ip地址，还可以和 -H 选项联用打印找到的公钥的散列值。

-H 对 known_hosts 文件进行散列计算。这将把文件中的所有主机名/ip地址替换为相应的散列值。原来文件的内容将会添加一个".old"后缀后保存。这些散列值只能被 ssh 和 sshd 使用。这个选项不会修改已经经过散列的主机名/ip地址，因此可以在部分公钥已经散列过的文件上安全使用。

-R hostname
从 known_hosts 文件中删除所有属于 hostname 的密钥。这个选项主要用于删除经过散列的主机(参见 -H 选项)的密钥。

-f filename 指定密钥文件名

-l 显示公钥文件的指纹数据。它也支持 RSA1 的私钥。对于 RSA 和 DSA 密钥，将会寻找对应的公钥文件，然后显示其指纹数据。

1、查看id_rsa.pub的公钥指纹
pipci@ubuntu:~$ ssh-keygen -lf .ssh/id_rsa.pub 
2048 SHA256:Hsi5oo0Yr1a9eXtgNeLlu/UAJx1EiH34Gghv96FeXEs pipci@ubuntu (RSA)

1、用 md5 的方式查看指纹数据
pipci@ubuntu:~$ ssh-keygen -E md5 -lf .ssh/id_rsa.pub 
2048 MD5:fa:ba:4b:35:18:7f:5f:94:f0:6b:b5:7a:89:98:f9:a5 pipci@ubuntu (RSA)
```
