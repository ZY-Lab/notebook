## micro操作手册

### 在gopath的src中生成一个样例文件
> Micro new example   

### 启动服务
> go run  

### 用micro api订阅
> micro api  --namespace=go.micro.evt  起一个micro api ，handler默认为api，namespace默认为go.micro.api。Namesapce类似于域名，在访问路径中不写，具体访问路径要看handler类型。

### 发送请求
> eg. http://localhost:8080/  

### 常用指令
```
# 查看启动的服务
micro list services

```