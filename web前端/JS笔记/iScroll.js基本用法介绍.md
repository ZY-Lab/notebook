## iScroll.js基本用法介绍  

#### 一、iScroll是什么以及它可以做什么？  
**是什么？**  
iScroll是一款高性能，小尺寸，无依赖，多平台的javascript滚轮，可以没有滚动条的滚动。  
它适用于PC端和移动端网页，支持多平台，从Android设备到iPhone，从Chrome浏览器到Internet Explorer。  

**能做什么？**  
上拉加载，下拉刷新，图片放大镜，旋转木马...  

#### 二、iScroll的种类  
- `iscroll.js`，它是通用脚本。它包含了最常用的功能，可以在很小的空间内提供非常高的性能。  
- `iscroll-lite.js`，它是主脚本的精简版本。它不支持捕捉，滚动条，鼠标滚轮，键绑定。但是，如果您只需要滚动（尤其是在移动设备上），则iScroll Lite是最小，最快的解决方案。  
- `iscroll-probe.js`，探测当前的滚动位置是一项艰巨的任务，这就是为什么我决定为它建立一个专用的版本。如果你在任何时候都需要知道滚动的位置，这是你的iScroll。（我正在做更多的测试，这可能会以普通iscroll.js脚本结束，所以请留意一下）。  
- `iscroll-zoom.js`，将缩放添加到标准滚动。  
- `iscroll-infinite.js`，可以做无限的和缓存的滚动。处理非常长的元素列表对于移动设备来说并非易事。iScroll infinite使用缓存机制，可以让您滚动无限数量的元素。  

#### 三、入门步骤
>[iScroll.js](http://iscrolljs.com/)网站  

##### 1、html部分  
最佳的html结构  
```
<div id="wrapper">
    <ul>
        <li>...</li>
        <li>...</li>
        ...
    </ul>
</div>
```  

##### 2、CSS部分  
```
<style>
	#wrapper{
     	width: 300px;
        height: 150px;
        
        /*下面代码的是最好加上的*/
        position: relative;
     	overflow: hidden;
        /* 防止本机Windows上的触摸事件 */
        -ms-touch-action: none;
        
        /* 防止callout tap-hold和文本的选择 */
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;

        /* 防止文本调整取向变化对web应用程序很有用 */
        -webkit-text-size-adjust: none;
        -moz-text-size-adjust: none;
        -ms-text-size-adjust: none;
        -o-text-size-adjust: none;
        text-size-adjust: none;
    }
</style>
```  

##### 3、JS部分  
`<script src="js/iscroll.js"></script>`
```js
<script>
        var iscroll_demo = new IScroll('#wrapper',{
            mouseWheel: true, //鼠标滚轮支持
            scrollbars: true,//滚动条
            interactiveScrollbars: true, //滚动条变得可拖动，用户可以与之交互
            shrinkScrollbars: 'scale', //当在界限之外滚动时，滚动条被缩小一小部分。有效值是：'clip'和'scale'。
            fadeScrollbars: true, //不使用时，滚动条消失。离开这个false去腾出资源。
            keyBindings: true, //键盘控制
            useTransition: false, //这在滚动Flash，iframe和视频等敏感内容时可能很有用，但要注意：性能损失巨大。默认true
        });

        //iscroll_demo.scrollTo(0, -100); //scrollTo（x，y，时间，宽松）, 这将向下滚动100个像素。记住：0总是左上角。滚动，你必须通过负数。
        //iscroll_demo.scrollBy(0, -10);  //将向下滚动10个像素。如果你在-100，你最终会达到-110。

    </script>

```  

*以上就是iScroll的基本知识，深入学习还得多看它的官网和其他例子*