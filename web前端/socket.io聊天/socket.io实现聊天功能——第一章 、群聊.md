### socket.io实现聊天功能——第一章 、群聊  

#### 一、准备工作--搭建项目  
1.确保node环境已经安好，我已将npm替换成了cnpm 淘宝镜像。  
2.新建一个名为 **" chat "** 的文件夹。  
3.在 **" chat "** 的文件夹里面 创建package.json的文件，我们用代码创建`cnpm init`,默认回车就行了。  
4.再分别安装**express** 和 **socke.io**的模块。  
>`cnpm install experss --save`  
 `cnpm install socket.io --save`  

5.在**chat**目录里创建一个名叫**app.js**的文件，写服务器代码。  
6.在**chat**目录里创建一个名叫**public**的文件夹，用来放页面**css、js、html**文件。  
7.在**public**目录里创建名为**chat.html**的文件，和名叫**js**文件夹和名叫**css**文件夹。聊天用到了Jquery和bootstrap的样式，所以自己需要引一下。  
8.在**chat/public/js**目录创建一个名为chat-room.js的文件,写客户端js的代码。  

**项目结构** 
```
├── node_modules
├── public
│   ├── css
│       └── bootstrap.min.css
│   └── js
│       └── bootstrap.min.js
│       └── chat-room.js
│       └── jquery.min.js
│   └── chat.html
├── app.js
│   └── example.js
├── package.json

```  

*下面就是代码部分了*  

#### 二、相关代码  
##### 1、chat.html里面的代码，里面写好一个简单的样式  
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>第一章-群聊</title>
    <meta name=”renderer” content=”webkit”>
    <!--避免IE使用兼容模式-->
    <meta http-equiv=”X-UA-Compatible” content=”IE=edge”>
    <meta name="viewport"
          content="width=device-width,height=device-height,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link rel="stylesheet" href="css/bootstrap.min.css">

    <style>
        /*滚动条样式*/
        ::-webkit-scrollbar { /*滚动条整体样式*/
            width: 4px; /*高宽分别对应横竖滚动条的尺寸*/
            height: 4px;
        }

        ::-webkit-scrollbar-thumb { /*滚动条里面小方块*/
            border-radius: 5px;
            -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
            background: rgba(99, 106, 207, 0.8);
        }

        ::-webkit-scrollbar-track { /*滚动条里面轨道*/
            -webkit-box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.2);
            border-radius: 0;
            background: rgba(255, 255, 255, 0.1);
        }

        .login-container {
            width: 300px;
            margin: 100px auto 0;
        }

        .login-container > div:nth-of-type(1) {
            width: 100%;
            text-align: center;
        }

        .login-container button {
            width: 100%;
        }

        .login-container .judge-warm {
            width: 100%;
            color: #a94442;
            background-color: #f2dede;
            border: 1px solid #ebccd1;
            border-radius: 4px;
            padding: 3px 10px;
        }

        /*聊天页面*/
        .chat-panel {
            position: absolute;
            width: 100%;
            max-width: 640px;
            min-width: 320px;
            height: 100%;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            margin: auto;
            box-shadow: 0 0 20px 5px #ccc;
        }

        .chat-panel .chat-content {
            position: absolute;
            width: 100%;
            height: calc(100% - 34px);
            background: #fff;
            overflow-y: scroll;
        }

        .chat-panel .chatinput {
            position: absolute;
            bottom: 0;
        }

        .clearfloat {
            zoom: 1;
            margin: 15px 5px;
        }

        .clearfloat:after {
            display: block;
            clear: both;
            content: "";
            visibility: hidden;
            height: 0;
        }

        .time-column {
            text-align: center;
            color: #888;
        }

        .chat-nickname {
            color: #9c9c9c;
            font-size: 12px;
            padding: 3px 10px;
        }

        .clearfloat .chat-avatars {
            display: inline-block;
            height: 30px;
            width: 30px;
            border-radius: 50%;
            border: solid 1px #e0e0e0;
            line-height: 30px;
            vertical-align: top;
            overflow: hidden;
            overflow: hidden;
        }

        .clearfloat .chat-avatars img {
            width: 100%;
            height: 30%;
        }

        .clearfloat .left .chat-avatars {
            margin-right: 10px;
        }

        .clearfloat .right .chat-avatars {
            margin-left: 10px;
        }

        .clearfloat .left .chat-message {
            background: #D9D9D9;
            min-height: 36px;
        }

        .clearfloat .chat-message {
            max-width: 252px;
            text-align: left;
            padding: 8px 12px;
            border-radius: 6px;
            word-wrap: break-word;
            display: inline-block;
            position: relative;
        }

        .clearfloat .left .chat-message:before {
            position: absolute;
            content: "";
            top: 8px;
            left: -6px;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
            border-right: 10px solid #D9D9D9;
        }

        .clearfloat .right {
            float: right;
        }

        .clearfloat .right {
            text-align: right;
        }

        .clearfloat .right .chat-message {
            background: #8c85e6;
            color: #fff;
            text-align: left;
            min-height: 36px;
        }

        .clearfloat .right .chat-message:before {
            position: absolute;
            content: "";
            top: 8px;
            right: -6px;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
            border-left: 10px solid #8c85e6;
        }


    </style>

</head>
<body>

<!--登陆部分-->
<div class="login-container">
    <div>
        <h1>聊天室</h1>
    </div>
    <div class="form-group">
        <input type="text" class="form-control" id="name" placeholder="用户名">
    </div>
    <button class="btn btn-primary" id="loginbtn">登录</button>
</div>

<!--聊天部分，最初是隐藏掉的-->
<div class="chat-container" style="display: none">
    <div class="chat-panel">
        <div class="chat-content">
            <!--这里显示的是聊天内容-->
        </div>
        <input type="text" class="form-control chatinput" id="chatinput" placeholder="...">
    </div>
</div>

<script src="js/jquery.min.js"></script>
<script src="socket.io/socket.io.js"></script>
<script src="js/chat-room.js"></script>

</body>
</html>
```  


##### 2.chat-room.js客户端里面的代码，代码里面也写有注释  
```js
$(function () {
    var socket = io();

    var _username = null;

    //设置用户名
    var setUsername = function () {
        _username = $("#name").val().trim();
        if (_username) {
            socket.emit("login", {username: _username});
        }
    };

    //开始聊天
    var beginChat = function () {
        $(".login-container").css("display", "none");
        $(".chat-container").css("display", "block");
    };

    //发送消息
    var sendMessage = function () {
        var _message = $(".chatinput").val();

        if (_message) {
            socket.emit("sendMessage", {username: _username, message: _message});
        }
    };

    // 获取时间
    function currentTime() {
        var d = new Date(),
            str = '';
        str += d.getFullYear() + '-';
        str += d.getMonth() + 1 + '-';
        str += d.getDate() + '  ';
        str += d.getHours() + ':';
        str += d.getMinutes() + ':';
        str += d.getSeconds();
        return str;
    }

    //显示消息
    var showMessage = function (data) {
        if (data.username === _username) {
            $(".chat-content").append("" +
                "<div class='clearfloat'>" +
                "   <div class='time-column'>" +
                "       <small class='chat-date'>" + currentTime() + "</small>" +
                "   </div>" +
                "   <div class='right'>" +
                "       <div class='chat-nickname'>" + data.username + "</div>" +
                "       <div class='chat-message'>" + data.message + "</div>" +
                "       <div class='chat-avatars'></div>" +
                "   </div>" +
                "</div>");
        } else {
            $(".chat-content").append("" +
                "<div class='clearfloat'>" +
                "   <div class='time-column'>" +
                "       <small class='chat-date'>" + currentTime() + "</small>" +
                "   </div>" +
                "   <div class='left'>" +
                "       <div class='chat-nickname'>" + data.username + "</div>" +
                "       <div class='chat-avatars'></div>" +
                "       <div class='chat-message'>" + data.message + "</div>" +
                "   </div>" +
                "</div>");
        }
    };

    //点击登录按钮触发setUsername();
    $("#loginbtn").on("click", function () {
        setUsername();
    });

    //用户名表单中回车触发setUsername();
    $("#name").on("keyup", function (event) {
        if (event.keyCode === 13) {
            setUsername();
        }
    });

    //发送信息表单中回车触发 sendMessage();
    $("#chatinput").on("keyup", function (event) {
        if (event.keyCode === 13) {
            sendMessage();
            $("#chatinput").val(""); //清空
        }
    });


    /**socket.io部分逻辑代码*/
    // 验证用户名是否重复
    socket.on('judgeUsername', function (data) {
        $(".login-container .form-group").append("<div class='judge-warm'>用户名重复!</div>");
        setTimeout(function () {
            $(".judge-warm").remove();
        }, 1500)
    });

    //监听到登录成功后
    socket.on("loginSuccess", function (data) {
        if (data.username === _username) {
            beginChat(data);
        }
    });

    //监听到事件发生就 显示消息
    socket.on("receiveMessage", function (data) {
        showMessage(data);
    });


});
```  

##### 3、app.js服务器端里面的代码
```js
var express = require("express"); //引用express模块
var app = express();
var server = require("http").Server(app);
var io = require("socket.io")(server);
var path = require("path");

server.listen("3000",function () {
   console.log("正在监听端口 3000");
});

app.get("/",function (req,res) {
   res.redirect("./chat.html");
});

app.use("/",express.static(path.join(__dirname, "/public")));


var users = []; //用来保存所有的用户信息  

io.on("connection",function (socket) {

    socket.on("login",function (data) {
        /**
         * 先保存在socket中
         * 循环数组判断用户名是否重复,如果重复，则触发usernameErr事件
         * 将用户名删除，之后的事件要判断用户名是否存在
         */
        socket.username = data.username;
        for (var user in users) {
            if(users[user].username === data.username){
                socket.emit('judgeUsername',{err: '用户名重复'});
                socket.username = null;
                break;
            }
        }
        //如果用户存在，将该用户的信息存进数组中
        if (socket.username){
            users.push({
                username: data.username,
                message: []
            });
            ///然后触发loginSuccess事件告诉浏览器登陆成功了
            io.emit("loginSuccess",data);
        }
    });

    //发送消息
    socket.on("sendMessage",function (data) {
        for (var _user in users){
            if (users[_user].username === data.username ){
                users[_user].message.push(data.message);

                //信息存储之后触发receiveMessage将信息发给所有浏览器
                io.emit("receiveMessage",data);
                break;
            }
        }
    });

    //断线
    socket.on("disconnect",function () {

    });

});

```  













