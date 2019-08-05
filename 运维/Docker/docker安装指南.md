#docker指南

##使用官方安装脚本自动安装
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

##Ubuntu 14.04 16.04 (使用apt-get进行安装)
### step 1: 安装必要的一些系统工具
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
### step 2: 安装GPG证书
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
### Step 3: 写入软件源信息
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
### Step 4: 更新并安装 Docker-CE
sudo apt-get -y update
sudo apt-get -y install docker-ce

##CentOS 7 (使用yum进行安装)
### step 1: 安装必要的一些系统工具
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
### Step 2: 添加软件源信息
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
### Step 3: 更新并安装 Docker-CE
sudo yum makecache fast
sudo yum -y install docker-ce
### Step 4: 开启Docker服务
sudo service docker start



##Debian 9
> sudo apt update

接下来，安装一些允许apt使用包通过HTTPS的必备软件包：

> sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common

然后将官方Docker存储库的GPG密钥添加到您的系统：

> curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -

将Docker存储库添加到APT源：

> sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

接下来，使用新添加的repo中的Docker包更新包数据库：

> sudo apt update

确保您要从Docker repo而不是默认的Debian repo安装：

> apt-cache policy docker-ce

虽然Docker的版本号可能不同，但您会看到这样的输出：

```
docker-ce:
  Installed: (none)
  Candidate: 18.06.1~ce~3-0~debian
  Version table:
     18.06.1~ce~3-0~debian 500
        500 https://download.docker.com/linux/debian stretch/stable amd64 Packages
```

请注意，docker-ce未安装，但安装的候选者来自Debian 9（stretch）的Docker存储库。
最后，安装Docker：

> sudo apt install docker-ce

现在应该安装Docker，守护进程启动，并启用进程启动进程。检查它是否正在运行：

> sudo systemctl status docker

输出应类似于以下内容，表明该服务处于活动状态并正在运行：
```
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2018-07-05 15:08:39 UTC; 2min 55s ago
     Docs: https://docs.docker.com
  Main PID: 21319 (dockerd)
   CGroup: /system.slice/docker.service
           ├─21319 /usr/bin/dockerd -H fd://
           └─21326 docker-containerd --config /var/run/docker/containerd/containerd.toml
```


##指定构建镜像文件
> docker build -t imagename -f path/to/dockerfile .
> docker build -f Dockerfile-ca -t base-auth-ca:v0.1 .


## 推送镜像到阿里云
> docker build -t registry.cn-hangzhou.aliyuncs.com/wall-js/test:1.0 .
> docker login --username=**** registry.cn-hangzhou.aliyuncs.com
> docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/wall-js/test:[镜像版本号]
> docker push registry.cn-hangzhou.aliyuncs.com/wall-js/test:[镜像版本号]

## 启动容器命令
> docker run -d -it -p 8080:8080 -v /data:/data base-auth-ca:v0.1
> docker run -p 8080:8080 -v /data:/data  base-auth-ca:v0.1
> docker logs $CONTAINER_ID # 在container外面查看它的输出 
> docker attach $CONTAINER_ID # 连接上容器实时查看
