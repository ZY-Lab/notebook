## LESS
##### 什么是LESS？

    less是一种动态样式语言，属于css预处理语言的一种，他可以类似css的语法，为css的赋予了动态语言的特性，如变量、继承。运算、函数等，更方便css的编写和维护。

    less可以在多种语言，环境中使用，包括浏览器端，桌面客户端，服务端。

##### 编译工具
**koala**
- 国人开发less/sass编译工具
- 下载地址：http://koala-app.com/index-zh.html

**Node.js库编译**

**浏览器端编译**

##### 怎么使用koala
1. 在项目中的文件夹下新建一个less的文件
![001.png](E:\Thunder\Markdown笔记\001.png)

2. 打开下载好的koala,将项目文件拖入其中
![002.png](E:\Thunder\Markdown笔记\002.png)

3. 右键选中-设置输出路径-再讲文件名改为.css的尾缀。

4. 然后koala就会自动编译css的代码了。

##### less怎么写？
    @charset "UTF-8";

less的注释:

    /*我是被编译的，会在编译后的css文件显示出来*/
    //不会被编译

less中的变量:

    //less中想声明变量的话 一定要用 @开头     @变量名:值；
    @test_width:300px;
    .box{
        width: @test_width;
        height: @test_width;
        background: #000;

        .border;
    }

less混合:

    .border{
        border: solid 5px pink;
    }

    .box2{
        .box;
        .border;
        margin-left: 100px;
    }

	//混合可带参数
    .border_02(@border_width){
        border:solid #0c0 @border_width
    }

    .test_hunhe{
        .border_02(30px);
    }

	//混合-默认带值
    .border_03(@border_width:10px){
        border: solid #0cc @border_width;
    }

    .test_hunhe_03{
        .border_03();
    }
    .test_hunhe_03_02{
        .border_03(100px);
    }

    .border_radius(@radius:20px){
        border-radius: @radius;
        -moz-border-radius: @radius;
        -webkit-border-radius: @radius;
    }
    .radius_test{
        width: 100px;
        height: 100px;
        background: #00CC00;
        .border_radius();
    }

匹配模式:

    .triangle(top,@w:5px,@c:#ccc){
        border-width: @w;
        border-color: transparent transparent @c transparent;
        border-style: dashed dashed solid dashed;
    }
    .triangle(bottom,@w:5px,@c:#ccc){
        border-width: @w;
        border-color: @c transparent transparent transparent;
        border-style: solid dashed dashed dashed;
    }
    .triangle(left,@w:5px,@c:#ccc){
        border-width: @w;
        border-color: transparent @c transparent transparent;
        border-style: dashed solid dashed dashed;
    }

    .triangle(right,@w:5px,@c:#ccc){
        border-width: @w;
        border-color: transparent transparent transparent @c;
        border-style: dashed dashed dashed solid;
    }
    .triangle(@_,@w:5px,@c:#ccc){
        width: 0;height: 0;
        overflow: hidden;
    }
    .sanjiao{
        .triangle(top,100px)
    }

    //匹配模式-定位:
    .pos(r){
        position: relative;
    }
    .pos(a){
        position: absolute;
    }
    .pos(f){
        position: fixed;
    }

    .pipei{
        width: 200px;
        height: 200px;
        background: #55f;
        .pos(a);
    }

less运算:

    @test_01:300px;
    .box_02{
        width: (@test_01 - 10) * 2;
        color: #ccc - 20;
    }

嵌套规则:
    .list{
        width: 600px;
        margin: 30px auto;
        padding: 0;
        list-style: none;
        li{
            height: 30px;
            line-height: 30px;
            background: #6df;
        }
        li:nth-of-type(3) a{
            color: #f0f;
            text-decoration: none;
        }
        a{
            float: left;
            &:hover{
                color: #5555FF;
            }
        }

        span{
            float: right;
        }
    }

@arguments:

    .border_arguments(@w:30px,@c:red,@xx:solid){
        border: @arguments;
    }
    .test_argument{
        .border_arguments();
    }
    .test_argument_02{
        .border_arguments(40px);
    }

避免编译:

	//属性:~'值';
    .test_03{
        width:~'calc(300px - 30px)';

    }

!important关键字:

    .test_03_important{
        .border_03() !important;
    }

##### 最后就看自己的了

















