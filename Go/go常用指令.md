## go常用指令

### 安装依赖
> go get -v -u github.com/gpmgo/gopm
> go get -v -u golang.org/x/oauth2

### 常用指令
```
# 运行main.go文件
go run main.go
# 生成go.mod文件
go mod init
# 查看当前工程依赖
go list
# 生成vendor文件夹
go mod vendor

```