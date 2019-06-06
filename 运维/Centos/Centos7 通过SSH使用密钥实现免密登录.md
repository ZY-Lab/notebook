## Centos7 通过SSH使用密钥实现免密登录

#### 查看 ssh 状态
> systemctl status sshd
#### 启动 ssh
> systemctl start sshd
#### 停止 ssh
> systemctl stop sshd

# 将 serverA ~/.ssh目录中的 id_rsa.pub 这个文件拷贝到你要登录的 serverB 的~/.ssh目录中
scp ~/.ssh/id_rsa.pub 192.168.0.101:~/.ssh/
# 然后在 serverB 运行以下命令来将公钥导入到~/.ssh/authorized_keys这个文件中
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# 另外要注意请务必要将服务器上
~/.ssh权限设置为700
~/.ssh/authorized_keys的权限设置为600
# 这是linux的安全要求，如果权限不对，自动登录将不会生效

1：修改/etc/ssh/sshd_config文件

找到：
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys

然后再找到：

PasswordAuthentication no

这里默认是yes，所以把改成no，就是禁止密码登录。

2：重启sshd服务

centos7 命令：

systemctl restart sshd.service
