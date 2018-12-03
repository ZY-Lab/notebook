## Subversion Edge使用经验
由于想通过Subversion来进行内部的版本控制，来有效地控制好每一个版本迭代，提高团队效率。
在安装之前有几点需要注意的地方：
* 1-安装过程不能使用root账号来安装和启动，否则会造成subversion启动失败，需要重装。
* 2-需要安装java jdk1.6 或以上版本才能运行。  

以下是关于Subversion Edge 的一些经验之谈，之所以选择 CollabNet Subversion Edge 是因为图形界面使用起来比较方便 ，不说太多，让我们开始吧。
下载安装Svn服务器
* （1）下载CollabNet Subversion Edge，到这个网址去下载最新版本：
 http://www.open.collab.net/cn/downloads/subversion/redhat.html
* （2）将下载的tar.gz文件放上服务器
先放在/opt/install/subversion/ 下面（注：路径根据自己的喜欢和习惯而定）
然后复制到 /home/suberversion/ 目录下面 （注：这个目录也是需要自己建立）
* （3）在安装subversion之前记得先安装jdk 1.6 或者 jre 6.0 和 python 2.4~2.6
* （4）以超级用户登录系统，设置我们安装CollabNet Subversion目录/opt的读写权限，设置svn群组下的用户对该文件具有读写权限
chmod -R 777 /home/subversion/csvn/
这里我直接将整个目录和目录下面的文件全部设置为777
把svn群组下的用户加入到sudo组，打开/etc/sudoers文件，找到root ALL=(ALL) ALL，在下一行加入svnuser ALL=(ALL) ALL，强制保存退出。
注意：在修改 /etc/sudoer 文件的时候出了不少问题，如果直接 sudo chmod u+w /etc/sudoers ，修改成功了，结果出现了可以使用用户svnuser修改/etc/sudoers文件，但是因为是read-only的，无法保存。再执行sudo命令，老是出现提示：
sudo: /etc/sudoers is mode 00, should be 0440， 
解决方法：
先执行 chmod u+w /etc/sudoer 打开修改权限
然后用root用户进行修改，修改完成后
再执行 chmod u-w /etc/sudoer 关闭修改权限
* （5）解压安装好后，执行以下命令：
在开头csvn start的时候出现time-out，启动失败情况，显示什么
CSVN Console time-out waiting for  http://localhost:3343/csvn
原因是访问subversion的3343端口已经备占用，可能是之前装过而没有结束访问端口。（为什么之前装过？原因是尼玛的不能使用root安装，吃亏了！浪费了不少时间.）
然后通过命令netstat -anp 找到3343端口备占用，再通过命令lsof -i:3343 （需要root权限使用）,查找出对应的PID，不要犹豫，干掉这个进程，kill PID.(如果进程比较多的话，直接关掉所有httpd进程 killall -9 httpd)
在来bin/csvn start ，终于启动成功，显示如下：
CSVN Console is ready at http://localhost:3343/csvn
* （6）启动成功之后，默认管理员登录地址：
地址：http://localhost:3343/csvn
用户名：admin
密码：admin
* （7）添加项目库，在浏览器中打开http://localhost:3343/csvn （如果是服务端的话，请用服务器IP地址取代localhost），以admin/admin登录。
点击菜单栏“Repositories”——“new Repository”， 在Name中输入code项目库名，再点击右下角的Create按钮即可。
* （8）添加用户，点击菜单栏“Users”——“new User”， 在右边输入相应的用户信息，再点击右下角的Create按钮即可。

最后启动服务SVN服务的时候可能会出现服务启动失败，出了之前我说不能用root用户来安装之后，还有就是查看 bin/apachetl 是否已经启动，如果没有启动则通过 bin/apachetl start 来启动apache，启动的时候可能会说找不到httpd，用vim编辑apachetl , 找到HTTPD=”“；这里就是配置httpd访问路径，把路径填写好再试，最终subversion启动成功，大功告成。
实践：
* 1、下载安装文件：CollabNetSubversionEdge-2.3.0_linux-x86_64.tar.gz；
* 2、建组及用户
   groupadd svn；
   useradd -g svn svn；
   mkdir /home/svn；
   chown svn:svn /home/svn；
* 3、解压安装
   tar zxvf CollabNetSubversionEdge-2.3.0_linux-x86_64.tar.gz；
* 4、配置环境变量
   vi .profile
   export CSVN_HOME=$HOME/csvn
   export PATH=$CSVN_HOME/bin:$PATH
* 5、安装成功
svn@campost:~> svnadmin --help
....
* 6、启动svn控制台
>svn@campost:~/csvn> csvn start
Unable to start CSVN Console: no Java executable found
Please make sure the variable JAVA_HOME is defined in your environment

（2）安装java环境
----见linux配置java环境博客

（3）启动svn web控制台：
> svn@campost:~> csvn start
Starting CSVN Console......
CSVN Console started
Waiting for application to initialize (this may take a minute)..........................
CSVN Console is ready at http://localhost:3343/csvn
admin：admin进入web管理；

（4）启动svn：
>svn@campost:~> csvn-httpd start
Starting Subversion Edge Apache Server:  
----也可以在svn控制台启动

* 7、检查python是否安装：
>campost:~ # rpm -qa| grep python

----已安装
* 8、在“版本库——访问规则”里配置用户的版本库访问规则  
