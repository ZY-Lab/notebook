### js实现页面底部内容位置显示问题详解  
相信大家在做页面的时候都会遇到一个问题，就是内容部分不足浏览器屏幕高度时，想让最底部的区域显示在浏览器屏幕的最下方。当内容部分大于浏览器屏幕高度是，又想让最底部的区域显示在内容部分的最下面。直接上代码再详细解释：  

**css代码:**  
```
*{margin:0px;padding:0px;}
.content{
    height: 1500px;
    width: 100%;
    background: #98b1d7;
    border: solid 2px #f55;
}
#footer{
	width:100%;
    height:150px;
    background: #464646;
    bottom:0px;
}
```

**HtML代码:**  
```
<div class="content">
	这是内容...
</div>
<div id="footer"> 这是底部</div>
```

**重要的js代码：**  
```js
function ct() {
    return document.compatMode == "BackCompat" ? document.body.clientHeight : document.documentElement.clientHeight;
    }
    var f = document.getElementById('footer');
    (window.onresize = function () {
        f.style.position = document.body.scrollHeight > ct() ? '' : 'fixed';
    })();
}
```

>**思路：** 内容部分不足浏览器高度时，让底部区域的位置固定在最底部`position: fixed; bottom: 0;`。否则不对底部区域位置进行操作。  

#### 对重要的js代码解释  

**1.document.compatMode**  
document.compatMode用来判断当前浏览器采用的渲染方式。  
它有两种可能的返回值：`BackCompat`和`CSS1Compat`  
>**官方解释：**  
`BackCompat`：标准兼容模式关闭。  
`CSS1Compat`：标准兼容模式开启。  
当document.compatMode等于BackCompat时，浏览器客户区宽度是`document.body.clientWidth`；  
当document.compatMode等于CSS1Compat时，浏览器客户区宽度是`document.documentElement.clientWidth`。  

**2.window.onresize**  
当浏览器被重置大小时执行里面的Javascript代码  
>为什么window.onresize = function(){ } 的外面被包裹成(window.onresize = function(){ })()？  
**那是因为window.onresize只有在屏幕发生变化时才会执行里面的js代码，外面包裹括号()后面结尾加个()是让浏览器被打开时就执行里面的代码。**  

**3.三元运算符**  
语法是 `条件 ? 结果1 : 结果2`;  
当条件为true时，返回的是结果1，否则返回结果2。  



