#常见LINUX命令（CentOs）

###  1.创建用户，修改密码，权限  ###
	useradd 用户名     （创建用户）
	passwd 用户名	  （修改密码）
	
	vim /etc/sudoers   (编辑修改用户权限 使用sodo）
	大约在92行 root 用户下添加以下内容
	用户名	ALL=(ALL)	ALL

	使修改生效，可以重启系统，或者执行以下内容
	source /etc/profile

	切换用户
	su 用户名

### 2.校验 下载文件完整性
	MD5校验
	md5sum 你的文件名    （会输出校验码 和校验的文件名）
 
	SHA1校验
	sha1sum 文件名		（会输出校验码 和校验的文件名）

	将校验码和网上下载文件的MD5校验码比对 相同即完整，错误重新下载再次比对
### 3.安装软件
	yum install 软件名
	yum remove 软件名
### 4. 解压文件
	tar -c	创建压缩文件
	tar -x	解开压缩文件
	tar -t	查看压缩包内有哪些文件
	tar -z	用Gzip压缩或解压文件
	tar -j	用bzip2压缩或解压文件
	tar -v	显示压缩或解压过程
	tar -f	目标文件名
	tar -p	保留原始权限和属性
	tar -P	使用绝对路径来解压
	tar -C	指定解压到的目录
### 5.下载文件
	wget -b	后台下载模式
	wget -P	下载到指定目录
	wget -t 最大尝试次数
	wget -c 断点续传
	wget -p 下载页面内所有资源
	wget -r 递归下载
### 6.重启系统
	reboot
### 7.查看网络状态及网卡配置等
	ifconfig
### 8.查看系统内核与版本信息
	uname -a
### 9.工作目录等命令
	pwd							显示当前目录
	cd							切换路径
	ls							显示目录中的文件信息
	touch 文件名		  			创建空白文件
	mkdir 目录名					创建空白目录
	mv 	源文件 目标文件			剪切文件或重命名文件
	rm 	文件						删除文件或目录
	cp 	源文件 目标文件			复制文件或目录