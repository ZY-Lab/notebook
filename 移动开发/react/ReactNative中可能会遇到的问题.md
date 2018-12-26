### ReactNative中可能会遇到的问题

####一般问题
**1、RN和React.js是一个东西吗？**
RN和React.js共用一些抽象层，但具体有很多差异，且目标平台不同：RN目前只能开发iOS/Android App，而React.js用于开发web页面。

**2、RN可以在windows下开发吗？**
对于iOS开发，可以通过虚拟机或黑苹果等方式，但很麻烦也不推荐。做iOS开发，迟早你都需要一台Mac电脑。

对于Android开发，理论上没问题。但由于FB的员工基本都用mac，没有怎么管过windows兼容性，所以目前的版本可能在windows上会遇到一些问题。

**3、RN所支持的最低iOS和Android版本？**
Android >= 4.1 (API 16)
iOS >= 7.0

**4、RN和cordova/phonegap是一个东西吗？**
不一样。RN不是一个webview（但包含了webview组件），不能直接复用web页面代码。RN的性能接近原生，超过cordova/phonegap。

**5、可以使用现有的js库吗？**
由于RN理论上更接近nodejs的运行环境，所以对nodejs的库兼容更好一些。浏览器端的js库，涉及到DOM、BOM、CSS等功能的模块无法使用，因为RN的环境中没有这些东西。

####环境搭建与编译问题

**1、创建新项目，```react-native init AwesomeProject```命令长时间无响应，或报错```shasum check failed```**
网络原因，react-native命令行从npm官方源拖代码时会遇上麻烦。请将npm仓库源替换为国内镜像：
```
npm config set registry https://registry.npm.taobao.org --global
npm config set disturl https://npm.taobao.org/dist --global
```
另，执行init时切记不要在前面加上sudo（否则新项目的目录所有者会变为root而不是当前用户，导致一系列权限问题，请使用chown修复）

**2、运行react-native run-android时报错，报错信息中含有```Could not find tools.jar```等字样**
重装JDK1.8

**3、运行react-native run-android时报错，报错信息中含有```SDK location...ANDROID_HOME```等字样**
请对照官方文档，配置ANDROID_HOME环境变量。

**4、运行react-native run-android时报错，报错信息中含有```No connected devices!```字样**
既然是没有connected devices，那你就connect一个device咯！（usb连上真机，或启动一个模拟器）。

**5、运行react-native run-android时报错，报错信息中含有```Unable to upload some APKs!```字样**
降级gradle版本

**6、真机上运行时白屏！**
请找到并打开悬浮窗权限。比如miui系统在这里打开悬浮窗权限。

**12、RN所支持的最低iOS和Android版本？**

