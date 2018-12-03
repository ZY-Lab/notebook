##PhpStorm配置debug

####PHP安装xdebug扩展  
前往[https://xdebug.org/wizard.php](https://xdebug.org/wizard.php)，将phpinfo信息输入，获知需要下载xdebug版本，并下载
下载好的xdebug放在PHP目录下的ext文件夹内。

####php.ini的配置
下面的配置仅供参考，路径要换成自己的：
>[Xdebug]
zend_extension = D:\php-5.6.30-Win32-VC11-x64\ext\php_xdebug-2.5.4-5.6-vc11-x86_64.dll  
xdebug.remote_enable = On  
xdebug.remote_handler = dbgp   
xdebug.remote_host= localhost  
xdebug.remote_port = 9000  
xdebug.idekey = PHPSTORM  

####PhpStorm配置
* 前往 File | Settings | Languages & Frameworks | PHP | Servers 配置server  
* 前往 File | Settings | Languages & Frameworks | PHP | Debug 配置Debug port
* 前往 File | Settings | Languages & Frameworks | PHP | Debug | DBGp Proxy 配置IDE key和Host 
（IDE key：PHPSTORM）
* 配置Run/Debug Configurations,创建一个PHP Built-in Web Server使用刚才配置好的server   
* 再配置一个PHP Web Application,使用刚才配置好的server