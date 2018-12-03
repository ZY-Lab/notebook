**1、每逢大的灾难的时候，很多网站变成了灰色，如何让网站快速变灰？css代码是很简单的，用的是css的filter功能。**
```
html {
   filter: grayscale(100%);//IE浏览器
  -webkit-filter: grayscale(100%);//谷歌浏览器
  -moz-filter: grayscale(100%);//火狐
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter:progid:DXImageTransform.Microsoft.BasicImage(grayscale=1);
  -webkit-filter: grayscale(1);//谷歌浏览器
}
```
> 有一些网站FLASH动画的颜色不能被CSS滤镜控制，可以在FLASH代码的和之间插入

```
//html代码
<param value="false" name="menu"/>
<param value="opaque" name="wmode"/>
```
**2、DIV可编辑，就是让一个div变成一个类似input输入框的效果**。
 在div中添加contentEditable="true" 属性就可以了，如下：
```
 <div id="div1" contentEditable="true"  ></div>
```
**3、有些网站为了不让用户复制，设置了div禁止选择的功能，设置如下属性：**
```
unselectable="on" onselectstart="return false;"
```
**4、CSS 中form表单两端对齐**
做form表单的时候，前面经常有姓名，年龄，公司名称等等，有的是2个字，有的是4个字，如何让字对齐呢？有的人的做法是打几个空格，但是这样不是很准确，最好的办法是如下：
```
	td  {
		text-align:justify;
		}
td:after{
		 content:"";
		 display: inline-block;
		 width:100%;
		}

```
**5、input声音录入按钮，（仅支持谷歌）**
```
<!-- 添加 x-webkit-speech 属性就可以了。 -->
<input type="text" class="box" name="s" id="s" class="inputText" placeholder="输入关键词"  x-webkit-speech>
```
**6、给input的placeholder设置颜色**
```
::-webkit-input-placeholder { /* WebKit browsers */
    color:    #999;
}
:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
    color:    #999;
}
::-moz-placeholder { /* Mozilla Firefox 19+ */
    color:    #999;
}
:-ms-input-placeholder { /* Internet Explorer 10+ */
    color:    #999;
}
```
**7、css3实现一个div设置多张背景图片及background-image属性**

```
div{
	background:url("1.jpg") 0 0 no-repeat,
             url("2.jpg") 200px 0 no-repeat,
             url("3.jpg") 400px 201px no-repeat;
}
/* 也可以这么写 */
div{
	background-image:url("1.jpg"),url("2.jpg"),url("3.jpg");
	background-repeat: no-repeat, no-repeat, no-repeat;  
	background-position: 0 0, 200px 0, 400px 201px; 
}
```
**8、CSS选中状态修改 **
```
<!DOCTYPE html>
<html lang="zh">
<head>
	<meta charset="UTF-8" />
	<style type="text/css">
		::selection {
			background: yellowgreen;
			color: red;
		}
	</style>
</head>
<body>
	<p>我虽然是一个段落标签，但经常被人冷落。</p>
</body>
</html>
```
**9、css input[type=file] 样式美化，input上传按钮美化**
```
		.file {
		    position: relative;
		    display: inline-block;
		    background: #D0EEFF;
		    border: 1px solid #99D3F5;
		    border-radius: 4px;
		    padding: 4px 12px;
		    overflow: hidden;
		    color: #1E88C7;
		    text-decoration: none;
		    text-indent: 0;
		    line-height: 20px;
		}
		.file input {
		    position: absolute;
		    font-size: 100px;
		    right: 0;
		    top: 0;
		    opacity: 0;
		}
		.file:hover {
		    background: #AADFFD;
		    border-color: #78C3F3;
		    color: #004974;
		    text-decoration: none;
		}
```

**10、CSS :after 和：before选择器**
```
.test-div{
		    position: relative;  /*日常相对定位*/
		    width:150px;
		    height:36px;
		    border-radius:5px;
		    border:black 1px solid;
		    background: rgba(245,245,245,1)
		}
		.test-div:before{
		    content: "";  /*:before和:after必带技能，重要性为满5颗星*/
		    display: block;
		    position: absolute;  /*日常绝对定位*/
		    top:8px;
		    width: 0;
		    height: 0;
		    border:6px solid transparent;
		    left:-12px;
		    border-right-color: #000;
		}
```
**11、透明度**
```
div{
    opacity: .9; 
    filter:alpha(opacity=90)
}
/* IE7和IE6中opacity是没有用的，在IE6中DIV透明的方法一般用filter； */
.div{
    opacity: 0; 
    cursor:pointer; 
    -ms-filter:"progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
    filter: alpha(opacity=0);
}
```

**12、超出长度显示省略号**
```
单行文本显示...
/* 一般要指定宽度，然后给如下四个属性。 */
		span{
			width:200px;
			display:block;
			overflow:hidden;
			white-space:nowrap;
			text-overflow:ellipsis;
		}
```

```
多行文本显示.... （主要属性-webkit-line-clamp）
	/* 一般要指定宽度，然后给如下四个属性。 */
		p {
			width: 200px;
		    overflow : hidden;
		    text-overflow: ellipsis;
		    display: -webkit-box;
		    -webkit-line-clamp: 2;
		    -webkit-box-orient: vertical;
		}
```
**13、阴影效果**
```
/* 盒子阴影 */
box-shadow: 2px 2px 10px 4px #333333;	
/* 文子阴影 */
text-shadow: 1px 1px 0px #fff;
```

**14、CSS强制换行和不换行**

```
/* 自动换行 */
div{ 
	word-wrap: break-word; 
	word-break: normal; 
}
/* 强制英文单词断行 */ 

div{
	word-break:break-all;
}
/* 强制不换行 */

div{
	white-space:nowrap;
}
```
**15、CSS 圆角**
IE 9、Opera 10.5、Safari 5、Chrome 4和Firefox 4，都支持上述的border-radius属性。早期版本的Safari和Chrome，支持-webkit-border-radius属性，早期版本的Firefox支持-moz-border-radius属性。 目前来看，为了保证兼容性，只需同时设置-moz-
border-radius和border-radius即可。
```
-moz-border-radius: 15px;
border-radius: 15px;
/* （注意：border-radius必须放在最后声明，否则可能会失效。） */

/* 另外，早期版本Firefox的单个圆角的语句，与标准语法略有不同。 */
-moz-border-radius-topleft（标准语法：border-top-left-radius）
-moz-border-radius-topright（标准语法：border-top-right-radius）
-moz-border-radius-bottomleft（标准语法：border-bottom-left-radius）
-moz-border-radius-bottomright（标准语法：border-bottom-right-radius）
```
**16. 表格单元格等宽**
表格工作起来很麻烦，所以务必尽量使用 table-layout: fixed 来保持单元格的等宽：
```
.calendar {
  table-layout: fixed;
}
```
**17、textarea禁止拖动**
```
resize: none; //禁止拖动
/* 
以下是resize属性的的各个取值：
    none：用户不能操纵机制调节元素的尺寸；
    both：用户可以调节元素的宽度和高度；
    horizontal：用户可以调节元素的宽度；
    vertical：让用户可以调节元素的高度；
    inherit：默认继承。
*/
```
**19、CSS3的一些前缀总结**
css3为了更好的兼容多个浏览器，通常前面加一大堆前缀，有时候感觉很烦，前缀也容易忘记或者漏掉。下面总结一下！
```
-webkit  为Chrome/Safari
-moz  为Firefox
-ms   为IE
-o 为Opera
```
**20、css3的box-sizing**
给了两个并排带边框的div百分比宽度，假如不用box-sizing，边框的宽度会在行内显示。用box-sizing：border-box,可以去除边框的占位，通俗讲它就是一个铁盒子，浏览器支持IE9以上及火狐、谷歌、Opera等等
```
	.container{
			width: 400px;
			height: 40px;
			border: 2px solid #333333;
			padding: 10px;
		}
	.container.box{
			box-sizing:border-box;
			-moz-box-sizing:border-box; /* Firefox */
			-webkit-box-sizing:border-box; /* Safari */
			width:50%;
			border:2px solid red;
			float:left;
		}
```
> 语法：box-sizing: content-box|border-box|inherit;

**21、模糊遮罩效率，模糊滤镜效果**
```
-webkit-filter: blur(3px);
-moz-filter: blur(3px);
-o-filter: blur(3px);
-ms-filter: blur(3px);
filter: blur(3px);
```
**22、渐变效果**
1.  背景渐变

默认渐变是从上往下代码如下：
```
background:#ed4a60; 
background: -webkit-linear-gradient(#ed5a5e, #ed3a61);
background: -o-linear-gradient(#ed5a5e, #ed3a61); 
 background: -moz-linear-gradient(#ed5a5e, #ed3a61); 
background: linear-gradient(#ed5a5e, #ed3a61);
```
前面加一个参数，right,left,bottom,top等，就可以指定渐变方向：
```
background:-moz-linear-gradient(left,#ace,#f96);/*Mozilla*/
background:-webkit-gradient(linear,0 50%,100% 50%,from(#ace),to(#f96));/*Old gradient for webkit*/
background:-webkit-linear-gradient(left,#ace,#f96);/*new gradient for Webkit*/
background:-o-linear-gradient(left,#ace,#f96); /*Opera11*/
```
还可以从左上角开始渐变left top，right top(右上角)以此类推，代码如下：
```
background: -moz-linear-gradient(left top, #ace, #f96);
background: -webkit-linear-gradient(left top, #ace, #f96);
background: -o-linear-gradient(left top, #ace, #f96);
```
另外还可以指定渐变角度，这个角度是一个由水平线与渐变线产生的的角度，逆时针方向。因此，使用0deg将产生一个左到右横向梯度，而90度将创建一个从底部到顶部的垂直渐变。
代码如下
```
background: -moz-linear-gradient(<angle>, #ace, #f96);
background: -webkit-gradient(<type>,<angle>, from(#ace), to(#f96));//老的写法
background: -webkit-linear-gradient(<angle>, #ace, #f96);
background: -o-linear-gradient(<angle>, #ace, #f96);

.deg45 {
  background: -moz-linear-gradient(45deg, #ace, #f96);
  background: -webkit-gradient(linear,0 100%,100% 0%,from(#ace),to(#f96));
  background: -webkit-linear-gradient(45deg, #ace, #f96);
  background: -o-linear-gradient(45deg, #ace, #f96);
}
```

2.边框渐变
```
border-image: -webkit-linear-gradient( #b5a76f, #a79c64,#938b5d, #b5a76f) 1 1;
```

3.文字渐变

```
background: -webkit-linear-gradient(left, rgb(194,169,99), rgb(255,243,182) 5%, rgb(194,169,99), rgb(255,243,182) 95%, rgb(194,169,99));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
```