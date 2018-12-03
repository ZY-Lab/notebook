##React Native

####一、什么是React Native

React Native是Facebook开源的一套用于开发移动端跨平台App的技术框架；起代码托管在GitHub上。

####二、为什么要用React Native

优点：跨平台、性能高、支持动态更新、代码复用率高

####三、React Native前期知识

- **React：**基础框架，主要涉及实现的理念，不能做网页开发和移动开发
- **React.js：**在React框架的基础之上发展的，专门用来做网页开发的
- **ReactNative：**用来做移动开发的


**知识准备：**
1. 前端基础知识：html、css、JavaScript
2. JSX语法知识
3. ES6相关知识
4. React中文网站



#####1、React介绍

（1）起源于Facebook公司，用来做ins的开发，不是属于MVC框架，主要考虑界面。
（2）特点：
             作为UI（MVC中的视图层）
             虚拟DOM：实现了优化视图的渲染和刷新
             组件化：封装起来的特定功能的组件
             数据流：实现了单向的数据流

####四、环境搭建

**文档手册：http://reactnative.cn/docs/0.45/getting-started.html#content**

#####1、需要安装的工具

**（1）Node.js
   （2）React Native Command Line
   （3）Android Studio/XCode
   **
#####2、在Windows平台上搭建React Native开发环境

**（1）安装Node.js
   （2）安装React Native命令行工具**
   可以通过react-native --help查看支持的命令行工具
   **（3）安装android studio**

#####3、创建应用

**创建项目：**react-native init 项目名
**运行项目：**将创建的项目中的android导入到android studio中，运行

**报错：**
![未启动服务](https://git.oschina.net/uploads/images/2017/0629/102646_a56ef2c1_684224.jpeg "在这里输入图片标题")

**解决：**在项目目录下通过npm启动包服务管理器，**npm start**

**报错：**
![](https://git.oschina.net/uploads/images/2017/0629/102934_6d6b17f7_684224.jpeg "在这里输入图片标题")

**解决：**设置IP地址和端口号，重新运行


#####3、项目理解

![输入图片说明](https://git.oschina.net/uploads/images/2017/0629/151421_f80f10e0_684224.png "在这里输入图片标题")
- **android**文件夹，就是一个可以用android studio打开的android项目。
- **ios**文件夹，是一个可以用xcode打开的ios项目。
- **index.android.js**，这是android的React Native入口文件。
- **index.ios.js**，这是ios的React Native入口文件。
- **package.json**，类似android studio的build.gradle，你依赖的库都写在里面。
- **node_module**文件夹，你依赖的库下载下来都存放在里面，属于git的忽略文件，你要找的依赖库源码也在里面，包括React和React Native。
- **jscode**文件夹，是自己创建的文件夹，用来存放自己写的js文件。

**PS:**
package.json，类似于android studio中的build.gradle添加远程依赖，不同的是，package.json大多数时候不需要我们手动添加，我们只需要在根目录通过命令行，npm install xxxxxx --save 就可以依赖一个库了。

install之后，库的依赖信息，自动被写到package.json里面，对应的库也会被下载到node_module文件夹中，类似android studio依赖后把aar同步到本地。


####五、开发工具的选择

#####1、开发工具的选择
- **WebStorm：**Web开发神奇
- **Nuclide+Watchman(Mac)**
- **Sublime**



