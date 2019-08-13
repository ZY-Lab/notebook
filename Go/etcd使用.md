# etcd使用
```
etcdctl --endpoints=http://192.168.3.128:2379 get --from-key ""
```
## 安装
```
https://github.com/etcd-io/etcd/releases
```
## 安装etcdctl
etcdctl的二进制文件可以在 github.com/coreos/etcd/releases 选择对应的版本下载，解压完后会有etcd和etcdctl文件，粘贴到/usr/local/bin/下
## 使用etcdctlv3的版本时，需设置环境变量ETCDCTL_API=3
```
export ETCDCTL_API=3
```