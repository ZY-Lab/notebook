# web端即时通讯技术
 
## 一、传统Web的通信原理

浏览器本身作为一个瘦客户端，不具备直接通过系统调用来达到和处于异地的另外一个客户端浏览器通信的功能。这和我们桌面应用的工作方式是不同的，通常桌面应用通过socket可以和远程主机上另外一端的一个进程建立TCP连接，从而达到全双工的即时通信。
浏览器从诞生开始一直走的是客户端请求服务器，服务器返回结果的模式，即使发展至今仍然没有任何改变。所以可以肯定的是，要想实现两个客户端的通信，必然要通过服务器进行信息的转发。
## 二、传统通信方式实现IM应用需要解决的问题

>● 双全工通信：

即达到浏览器拉取（pull）服务器数据，服务器推送（push）数据到浏览器；

>● 低延迟：

即浏览器A发送给B的信息经过服务器要快速转发给B，同理B的信息也要快速交给A，实际上就是要求任何浏览器能够快速请求服务器的数据，服务器能够快速推送数据到浏览器；

>● 支持跨域：

通常客户端浏览器和服务器都是处于网络的不同位置，浏览器本身不允许通过脚本直接访问不同域名下的服务器，即使IP地址相同域名不同也不行，域名相同端口不同也不行，这方面主要是为了安全考虑。

## 三、全双工低延迟的解决办法

### 1、客户端浏览器轮询服务器（polling）（每次都要发送一个请求，服务端不管数据是否发生变化都发送数据，请求完成后连接关闭）

这是最简单的一种解决方案，其原理是在客户端通过Ajax的方式的方式每隔一小段时间就发送一个请求到服务器，服务器返回最新数据，然后客户端根据获得的数据来更新界面，这样就间接实现了即时通信。优点是简单，缺点是对服务器压力较大，浪费带宽流量（通常情况下数据都是没有发生改变的）。

客户端代码如下：

	function createXHR(){
        if(typeof XMLHttpRequest !='undefined'){
            return new XMLHttpRequest();
        }else if(typeof ActiveXObject !='undefined' ){
            if(typeof arguments.callee.activeXString!="string"){
            var versions=["MSXML2.XMLHttp.6.0","MSXML2.XMLHttp.3.0",
                    "MSXML2.XMLHttp"],
                    i,len;
            for(i=0,len=versions.length;i<len;i++){
                try{
                    new ActiveXObject(versions[i]);
                    arguments.callee.activeXString=versions[i];
                    break;
                }catch(ex) {
 
                }
            }
        }
        return new ActiveXObject(arguments.callee.activeXString);
       }else{
            throw new Error("no xhr object available");
        }
    }
    function polling(url,method,data){
       method=method ||'get';
       data=data || null;
       var xhr=createXHR();
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4){
                if(xhr.status>=200&&xhr.status<300||xhr.status==304){
                    console.log(xhr.responseText);
                }else{
                    console.log("fail");
                }
            }
        };
        xhr.open(method,url,true);
        xhr.send(data);
    }
    setInterval(function(){
        polling('http://localhost:8088/time','get');
    },2000);

创建一个XHR对象，每2秒就请求服务器一次获取服务器时间并打印出来。

服务端代码（Node.js）：

	var http=require('http');
	var fs = require("fs");
	var server=http.createServer(function(req,res){
	if(req.url=='/time'){
	    //res.writeHead(200, {'Content-Type': 'text/plain','Access-Control-Allow-Origin':'http://localhost'});
	    res.end(new Date().toLocaleString());
	};
	if(req.url=='/'){
	    fs.readFile("./pollingClient.html","binary",function(err, file) {
	        if (!err) {
	            res.writeHead(200, {'Content-Type':'text/html'});
	            res.write(file,"binary");
	            res.end();
	        }
	});
	}
	}).listen(8088,'localhost');
	server.on('connection',function(socket){
	    console.log("客户端连接已经建立");
	});
	server.on('close',function(){
	    console.log('服务器被关闭');
	});

### 2、长轮询（long-polling）（保持客户端与服务端的长连接采取的是服务端阻塞（保持响应不返回），客户端轮询的方式）

这种方式是客户端发送一个请求到服务器，服务器查看客户端请求的数据是否发生了变化（是否有最新数据），如果发生变化则立即响应返回，否则保持这个连接并定期检查最新数据，直到发生了数据更新或连接超时。同时客户端连接一旦断开，则再次发出请求，这样在相同时间内大大减少了客户端请求服务器的次数。

客户端：

	function createXHR(){
        if(typeof XMLHttpRequest !='undefined'){
            return new XMLHttpRequest();
        }else if(typeof ActiveXObject !='undefined' ){
            if(typeof arguments.callee.activeXString!="string"){
                var versions=["MSXML2.XMLHttp.6.0","MSXML2.XMLHttp.3.0",
                            "MSXML2.XMLHttp"],
                        i,len;
                for(i=0,len=versions.length;i<len;i++){
                    try{
                        new ActiveXObject(versions[i]);
                        arguments.callee.activeXString=versions[i];
                        break;
                    }catch(ex) {
 
                    }
                }
            }
            return new ActiveXObject(arguments.callee.activeXString);
        }else{
            throw new Error("no xhr object available");
        }
    }
    function longPolling(url,method,data){
        method=method ||'get';
        data=data || null;
        var xhr=createXHR();
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4){
                if(xhr.status>=200&&xhr.status<300||xhr.status==304){
                    console.log(xhr.responseText);
                }else{
                    console.log("fail");
                }
                longPolling(url,method,data);
            }
        };
        xhr.open(method,url,true);
        xhr.send(data);
    }
    longPolling('http://localhost:8088/time','get');

在XHR对象的readySate为4的时候，表示服务器已经返回数据，本次连接已断开，再次请求服务器建立连接。

服务端代码：

	var http=require('http');
	var fs = require("fs");
	var server=http.createServer(function(req,res){
	    if(req.url=='/time'){
	        setInterval(function(){
	            sendData(res);
	        },20000);
	    };
	    if(req.url=='/'){
	        fs.readFile("./lpc.html","binary",function(err, file) {
	            if (!err) {
	                res.writeHead(200, {'Content-Type':'text/html'});
	                res.write(file,"binary");
	                res.end();
	            }
	        });
	    }
	}).listen(8088,'localhost');
	//用随机数模拟数据是否变化
	function sendData(res){
	    var randomNum=Math.floor(10*Math.random());
	    console.log(randomNum);
	    if(randomNum>=0&&randomNum<=5){
	        res.end(new Date().toLocaleString());
	    }
	}

### 3、基于http-stream通信

让客户端在一次请求中保持和服务端连接不断开，然后服务端源源不断传送数据给客户端，就好比数据流一样，并不是一次性将数据全部发给客户端。它与polling方式的区别在于整个通信过程客户端只发送一次请求，然后服务端保持与客户端的长连接，并利用这个连接在回送数据给客户端。

#### 3.1、基于XHR对象的streaming方式

这种方式的思想是构造一个XHR对象，通过监听它的onreadystatechange事件，当它的readyState为3的时候，获取它的responseText然后进行处理，readyState为3表示数据传送中，整个通信过程还没有结束，所以它还在不断获取服务端发送过来的数据，直到readyState为4的时候才表示数据发送完毕，一次通信过程结束。在这个过程中，服务端传给客户端的数据是分多次以stream的形式发送给客户端，客户端也是通过stream形式来获取的，所以称作http-streaming数据流方式。

客户端代码：

	function createStreamClient(url,progress,done){
        //received为接收到数据的计数器
        var xhr=new XMLHttpRequest(),received=0;
        xhr.open("get",url,true);
        xhr.onreadystatechange=function(){
            var result;
            if(xhr.readyState==3){
                //console.log(xhr.responseText);
                result=xhr.responseText.substring(received);
                received+=result.length;
                progress(result);
            }else if(xhr.readyState==4){
                done(xhr.responseText);
            }
        };
        xhr.send(null);
        return xhr;
    }
    var client=createStreamClient("http://localhost:8088/stream",function(data){
        console.log("Received:"+data);
    },function(data){
        console.log("Done,the last data is:"+data);
    })

这里由于客户端收到的数据是分段发过来的，所以最好定义一个游标received，来获取最新数据而舍弃之前已经接收到的数据，通过这个游标每次将接收到的最新数据打印出来，并且在通信结束后打印出整个responseText。

服务端代码：

	var http=require('http');
	var fs = require("fs");
	var count=0;
	var server=http.createServer(function(req,res){
	    if(req.url=='/stream'){
	        res.setHeader('content-type','multipart/octet-stream');
	        var timer=setInterval(function(){
	            sendRandomData(timer,res);
	        },2000);
	 
	    };
	    if(req.url=='/'){
	        fs.readFile("./xhr-stream.html","binary",function(err, file) {
	            if (!err) {
	                res.writeHead(200, {'Content-Type':'text/html'});
	                res.write(file,"binary");
	                res.end();
	            }
	        });
	    }
	}).listen(8088,'localhost');
	function sendRandomData(timer,res){
	    var randomNum=Math.floor(10000*Math.random());
	    console.log(randomNum);
	    if(count++==10){
	        clearInterval(timer);
	        res.end(randomNum.toString());
	    }
	        res.write(randomNum.toString());
	}

#### 3.2、基于iframe的数据流

由于低版本的IE不允许在XHR的readyState为3的时候获取其responseText属性，为了达到在IE上使用这个技术，又出现了基于iframe的数据流通信方式。具体来讲，就是在浏览器中动态载入一个iframe,让它的src属性指向请求的服务器的URL，实际上就是向服务器发送了一个http请求，然后在浏览器端创建一个处理数据的函数，在服务端通过iframe与浏览器的长连接定时输出数据给客户端，但是这个返回的数据并不是一般的数据，而是一个类似于<script type=\”text/javascript\”>parent.process(‘”+randomNum.toString()+”’)</script>脚本执行的方式，浏览器接收到这个数据就会将它解析成js代码并找到页面上指定的函数去执行，实际上是服务端间接使用自己的数据间接调用了客户端的代码，达到实时更新客户端的目的。

客户端代码如下：

	function process(data){
	            console.log(data);
	        }
	var dataStream = function (url) {
	    var ifr = document.createElement("iframe"),timer;
	    ifr.src = url;
	    document.body.appendChild(ifr);
	};
	    dataStream('http://localhost:8088/htmlfile');

服务端代码：

	var http=require('http');
	var fs = require("fs");
	var count=0;
	var server=http.createServer(function(req,res){
	    if(req.url=='/htmlfile'){
	        res.setHeader('content-type','text/html');
	        var timer=setInterval(function(){
	            sendRandomData(timer,res);
	        },2000);
	 
	    };
	    if(req.url=='/'){
	        fs.readFile("./htmlfile-stream.html","binary",function(err, file) {
	            if (!err) {
	                res.writeHead(200, {'Content-Type':'text/html'});
	                res.write(file,"binary");
	                res.end();
	            }
	        });
	    }
	}).listen(8088,'localhost');
	function sendRandomData(timer,res){
	    var randomNum=Math.floor(10000*Math.random());
	    console.log(randomNum.toString());
	    if(count++==10){
	        clearInterval(timer);
	        res.end("<script type=\"text/javascript\">parent.process('"+randomNum.toString()+"')</script>");
	    }
	    res.write("<script type=\"text/javascript\">parent.process('"+randomNum.toString()+"')</script>");
	}

#### 3.3、基于htmlfile的数据流通信

在IE中，使用iframe请求服务端，服务端保持通信连接没有全部返回之前，浏览器title一直处于加载状态，并且底部也显示正在加载，这对于一个产品来讲用户体验是不好的，于是谷歌的天才们又想出了一中hack方式。就是在IE中，动态生成一个htmlfile对象，这个对象ActiveX形式的com组件，它实际上就是一个在内存中实现的HTML文档，通过将生成的iframe添加到这个内存中的HTMLfile中，并利用iframe的数据流通信方式达到上面的效果。同时由于HTMLfile对象并不是直接添加到页面上的，所以并没有造成浏览器显示正在加载的现象。

客户端：

	function connect_htmlfile(url, callback) {
            var transferDoc = new ActiveXObject("htmlfile");
            transferDoc.open();
            transferDoc.write(
                            "<!DOCTYPE html><html><body><script  type=\"text/javascript\">" +
                            "document.domain='" + document.domain + "';" +
                            "<\/script><\/body><\/html>");
            transferDoc.close();
            var ifrDiv = transferDoc.createElement("div");
            transferDoc.body.appendChild(ifrDiv);
            ifrDiv.innerHTML = "<iframe src='" + url + "'><\/iframe>";
            transferDoc.callback=callback;
            setInterval(function () {}, 10000);
        }
        function prograss(data) {
            alert(data);
        }
        connect_htmlfile('http://localhost:8088/htmlfile',prograss);

服务端传送给iframe的是这样子：

	<script type=\"text/javascript\">callback.process('"+randomNum.toString()+"')</script>
### 4、SSE（服务器推送事件（Server-sent Events）
为了解决浏览器只能够单向传输数据到服务端，HTML5提供了一种新的技术叫做服务器推送事件SSE（关于该技术详细介绍请参见《SSE技术详解：一种全新的HTML5服务器推送事件技术》），它能够实现客户端请求服务端，然后服务端利用与客户端建立的这条通信连接push数据给客户端，客户端接收数据并处理的目的。从独立的角度看，SSE技术提供的是从服务器单向推送数据给浏览器的功能，但是配合浏览器主动请求，实际上就实现了客户端和服务器的双向通信。它的原理是在客户端构造一个eventSource对象，该对象具有readySate属性，分别表示如下：


0：正在连接到服务器；

1：打开了连接；

2：关闭了连接。

同时eventSource对象会保持与服务器的长连接，断开后会自动重连，如果要强制连接可以调用它的close方法。可以它的监听onmessage事件，服务端遵循SSE数据传输的格式给客户端，客户端在onmessage事件触发时就能够接收到数据，从而进行某种处理。

客户端：

	var source=new EventSource('http://localhost:8088/evt');
    source.addEventListener('message',function(e) {
        console.log(e.data);
    },false);
    source.onopen=function(){
        console.log('connected');
    }
    source.onerror=function(err){
        console.log(err);
    }

服务端：

	var http=require('http');
	var fs = require("fs");
	var count=0;
	var server=http.createServer(function(req,res){
	    if(req.url=='/evt'){
	        //res.setHeader('content-type', 'multipart/octet-stream');
	        res.writeHead(200, {"Content-Type":"tex" +
	            "t/event-stream","Cache-Control":"no-cache",
	            'Access-Control-Allow-Origin':'*',
	            "Connection":"keep-alive"});
	        var timer=setInterval(function(){
	            if(++count==10){
	                clearInterval(timer);
	                res.end();
	            }else{
	                res.write('id: ' + count + '\n');
	                res.write("data: " +new Date().toLocaleString() + '\n\n');
	            }
	        },2000);
	 
	    };
	    if(req.url=='/'){
	        fs.readFile("./sse.html","binary",function(err, file) {
	            if (!err) {
	                res.writeHead(200, {'Content-Type':'text/html'});
	                res.write(file,"binary");
	                res.end();
	            }
	        });
	    }
	}).listen(8088,'localhost');

## 四、跨域解决办法

#### 1、基于XHR的COSR（跨域资源共享）

ORS（跨域资源共享）是一种允许浏览器脚本向出于不同域名下服务器发送请求的技术，它是在原生XHR请求的基础上，XHR调用open方法时，地址指向一个跨域的地址，在服务端通过设置’Access-Control-Allow-Origin’:’*’响应头部告诉浏览器，发送的数据是一个来自于跨域的并且服务器允许响应的数据，浏览器接收到这个header之后就会绕过平常的跨域限制，从而和平时的XHR通信没有区别。该方法的主要好处是在于客户端代码不用修改，服务端只需要添加’Access-Control-Allow-Origin’:’*’头部即可。适用于ff,safari,opera,chrome等非IE浏览器。跨域的XHR相比非跨域的XHR有一些限制，这是为了安全所需要的，主要有以下限制：


客户端不能使用setRequestHeader设置自定义头部；

不能发送和接收cookie；

调用getAllResponseHeaders()方法总会返回空字符串。

以上这些措施都是为了安全考虑，防止常见的跨站点脚本攻击（XSS）和跨站点请求伪造（CSRF）。

客户端代码：

	var polling=function(){
        var xhr=new XMLHttpRequest();
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4)
                if(xhr.status==200){
                    console.log(xhr.responseText);
                }
            }
    xhr.open('get','http://localhost:8088/cors');
    xhr.send(null);
    };
    setInterval(function(){
        polling();
    },1000);

服务端代码：

	var http=require('http');
	var fs = require("fs");
	var server=http.createServer(function(req,res){
	    if(req.url=='/cors'){
	            res.writeHead(200, {'Content-Type':'text/plain','Access-Control-Allow-Origin':'http://localhost'});
	            res.end(new Date().toString());
	    }
	    if(req.url=='/jsonp'){
	 
	    }
	}).listen(8088,'localhost');
	server.on('connection',function(socket){
	    console.log("客户端连接已经建立");
	});
	server.on('close',function(){
	    console.log('服务器被关闭');
	});

注意服务端需要设置头部Access-Control-Allow-Origin为需要跨域的域名。


#### 2、基于XDR的CORS

对于IE8-10，它是不支持使用原生的XHR对象请求跨域服务器的，它自己实现了一个XDomainRequest对象，类似于XHR对象，能够发送跨域请求，它主要有以下限制：


cookie不会随请求发送，也不会随响应返回；

只能设置请求头部信息中的Content-Type字段；

不能访问响应头部信息；

只支持Get和Post请求；

只支持IE8-IE10。

客户端请求代码：

	var polling=function(){
        var xdr=new XDomainRequest();
        xdr.onload=function(){
            console.log(xdr.responseText);
        };
        xdr.onerror=function(){
            console.log('failed');
        };
        xdr.open('get','http://localhost:8088/cors');
        xdr.send(null);
    };
    setInterval(function(){
        polling();
    },1000);


#### 3、基于JSONP的跨域

这种方式不需要在服务端添加Access-Control-Allow-Origin头信息，其原理是利用HTML页面上script标签对跨域没有限制的特点，让它的src属性指向服务端请求的地址，其实是通过script标签发送了一个http请求，服务器接收到这个请求之后，返回的数据是自己的数据加上对客户端JS函数的调用，其原理类似于我们上面所说的iframe流的方式，客户端浏览器接收到返回的脚本调用会解析执行，从而达到更新界面的目的。

客户端代码如下：

	function callback(data){
        console.log("获得的跨域数据为:"+data);
    }
    function sendJsonp(url){
        var oScript=document.createElement("script");
        oScript.src=url;
        oScript.setAttribute('type',"text/javascript");
        document.getElementsByTagName('head')[0].appendChild(oScript);
    }
    setInterval(function(){
        sendJsonp('http://localhost:8088/jsonp?cb=callback');
    },1000);

服务端代码：

	var http=require('http');
	var url=require('url');
	var server=http.createServer(function(req,res){
	    if(/\/jsonp/.test(req.url)){
	        var urlData=url.parse(req.url,true);
	        var methodName=urlData.query.cb;
	        res.writeHead(200,{'Content-Type':'application/javascript'});
	        //res.end("<script type=\"text/javascript\">"+methodName+"("+new Date().getTime()+");</script>");
	        res.end(methodName+"("+new Date().getTime()+");");
	        //res.end(new Date().toString());
	    }
	}).listen(8088,'localhost');
	server.on('connection',function(socket){
	    console.log("客户端连接已经建立");
	});
	server.on('close',function(){
	    console.log('服务器被关闭');
	});

注意这里服务端输出的数据content-type首部要设定为application/javascript,否则某些浏览器会将其当做文本解析。

## 五、WebSocket

在上面的这些解决方案中，都是利用浏览器单向请求服务器或者服务器单向推送数据到浏览器这些技术组合在一起而形成的hack技术，在HTML5中，为了加强web的功能，提供了websocket技术，它不仅是一种web通信方式，也是一种应用层协议。它提供了浏览器和服务器之间原生的双全工跨域通信，通过浏览器和服务器之间建立websocket连接（实际上是TCP连接）,在同一时刻能够实现客户端到服务器和服务器到客户端的数据发送。关于该技术的原理，请参见：《[WebSocket详解（一）：初步认识WebSocket技术](http://www.52im.net/forum.php?mod=viewthread&tid=331&ctid=15)》、《[WebSocket详解（二）：技术原理、代码演示和应用案例](http://www.52im.net/forum.php?mod=viewthread&tid=326&ctid=15)》、《[WebSocket详解（三）：深入WebSocket通信协议细节](http://www.52im.net/forum.php?mod=viewthread&tid=332&ctid=15)》，此处就不在赘述了，直接给出代码。在看代码之前，需要先了解websocket整个工作过程。

首先是客户端new 一个websocket对象，该对象会发送一个http请求到服务端，服务端发现这是个webscoket请求，会同意协议转换，发送回客户端一个101状态码的response，以上过程称之为一次握手，经过这次握手之后，客户端就和服务端建立了一条TCP连接，在该连接上，服务端和客户端就可以进行双向通信了。这时的双向通信在应用层走的就是ws或者wss协议了，和http就没有关系了。所谓的ws协议，就是要求客户端和服务端遵循某种格式发送数据报文（帧），然后对方才能够理解。

![](https://i.imgur.com/Dx5hDOV.png)

其中比较重要的是FIN字段，它占用1位，表示这是一个数据帧的结束标志，同时也下一个数据帧的开始标志。opcode字段，它占用4位，当为1时，表示传递的是text帧，2表示二进制数据帧，8表示需要结束此次通信（就是客户端或者服务端哪个发送给对方这个字段，就表示对方要关闭连接了）。9表示发送的是一个ping数据。mask占用1位，为1表示masking-key字段可用，masking-key字段是用来对客户端发送来的数据做unmask操作的。它占用0到4个字节。Payload字段表示实际发送的数据，可以是字符数据也可以是二进制数据。

所以不管是客户端和服务端向对方发送消息，都必须将数据组装成上面的帧格式来发送。

服务端代码：

	//握手成功之后就可以发送数据了
	var crypto = require('crypto');
	var WS = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11';
	var server=require('net').createServer(function (socket) {
	    var key;
	    socket.on('data',function (msg) {
	        if (!key) {
	            //获取发送过来的Sec-WebSocket-key首部
	            key = msg.toString().match(/Sec-WebSocket-Key: (.+)/)[1];
	            key = crypto.createHash('sha1').update(key + WS).digest('base64');
	            socket.write('HTTP/1.1 101 Switching Protocols\r\n');
	            socket.write('Upgrade: WebSocket\r\n');
	            socket.write('Connection: Upgrade\r\n');
	            //将确认后的key发送回去
	            socket.write('Sec-WebSocket-Accept: ' + key + '\r\n');
	            //输出空行，结束Http头
	            socket.write('\r\n');
	        }else {
	            var msg=decodeData(msg);
	            console.log(msg);
	            //如果客户端发送的操作码为8,表示断开连接,关闭TCP连接并退出应用程序
	            if(msg.Opcode==8){
	                socket.end();
	                server.unref();
	            }else{
	                socket.write(encodeData({FIN:1,
	                    Opcode:1,
	                    PayloadData:"接受到的数据为"+msg.PayloadData}));
	            }
	 
	        }
	    });
	});
	    server.listen(8000,'localhost');
	//按照websocket数据帧格式提取数据
	function decodeData(e){
	    var i=0,j,s,frame={
	        //解析前两个字节的基本数据
	        FIN:e[i]>>7,Opcode:e[i++]&15,Mask:e[i]>>7,
	        PayloadLength:e[i++]&0x7F
	    };
	    //处理特殊长度126和127
	    if(frame.PayloadLength==126)
	        frame.length=(e[i++]<<8)+e[i++];
	    if(frame.PayloadLength==127)
	        i+=4,//长度一般用四字节的整型，前四个字节通常为长整形留空的
	            frame.length=(e[i++]<<24)+(e[i++]<<16)+(e[i++]<<8)+e[i++];
	    //判断是否使用掩码
	    if(frame.Mask){
	        //获取掩码实体
	        frame.MaskingKey=[e[i++],e[i++],e[i++],e[i++]];
	        //对数据和掩码做异或运算
	        for(j=0,s=[];j<frame.PayloadLength;j++)
	            s.push(e[i+j]^frame.MaskingKey[j%4]);
	    }else s=e.slice(i,frame.PayloadLength);//否则直接使用数据
	    //数组转换成缓冲区来使用
	    s=new Buffer(s);
	    //如果有必要则把缓冲区转换成字符串来使用
	    if(frame.Opcode==1)s=s.toString();
	    //设置上数据部分
	    frame.PayloadData=s;
	    //返回数据帧
	    return frame;
	}
	//对发送数据进行编码
	function encodeData(e){
	    var s=[],o=new Buffer(e.PayloadData),l=o.length;
	    //输入第一个字节
	    s.push((e.FIN<<7)+e.Opcode);
	    //输入第二个字节，判断它的长度并放入相应的后续长度消息
	    //永远不使用掩码
	    if(l<126)s.push(l);
	    else if(l<0x10000)s.push(126,(l&0xFF00)>>2,l&0xFF);
	    else s.push(
	            127, 0,0,0,0, //8字节数据，前4字节一般没用留空
	                (l&0xFF000000)>>6,(l&0xFF0000)>>4,(l&0xFF00)>>2,l&0xFF
	        );
	    //返回头部分和数据部分的合并缓冲区
	    return Buffer.concat([new Buffer(s),o]);
	}

服务端通过监听data事件来获取客户端发送来的数据，如果是握手请求，则发送http 101响应，否则解析得到的数据并打印出来，然后判断是不是断开连接的请求（Opcode为8），如果是则断开连接，否则将接收到的数据组装成帧再发送给客户端。

客户端代码：

	window.onload=function(){
        var ws=new WebSocket("ws://127.0.0.1:8088");
        var oText=document.getElementById('message');
        var oSend=document.getElementById('send');
        var oClose=document.getElementById('close');
        var oUl=document.getElementsByTagName('ul')[0];
        ws.onopen=function(){
            oSend.onclick=function(){
                if(!/^\s*$/.test(oText.value)){
                    ws.send(oText.value);
                }
            };
 
        };
        ws.onmessage=function(msg){
          var str="<li>"+msg.data+"</li>";
          oUl.innerHTML+=str;
        };
        ws.onclose=function(e){
            console.log("已断开与服务器的连接");
            ws.close();
        }
    }

客户端创建一个websocket对象，在onopen时间触发之后（握手成功后），给页面上的button指定一个事件，用来发送页面input当中的信息，服务端接收到信息打印出来，并组装成帧返回给日客户端，客户端再append到页面上。

## 结束语

面论述了这么多对于IM应用开发所涉及到的通信方式，在实际开发中，我们通常使用的是一些别人写好的实时通讯的库，比如[socket.io](http://www.52im.net/forum.php?mod=viewthread&tid=190&ctid=15)、[sockjs](https://github.com/sockjs/sockjs-client)，他们的原理就是将上面（还有一些其他的如基于Flash的push）的一些技术进行了在客户端和服务端的封装，然后给开发者一个统一调用的接口。这个接口在支持websocket的环境下使用websocket，在不支持它的时候启用上面所讲的一些hack技术。

从实际来讲，单独使用本文上述所讲的任何一种技术（WebSocket除外）达不到我们在文章开头提出的低延时，双全工、跨域的全部要求，只有把他们组合起来才能够很好地工作，所以通常情况下，这些库都是在不同的浏览器上采用各种不同的组合来实现实时通讯的。

下面是sockjs在不同浏览器下面采取的不同组合方式：

![](https://i.imgur.com/d3mrLix.png)