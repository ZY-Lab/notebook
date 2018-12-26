## pm2常用命令
####主要特性
内建负载均衡（使用 Node cluster 集群模块）
后台运行
0 秒停机重载
具有 Ubuntu 和 CentOS 的启动脚本
停止不稳定的进程（避免无限循环）
控制台检测
提供 HTTP API
远程控制和实时的接口 API ( Nodejs 模块，允许和 PM2 进程管理器交互 )

####安装
> npm install -g pm2

####使用

进入 NoderCMS 的目录执行以下语句
> pm2 start bin/www -n my-nodercms

常用命令
指定 node 版本启动
> pm2 start bin/www -n my-nodercms --interpreter `/node-6.0.0`

其中/node-6.0.0为你的 node 目录

通过 n 来指定 node 版本启动
> pm2 start bin/www -n my-nodercms --interpreter `n bin 5.10.1`

指定 NoderCMS 端口号
> pm2 start bin/www -n my-nodercms --interpreter `n bin 5.10.1` -- -p 3001

查看托管列表
> pm2 list

重启
> pm2 restart my-nodercms

或

> pm2 restart all

其他命令
> pm2 --help

> pm2 start bin/www -n XinShunDa-nodercms-1.4.0  -- -p 8061

> pm2 startup                   # 创建开机自启动命令

> pm2 save                      # 保存当前应用列表
