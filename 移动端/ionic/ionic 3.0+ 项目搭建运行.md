#ionic 3.0+ 项目搭建运行

###环境迁移
先看下升级后最新的环境输出信息

>ionic info

全局升级了Cordova和Ionic的版本，分别是7.0.1和3.4.0。
输出ionic info 打印出最新的环境配置信息。这里要特殊指出的是Ionic CLI。
Ionic和Ionic CLI是不一样的东西。
Ionic CLI是基于nodeJS的工具脚手架，开发Ionic应用程序过程中使用的主要工具。
更新了最新的Ionic版本后，该工具也随之升级。

在官博相关资料中有介绍，Ionic团队为了提高其性能和用户体验，重写了CLI。
更新后的其中一个变化就是和Cordova CLI交互相关的所有命令，都需要将cordova作为命令的一部分。
以前我们是执行以下命令

>ionic platform add android  
ionic run/build android

在v3 CLI命令则是

>ionic cordova platform add android  
 ionic cordova run/build android

再说起cordova，其实以上命令也都是基于Cordova CLI，那么，如果用Cordova CLI提供的命令来打包，是不是也是可以执行。
这当然可以，只是新的工具提供了更多的命令，比如ionic generate(简写: ionic g)，可以更加高效的构建项目。
拿官博提供的一个例子说下。

>$ ionic g tabs  
What should the name be? myTab  
? How many tabs? 4  
? Name of this tab: home  
? Name of this tab: maps  
? Name of this tab: contacts  
? Name of this tab: more  
[OK] Generated a tabs named myTab!  

再比如ionic g page myPage、ionic g provider MyData，都可以快速的为我们构建模块化、结构化的目录。
工具的作用就是提高我们的开发效率，具体怎么使用，见仁见智了。
如果习惯了依旧可以使用cordova，但为了往后面的版本靠拢，升级也无可厚非。
###版本降级

说完环境迁移，说说版本回退的问题。在升级到3.4.0之前，因为有升级到2.x的经历，导致1.x项目也是无法正常运行打包，因此对版本进行了回退。而在升级到3.3的时候，折腾了半天也没发现命令重构成ionic cordova。所以把Ionic CLI降级回退到了2.x，这时候ionic start 都是1.x的版本，再通过ionic start xxx –v2的方法去下载ionic框架在github最新的demo，这时候下载的就是最新的3.x版本。
2.x->3.x只是版本号的迭代，所以执行–v2是会下载最新的demo源码。



打开 Node 命令行，首先 cd 到项目目录，使用 start 命令来创建一个新App：
>ionic start MyIonic2Project tutorial --v2

这个命令将下载项目模板，安装 npm modules，设置 Cordova 的相关信息。
tutorial 参数的意思是下载 tutorial 模板来初始化项目，如果不指定这个参数的话，比如：
>ionic start MyIonic2Project --v2

默认会使用 tabs 模板。
当然你也可以加一个 blank 参数，这样就是一个空项目。
--v2 的参数必须要加，不然会建立 v1.x 版本的项目。
如果失败，有可能会出现以下信息：

>Creating Ionic app in folder E:\Workspaces\Ionic2\MyIonic2Project based on tutorial project
Downloading: https://github.com/driftyco/ionic2-app-base/archive/master.zip
[=============================] 100% 0.0s
Downloading: https://github.com/driftyco/ionic2-starter-tutorial/archive/master.zip
[=============================] 100% 0.0s
Installing npm packages...
Error with start undefined
Error Initializing app: There was an error with the spawned command: npminstall
There was an error with the spawned command: npminstall
Caught exception:
 undefined
Mind letting us know? https://github.com/driftyco/ionic-cli/issues

这说明 npm 安装的时候失败了，可以 cd 到项目目录，使用之前设置过的 cnpm 命令：
>E:\Workspaces\Ionic2>cd MyIonic2Project
E:\Workspaces\Ionic2\MyIonic2Project>cnpm install

直到最后输出类似以下信息：
>All packages installed (319 packages installed from npm registry, use 2m, speed 37.49kB/s, json 659(4MB), tarball 1.07MB)

说明 npm modules 安装成功。

###项目启动
>ionic serve