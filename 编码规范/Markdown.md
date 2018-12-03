#Markdown#
------
-  概述
	-  宗旨
	-  兼容html
	-  特殊字符自动转换
-  区块元素
    -  段落和换行
    -  标题
    -  区块引用
    -  列表
    -  代码区块
    -  分割线
-  区段元素
	-  链接
	-  强调
	-  代码
	-  图片
-  其他
	-  反斜杠
	-  自动链接
	
-------
##概述##
###宗旨###
Markdown 的目标是实现「易读易写」。

可读性，无论如何，都是最重要的。一份使用 Markdown 格式撰写的文件应该可以直接以纯文本发布，并且看起来不会像是由许多标签或是格式指令所构成。Markdown 语法受到一些既有 text-to-HTML 格式的影响，包括 [Setext][]、[atx][]、[Textile][]、[reStructuredText][]、[Grutatext][] 和 [EtText][]，而最大灵感来源其实是纯文本电子邮件的格式。

[Setext]: www.baidu.com "Setext"
[atx]:  www.baidu.com  "atx"
[Textile]:  www.baidu.com  "Textile"
[reStructuredText]:  www.baidu.com  "reStructuredText"
[Grutatext]:  www.baidu.com  "Grutatext"
[EtText]:  www.baidu.com  "EtText"

总之， Markdown 的语法全由一些符号所组成，这些符号经过精挑细选，其作用一目了然。比如：在文字两旁加上星号，看起来就像*强调*。Markdown 的列表看起来，嗯，就是列表。Markdown 的区块引用看起来就真的像是引用一段文字，就像你曾在电子邮件中见过的那样。  

##兼容HTML##
Markdown 语法的目标是：成为一种适用于网络的书写语言。

Markdown 不是想要取代 HTML，甚至也没有要和它相近，它的语法种类很少，只对应 HTML 标记的一小部分。Markdown 的构想不是要使得 HTML 文档更容易书写。在我看来， HTML 已经很容易写了。Markdown 的理念是，能让文档更容易读、写和随意改。HTML 是一种发布的格式，Markdown 是一种书写的格式。就这样，Markdown 的格式语法只涵盖纯文本可以涵盖的范围。

不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。不需要额外标注这是 HTML 或是 Markdown；只要直接加标签就可以了。

要制约的只有一些 HTML 区块元素――比如` <div>、<table>、<pre>、<p> `等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的` <p> `标签。

##特殊字符的自动转换##
在 HTML 文件中，有两个字符需要特殊处理： `< `和 `&` 。` < `符号用于起始标签，`& `符号则用于标记 HTML 实体，如果你只是想要显示这些字符的原型，你必须要使用实体的形式，像是 `&lt`; 和 `&amp`;。

`& `字符尤其让网络文档编写者受折磨，如果你要打`「AT&T」` ，你必须要写成`「AT&amp;T」`。而网址中的 `& `字符也要转换。比如你要链接到：  

		http://images.google.com/images?num=30&q=larry+bird
你必须要把网址转换写为：  

		http://images.google.com/images?num=30&amp;q=larry+bird
才能放到链接标签的 href 属性里。不用说也知道这很容易忽略，这也可能是 HTML 标准检验所检查到的错误中，数量最多的。

Markdown 让你可以自然地书写字符，需要转换的由它来处理好了。如果你使用的 `& `字符是 HTML 字符实体的一部分，它会保留原状，否则它会被转换成 `&amp`;。  

-------
##区块元素##
###段落和换行###
一个 Markdown 段落是由一个或多个连续的文本行组成，它的前后要有一个以上的空行（空行的定义是显示上看起来像是空的，便会被视为空行。比方说，若某一行只包含空格和制表符，则该行也会被视为空行）。普通段落不该用空格或制表符来缩进。

「由一个或多个连续的文本行组成」这句话其实暗示了 Markdown 允许段落内的强迫换行（插入换行符），这个特性和其他大部分的 text-to-HTML 格式不一样（包括 Movable Type 的「Convert Line Breaks」选项），其它的格式会把每个换行符都转成 <br /> 标签。

如果你确实想要依赖 Markdown 来插入` <br /> `标签的话，在插入处先按入两个以上的空格然后回车。

的确，需要多费点事（多加空格）来产生` <br /> `，但是简单地「每个换行都转换为 <br />」的方法在 Markdown 中并不适合， Markdown 中 email 式的 区块引用 和多段落的 列表 在使用换行来排版的时候，不但更好用，还更方便阅读。  
####标题####
Markdown 支持两种标题的语法，类 Setext 和类 atx 形式。
类 Setext 形式是用底线的形式，利用 = （最高阶标题）和 - （第二阶标题），例如：  
		
		This is an H1
		=============

		This is an H2
		-------------  

类 Atx 形式则是在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶，例如：   
		
		# 这是 H1

		## 这是 H2

		##### 这是 H6  
##区块引用 Blockquotes##  
Markdown 标记区块引用是使用类似 email 中用 `>` 的引用方式。如果你还熟悉在 email 信件中的引言部分，你就知道怎么在 Markdown 文件中建立一个区块引用，那会看起来像是你自己先断好行，然后在每行的最前面加上 `> `： 
 
	> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,  
	> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.  
	> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae,risus.    
	>   
	> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse  
	>   
	> id sem consectetuer libero luctus adipiscing.  
##列表##  
Markdown 支持有序列表和无序列表。

无序列表使用星号、加号或是减号作为列表标记：

		*   Red  
		*   Green 
		*   Blue 
等同于：

		+   Red
		+   Green
		+   Blue 
也等同于：

		-   Red 
		-  Green 
		-   Blue
有序列表则使用数字接着一个英文句点：

		1.  Bird  
		2.  McHale  
		3.  Parish 
##代码区块##
和程序相关的写作或是标签语言原始码通常会有已经排版好的代码区块，通常这些区块我们并不希望它以一般段落文件的方式去排版，而是照原来的样子显示，Markdown 会用`` <pre> ``和 ``<code>`` 标签来把代码区块包起来。

要在 Markdown 中建立代码区块很简单，只要简单地缩进 4 个空格或是 1 个制表符就可以，例如，下面的输入：

	这是一个普通段落：
	
        这是一个代码区块。
Markdown 会转换成：

	<p>这是一个普通段落：</p>

	<pre><code>这是一个代码区块。
	</code></pre>

##分隔线##
你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

		* * *

		***

		*****

		- - -

		---------------------------------------

------
#区段元素#
##链接##
Markdown 支持两种形式的链接语法： 行内式和参考式两种形式。

不管是哪一种，链接文字都是用 [方括号] 来标记。

要建立一个行内式的链接，只要在方块括号后面紧接着圆括号并插入网址链接即可，如果你还想要加上链接的 title 文字，只要在网址后面，用双引号把 title 文字包起来即可，例如：

		This is [an example](http://example.com/ "Title") inline link.

		[This link](http://example.net/) has no title attribute.
参考式的链接是在链接文字的括号后面再接上另一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：

		This is [an example][id] reference-style link.
你也可以选择性地在两个方括号中间加上一个空格：

		This is [an example] [id] reference-style link.
接着，在文件的任意处，你可以把这个标记的链接内容定义出来：

		[id]: http://example.com/  "Optional Title Here"
链接内容定义的形式为：

-	方括号（前面可以选择性地加上至多三个空格来缩进），里面输入链接文字
-	接着一个冒号
-	接着一个以上的空格或制表符
-	接着链接的网址
-	选择性地接着 title 内容，可以用单引号、双引号或是括弧包着

##强调##

Markdown 使用星号（*）和底线（_）作为标记强调字词的符号，被 `*` 或 `_` 包围的字词会被转成用` <em>` 标签包围，用两个 `*` 或` _` 包起来的话，则会被转成 `<strong>`，例如：

		*single asterisks*

		_single underscores_

		**double asterisks**

		__double underscores__
会转成：

		<em>single asterisks</em>

		<em>single underscores</em>

		<strong>double asterisks</strong>

		<strong>double underscores</strong>

##代码##
如果要标记一小段行内代码，你可以用反引号把它包起来（`` ` ``），例如：

		Use the `printf()` function.
会产生：

		<p>Use the <code>printf()</code> function.</p>
代码区段的起始和结束端都可以放入一个空白，起始端后面一个，结束端前面一个，这样你就可以在区段的一开始就插入反引号：

		A single backtick in a code span: `` ` ``

		A backtick-delimited string in a code span: `` `foo` ``
会产生：

		<p>A single backtick in a code span: <code>`</code></p>

		<p>A backtick-delimited string in a code span: <code>`foo`</code></p>
##图片##

很明显地，要在纯文字应用中设计一个「自然」的语法来插入图片是有一定难度的。

Markdown 使用一种和链接很相似的语法来标记图片，同样也允许两种样式： 行内式和参考式。

行内式的图片语法看起来像是：

		![Alt text](/path/to/img.jpg)

		![Alt text](/path/to/img.jpg "Optional title")
详细叙述如下：

-	一个惊叹号 !
-	接着一个方括号，里面放上图片的替代文字
-	接着一个普通括号，里面放上图片的网址，最后还可以用引号包住并加上 选择性的 'title' 文字。  

参考式的图片语法则长得像这样：

		![Alt text][id]
「id」是图片参考的名称，图片参考的定义方式则和连结参考一样：

		[id]: url/to/image  "Optional title attribute"
到目前为止， Markdown 还没有办法指定图片的宽高，如果你需要的话，你可以使用普通的 `<img>` 标签。

-----
#其他#
##自动链接##

Markdown 支持以比较简短的自动链接形式来处理网址和电子邮件信箱，只要是用方括号包起来， Markdown 就会自动把它转成链接。一般网址的链接文字就和链接地址一样，例如：

		<http://example.com/>
Markdown 会转为：

		<a href="http://example.com/">http://example.com/</a>
邮址的自动链接也很类似，只是 Markdown 会先做一个编码转换的过程，把文字字符转成 16 进位码的 HTML 实体，这样的格式可以糊弄一些不好的邮址收集机器人，例如：

		<address@example.com>
Markdown 会转成：

		<a href="&#x6D;&#x61;i&#x6C;&#x74;&#x6F;:&#x61;&#x64;&#x64;&#x72;&#x65;
		&#115;&#115;&#64;&#101;&#120;&#x61;&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;
		&#109;">&#x61;&#x64;&#x64;&#x72;&#x65;&#115;&#115;&#64;&#101;&#120;&#x61;
		&#109;&#x70;&#x6C;e&#x2E;&#99;&#111;&#109;</a>

反斜杠

Markdown 可以利用反斜杠来插入一些在语法中有其它意义的符号，例如：如果你想要用星号加在文字旁边的方式来做出强调效果（但不用 `<em>` 标签），你可以在星号的前面加上反斜杠：

		\*literal asterisks\*
Markdown 支持以下这些符号前面加上反斜杠来帮助插入普通的符号：

		\   反斜线
		`   反引号
		*   星号
		_   底线
		{}  花括号
		[]  方括号
		()  括弧
		#   井字号
		+   加号
		-   减号
		.   英文句点
		!   惊叹号