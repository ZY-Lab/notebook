## micro操作手册

### 在gopath的src中生成一个样例文件
> micro new example   

### 启动服务
> go run  

### 用micro api订阅
> micro api  --namespace=go.micro.evt  起一个micro api ，handler默认为api，namespace默认为go.micro.api。Namesapce类似于域名，在访问路径中不写，具体访问路径要看handler类型。

### 发送HTTP请求
> 请求路径按照handler中选择的方式，具体官方文档：https://micro.mu/docs/go-api.html#rpc-handler

+ API Handler(默认)
> Path: /[service]/[method]

+ Broker Handler
> Path: /

+ CloudEvents Handler
> Path: /[topic]

+ Event Handler
> Path: /[topic]/[event]

+ HTTP Handler
> Path: /[service]

+ RPC Handler
> Path: /[service]/[method]

+ Registry Handler
> Path: /

+ Web Handler
> Path: /[service]
### 常用指令
```
# 安装micro
go get -u github.com/micro/micro
# 查看启动的服务
micro list services

```