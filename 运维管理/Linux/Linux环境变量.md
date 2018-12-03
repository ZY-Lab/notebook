#Linux环境变量

1. 修改/etc/profile文件，将影响全局，所有用户。/etc/profile在系统启动后第一个用户登录时运行。在/etc/profile文件中添加

	export PATH=/someapplication/bin:$PATH

	要使修改生效，可以重启系统，或者执行

	source /etc/profile


2. 修改/etc/environment，将影响全局。/etc/environment文件与/etc/profile文件的区别是：/etc/environment设置的是系统的环境，而/etc/profile设置的是所有用户的环境，即/etc/environment与用户无关，在系统启动时运行。在/etc/environment文件中添加

	PATH=/someapplication/bin:$PATH

	CentOS和大多Linux系统使用$访问环境变量，环境变量PATH中使用冒号:分隔。而Windows中使用两个%访问环境变量，PATH使用分号;分隔，例如：

	set PATH=E:\someapplication\bin;%PATH%

3. 修改~/.bash_profile（首选），将影响当前用户。在~/.bash_profile文件中添加
 
	export PATH=/someapplication/bin:$PATH

4. 修改/etc/bashrc（Ubuntu和Debian中是/etc/bash.bashrc），影响所有用户使用的bash shell。/etc/bashrc顾名思义是为初始化bash shell而生，在bash shell打开时运行。这里bash shell有不同的类别：登录shell和非登陆shell，登录shell需要输入用户密码，例如ssh登录或者su - 命令提权都会启动login shell模式。非登陆shell不会执行任何profiel文件；交互shell和非交互shell，提供命令提示符等待用户输入命令的是交互shell模式，直接运行脚本文件是非交互shell模式，一般情况下非交互shell模式不执行任何bashrc文件。根据以上情况，选择是否修改/etc/bashrc。

5. 修改~/.bashrc，影响当前用户使用的bash shell。

6. 在终端中执行以下命令，只影响当前终端。

	export PATH=/someapplication/bin:$PATH