## Android Studio常用功能配置

#### 1.代码提示不区分大小写

File | Settings 打开设置，选择Editor | General | Code Completion

Case sensitive completion：选择None。

![](https://i.imgur.com/5epkBug.png)

#### 2.显示行号

File | Settings 打开设置，选择Editor | General | Appearance

如图勾选 Show line numbers。

![](https://i.imgur.com/1m6Q73r.png)

#### 3.自动导包

在 Android Studio 中， Alt + Enter 和 Control + Alt + O 是用来导包和清除无用导包。但是，你可以设置其快速自动导包的。

File | Settings打开设置，选择 Editor | General | Auto Import，勾选 Optimize imports on the fly 和 Add unambiguous imports on the fly 。

![](https://i.imgur.com/UDRSUny.png)

#### 4.Log日志的颜色自定义

Android Studio中 Logcat 的默认只有红白两种颜色，这样不利于我们分析Log打印的信息。建议还是采用Android Holo主题的配色方案。

File | Settings 打开设置，选择Editor | Color & Fonts | Android Logcat，点击 Click on Save As…按钮创建一个新的配色 myLog。

注意：修改之前一定要取消勾选 Use inherited attributes

![](https://i.imgur.com/R6ZuSy1.png)






