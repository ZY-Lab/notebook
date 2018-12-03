#Nginx + PHP环境配置#
****
##安装Nginx##
1.	下载网址<http://nginx.org/>选择合适版本进行下载，试验中使用Nginx1.12.0  
2.	解压到指定目录下，如 F:/nginx

##下载PHP##
1.	根据自己需求版本下载php，试验中使用php5.4

##配置nginx#
##两种运行方式##
1.	在命令提示符下进去到Ngin的目录下输入nginx，如果安装失败也会提示（比较直观）  
2.	在F:/nginx文件夹下找到nginx.exe文件运行，期间会快速闪过命令提示窗口，运行任务管理器查看进程是否存在nginx.exe文件或者通过网址输出localhost查看nginx服务器是否安装成功  
 　　　**注：如果没有安装成功，打开F:Nginx目录下的log文件夹下的error.log  
 　　　如果出现类似的日志，说明８０端口被占用，无法安装**　　　　
	
    
		2017/07/03 10:45:18 [emerg] 3104#1932: bind() to 0.0.0.0:80 failed 　　
		(10013: An attempt was made to access a socket in a way forbidden by its access permissions)
        
 　**Nginx**本身是安装的默认端口是80端口，所以当80端口被系统所占用时无法安装  

**解决方案：** 命令提示符中输入`netstat -aon|findstr "80" `，查询80端口下谁在占用，例如查询结果如  

		TCP 127.0.0.1:80 0.0.0.0:0 LISTENING ４　　
　　　![baocuo](http://images.cnitblog.com/blog/433994/201309/11212431-34f1c558a528492fb4b9189b4c005b0f.jpg)　　　　

在任务管理器中找到４对应的任务，结束任务进程即可

3.	成功安装以后，在Nginx文件夹下的conf文件夹下找到**nginx.conf**文件  
4.	将这串代码中的root  html后面的html修改成你运行的主目录菜单，下面一栏添加上index.php，方便Nginx识别php文件


		server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   html;
            index  index.html index.htm;
        }

 如

 	server {
        listen       80;
        server_name  localhost;

        #charset koi8-r;

        #access_log  logs/host.access.log  main;

        location / {
            root   f:/nginx;
            index  index.html index.htm index.php;
        }
5.  再往下找到  


        
        #location ~ \.php$ {
        #    root           html;
        #    fastcgi_pass   127.0.0.1:9000;
        #    fastcgi_index  index.php;
        #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
        #    include        fastcgi_params;
        #}
把代码前面`#`注释去掉，同样修改root后面的地址将`/scripts`修改成`$document_root`代表root所指的地点，修改完配置文件，重启Nginx服务器

##配置PHP##

在php文件夹下找到**php.ini-production**文件修改名称为**php.ini**,进入文件，为了让php能够与nginx结合。找到 

		;cgi.fix_pathinfo=1
去掉前面的`#`注释  

		cgi.fix_pathinfo=1


1.	启动php-cgi  
打开cmd命令窗口，切换到php的安装目录，执行php-cgi -b 127.0.0.1:9000，即可启动php-cgi，启动完成后，cmd窗口切勿关闭，否则php-cgi也会被关掉的。  
**特别提醒：只有在开启php-cgi的情况下，nginx才能正常访问php。**  
2.	重启nginx
打开cmd命令窗口，切换到nginx所在目录，执行nginx -s reload即可重启nginx。其它相关nginx相关命令如下：  
启动：start nginx  
停止：nginx -s stop  
退出：nginx -s quit  