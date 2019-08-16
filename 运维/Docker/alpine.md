## 使用alpine构建基础镜像

### alpine
Alpine Linux是体积最小的Linux发行版，它重点关注于安全和速度。使用apk能够很快地安装软件包，
默认情况下，镜像只包含了完成基础UNIX任务所需要的东西 ，因此相对于其它Docker基础镜像，体积会更小。

### 更新最新镜像源列表
> apk update    

### 搜索软件包
> apk search #查找所以可用软件包

> apk search -v #查找所以可用软件包及其描述内容

> apk search -v 'acf*' #通过软件包名称查找软件包

> apk search -v -d 'docker' #通过描述文件查找特定的软件包

### 安装软件包：apk add
> apk add openssh #安装一个软件

> apk add openssh openntp vim   #安装多个软件

> apk add --no-cache mysql-client  #不使用本地镜像源缓存，相当于先执行update，再执行add

### 列出已安装的软件包：apk info
> apk info #列出所有已安装的软件包

> apk info -a zlib #显示完整的软件包信息

> apk info --who-owns /sbin/lbu #显示指定文件属于的包

### 升级软件版本：apk upgrade
> apk upgrade #升级所有软件

> apk upgrade openssh #升级指定软件

> apk upgrade openssh openntp vim   #升级多个软件

> apk add --upgrade busybox #指定升级部分软件包

### 删除软件包：apk del
> apk del openssh  #删除一个软件


### 使用alpine系统构建基础镜像

#### 基础alpine镜像

```
FROM alpine:3.9.2

//更新最新镜像源列表
RUN apk update

//设置Docker 时间为上海时区
RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/shanghai" >> /etc/timezone

//依次安装命令：curl、scp、telnet
RUN apk add curl
RUN apk add openssh-client
RUN apk add busybox-extras

//这里添加top命令是为了方便本地测试，防止启动该基本镜像容器后自动运行停止
ENTRYPOINT ["top"]


```

####基于Java jdk的镜像构建

```
FROM java:8-alpine

//更新最新镜像源列表

RUN apk update


//设置Docker 时间为上海时区

RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/shanghai" >> /etc/timezone


//依次安装命令：curl、scp、

RUN apk add curl
RUN apk add openssh-client

ENTRYPOINT ["top"]

```

### 构建过程中遇到的一些问题

#### 打包curl、scp、telnet基本命令至镜像中（添加RUN命令，采用apk add 的方式添加所需的软件包）

```

//更新最新镜像源列表

RUN apk update

//依次安装命令curl、scp、telnet

RUN apk add curl
RUN apk add openssh-client
RUN apk add busybox-extras

```

#### 更新为中国时区

```

//设置Docker 时间为上海时区

RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/shanghai" >> /etc/timezone

```


