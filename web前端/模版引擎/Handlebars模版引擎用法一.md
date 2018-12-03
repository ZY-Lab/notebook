## Handlebars.js模版引擎用法一  

#### 一、为什么要使用Handlebars模版引擎  

1、Handlebars是全球使用率最高的模板引擎,所以当之无愧是全球最受欢迎的模板引擎.Handlebars在许多前端框架中都被引入,比如在MUI和AmazeUI等框架,都推荐使用Handlebars。  

2、可维护性（后期改起来方便）；可扩展性（想要增加功能，增加需求方便）；开发效率提高（程序逻辑组织更好，调试方便）；看起来方便。  

3、Handlebars基本语法极其简单,使用{{value}}将数据包装起来即可,Handlebars会自动匹配响应的数值和对象，容易上手。  

#### 二、怎么使用Handlebars  

##### 1、先获取handlebars  

通过Handlebars官网下载：http://handlebarsjs.com./installation.html ;  
通过npm下载：npm install –save handlebars ;  
通过bower下载：bower install –save handlebars ;  
通过github下载：https://github.com/daaain/Handlebars.git ;  

##### 2、基本用法  

###### ⑴.引入handlebars到项目中  
```js
<script src="js/handlebars-v4.0.11.js"></script>
```  
###### ⑵.在script标签里写模板内容  
这儿的标签type=”text/x-handlebars-template” 且需要设置一个id
```js
<script id="card-template" type="text/x-handlebars-template">
    <!--再这儿写相关内容-->
</script>
```
###### ⑶.在JS中编译模版  
```js
var t = $("#card-template").html(); //得到模版中的html
var f = Handlebars.compile(t);//预编译模版
var h = f(data); //将数据放入模板中

$("#card").html(h); //显示在某一个标签里面
```  

#### 三、简单的例子  
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .card {
            font-size: 24px;
            margin: 20px;
            padding: 10px;
            float: left;
            background: #5cffeb;
        }
    </style>
</head>
<body>

<div class="card" id="card"></div>

<script src="js/jquery-2.1.1.js"></script>
<script src="js/handlebars-v4.0.11.js"></script>
<script id="card-template" type="text/x-handlebars-template">
    <div>姓名：{{name}}</div>
    <div>年龄：{{age}}</div>
    <div>出生地：{{home}}</div>
    <div>职业：{{job}}</div>

</script>

<script>
    var data = {
        name: "自酌一杯酒",
        age: 22,
        home: "中国",
        job: "WEB前端工程师"
    };

    var t = $("#card-template").html(); //得到模版中的html
    var f = Handlebars.compile(t);//预编译模版
    var h = f(data); //将数据放入模板中

    $("#card").html(h); //显示在某一个标签里面
</script>

</body>
</html>
```
虽然感觉这个简单的例子，比起之前在js里用拼接的方法看起稍麻烦点，但如果在js里写更多的html代码呢，这样不方便维护。并且handlebars的魅力还有很多.