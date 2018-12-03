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
