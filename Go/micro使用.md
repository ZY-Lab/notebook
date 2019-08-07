## micro操作手册

### 概念理解
micro在该框架中可作为边车模型，并且可以开发plugins编译进micro中进行二次开发。

### 在gopath的src中生成一个样例文件
> micro new example   

### 启动服务
> go run  

### 用micro api订阅
> micro api  --namespace=go.micro.evt  

起一个micro api ，handler默认为api，namespace默认为go.micro.api。Namesapce类似于域名，在访问路径中不写，具体访问路径要看handler类型。

### 发送HTTP请求
> 请求路径按照handler中选择的方式，具体官方文档：https://micro.mu/docs/go-api.html#rpc-handler

+ API Handler(默认)
> Path: /[service]/[method]
> 与rpc差不多，但是会把完整的http头封装向下传送，不限制请求方法

+ Broker Handler
> Path: /

+ CloudEvents Handler
> Path: /[topic]

+ Event Handler
> Path: /[topic]/[event]
> 代理event事件服务类型的请求

+ HTTP Handler
> Path: /[service]
> 以反向代理的方式使用API，相当于把普通的web应用部署在API之后，让外界像调api接口一样调用web服务

+ RPC Handler
> Path: /[service]/[method]
> 通过RPC向go-micro应用转送请求，通常只传送请求body，头信息不封装。只接收POST请求

+ Registry Handler
> Path: /

+ Web Handler
> Path: /[service]
> 与http差不多，但是支持websocket

### 订阅中消息
broker.Subscribe(topic, func(p broker.Event) error {    
	// do anything    
}, broker.Queue("name"))
  
broker.Queue("name") 通过句话可以设置要共享消息的队列名称

### 常用指令
```
# 安装micro
go get -u github.com/micro/micro
# 查看启动的服务
micro list services

```
