## CocoaPods安装使用

替换更新源

    $ gem sources --remove https://rubygems.org/
    
    $ gem sources -a https://ruby.taobao.org/
    
    $ gem sources -l 
    
升级gem，在终端输入命令
> sudo gem update --system

安装CocoaPods，在终端输入命令
> sudo gem install cocoapods

查找第三方库，在终端输入命令
> pod search AFNetworking

在工程中创建一个Podfile文件，在终端输入命令
> touch Podfile

使用Xcode打开Podfile,然后按如下格式编辑Podfile，保存。

    platform :ios, '7.0'
    
    pod 'AFNetworking', '~>2.0'
    
    pod 'MJExtension'
    
    platform :ios, '6.1'
    
    pod 'SDWebImage', '~>3.7'
    
    pod 'MBProgressHUD', '~>0.9.1'
    
    pod 'Reachability', '~> 3.2'
    
安装第三方库，在终端输入命令
> pod install



使用CocoaPods 生成的 .xcworkspace 文件来打开工程，而不是以前的.xcodeproj 文件。
每次更改了Podfile 文件，你需要cd到工程根目录，然后重新执行一次pod update命令。


复制代码
 

 

Cocoapods 引用第三方库的几种方式

使用过 Cocoapods 的童鞋应该都知道，Cocoapods 的引用方式有三种：

版本号引用:	
> pod 'Alamofire', '~> 3.0'	

这种方式引用的是已经发布的版本，包含了 >``>=``<``<=``~> 几种版本限制符号，其中~>符号代表只更新最新的小版本号，比如 ~> 1.0.0 则只会更新到 1.0.x 的最新版本，而不会更新 1.x.0 以上的版本

本地路径引用:
> pod 'Alamofire', :path => '~/Documents/Alamofire'
   
这种方式直接引用本地的代码，这种方式下对引用库的修改仍然会提交到引用库的 git 上，而不会提交到主工程。

远程 git 路径引用:
> pod 'Alamofire', :git => 'https://github.com/Alamofire/Alamofire.git'

这种方式直接引用远程 git 代码，不需要引用的库进行发布，而且还支持 :branch =>、:tag => 和 :commit => 三种选项
