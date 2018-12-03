## Android环境搭建

### JDK的安装和Java环境变量的设置

 JDK下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html

 JDK(Java Development Kit)是整个Java的核心，包括一系列Java开发的东西，安装完毕需要配置一下环境变量。

 JAVA_HOME

 JDK的安装路径，这个环境变量本身不存在，需要创建，创建完则可以利用%JAVA_HOME%作为统一引用路径，其值为：jdk在你电脑上的安装路径。

![](https://i.imgur.com/S8p5rSs.jpg)

 PATH

 PATH属性已存在，可直接编辑。作用是用于配置路径，简化命令的输入，其值为：%JAVA_HOME%\bin。

![](https://i.imgur.com/9M7gx2g.jpg)

 CLASSPATH

 用于编译时JAVA类的路径，注意这里设置的是两个值，(.;)表示的是JVM先搜索当前目录。其值为：.;%JAVA_HOME%\lib\tools.jar。

![](https://i.imgur.com/W5L6XPd.jpg)

配置完毕后，通过cmd运行以下命令：java -version，javac 如果出现返回信息，则设置成功。

![](https://i.imgur.com/ilKP9CN.jpg)

### 安装Android SDK

 Android SDK下载地址：http://developer.android.com/sdk/index.html。

 Andorid SDK为Android管理开发包工具，提供了Android各级平台的开发包和工具。注意，因为我们是独立安装，不是一体化(集成系列工具)所以需要单独下载SDK。

 运行安装文件，并把安装目录下tools文件夹路径设置进PATH环境变量。

![](https://i.imgur.com/tUuN9Eh.jpg)

![](https://i.imgur.com/o7iCQrY.jpg)

