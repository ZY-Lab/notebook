###JavaScript基础
####一、JavaScript数据类型
**1、数据类型**
- number：数字
- true/false：逻辑值
- string：字符串
- null：没有值
- undefined：没有定义的值

**2、判断变量的类型**
```
type(变量名)
```
####二、function函数
**1、定义函数的方式**
-  函数声明的方式
-  函数表达的方式

**2、用函数声明的方式定义函数**

>例如：定义函数弹出alert

```JavaScript
function alertMessage(message){
alert(message);
}
//调用函数：
alertMessage('hello');

```
**3、用函数表达式的方式定义函数**

理解：通过定义一个匿名的函数，交个定义的一个变量
```JavaScript
var alertMessage = function(message){
alert(message);
}
//调用函数：
alertMessage('hello');
```
####三、对象
**1、对象Object**
- 对象的属性（property）
- 对象的方法（method）

**2、创建对象**

>创建空对象

```JavaScript
var beyond={};
```

>设置对象的属性

```JavaScript
//通过.的形式：
beyond.formeIn='1986';
//通过[]的形式：
beyond['foundedIn']='香港';
```

>创建对象时设置对象的属性

```JavaScript
var beyond={formeIn:"1983",foundedIn:"香港"};
```
>输出对象

```JavaScript
console.log(beyond);

```
结果：Object{formeIn:"1983",foundedIn:"香港"}

**3、访问属性的值**
>通过.的方式

```JavaScript
byeond.formeIn
```
结果“1983”
>通过[]的形式

```JavaScript
byeond['formeIn']
```
结果“1983”

**4、对象里面添加数组**
```JavaScript
var beyond={
formedIn:'1983',
foundedIn:'香港',
artist:['A','B','C','D']

console.log(beyond);
};
```
结果：Object{formeIn:"1983",foundedIn:"香港"，artist:Array[4]}

**5、为对象添加方法**
```JavaScript
beyond.showArtist=function(){
for(var i=0;i<this.artist.length;i++){
document.writeln(this.artist[i]);
}
};
```
**注：this代表了对象本身**
>调用对象的方法：

```JavaScript
beyond.showArtist();
```
结果：A B C D

**6、循环的输出对象里的属性**
>输出一个对象里的所有属性（for....in）

```JavaScript
var property;//作为属性的名称
for(property in beyond){
if(typeof beyond[property]!=='function'){
console.log(beyond[property]);
}
}
```
####三、DOM操作文档的接口

**1.文档对象模型DOM**
**2.文档树DOM tree**

![输入图片说明](https://git.oschina.net/uploads/images/2017/0721/171619_73c55713_684224.png "QQ截图20170721121703.png")

**3.获取文档中的元素**

![输入图片说明](https://git.oschina.net/uploads/images/2017/0721/171658_b38f12ba_684224.png "QQ截图20170721121854.png")

1.通过getElementsById获取元素

```JavaScript
document.getElementById('page-title')

//结果：<h1 id="page-title">Coldplay</h1>
```
2.通过getElementsByTagName获取元素

```JavaScript
//通过html标签的名称获取元素
document.getElementsByTagName('li')

//结果为：标签为<li>的数组
```

3.通过querySelector和querySelectorAll获取元素
```JavaScript
document.querySelectorAll('.artist-list li')

//结果：返回artist-list中的所有li标签


document.querySelector('.artist-list li')

//结果：返回artist-list中的第一个li标签
```

**4.在文档中创建并插入新的节点**

1、创建新节点
>创建元素类型的节点：createElement
>创建文本类型的节点：createTextNode
>把节点插入到指定的地方：appendChild或insertBefore

例如：

![输入图片说明](https://git.oschina.net/uploads/images/2017/0721/172324_0209ac18_684224.png "QQ截图20170721144020.png")
![输入图片说明](https://git.oschina.net/uploads/images/2017/0721/172340_2fa63887_684224.png "QQ截图20170721145031.png")

2、insertBefore在指定的位置插入节点
```JavaScript
var artistList=document.querySelector('.artist-list');
artistList.insertBefore(newMember,artistList.firstChild)//参数1：要插入的内容；参数2：插入的位置
```
结果：
![输入图片说明](https://git.oschina.net/uploads/images/2017/0721/172447_abd53a96_684224.png "QQ截图20170721145958.png")

####四、Event处理发生的事情

**1、处理事件的方法**
- 在元素里使用事件的属性
- 元素事件处理的属性
- addEventListener为元素绑定事件

**2、事件的另一种传播方式：事件的捕获方式**
addEventListener()的第三个参数：
- true:事件通过捕获的方式进行传播
- false:事件会用冒泡的方式进行传播

![输入图片说明](https://git.oschina.net/uploads/images/2017/0721/173032_b481bc45_684224.png "QQ截图20170721164020.png")
```JavaScript
//获取listGroup
 var listGroup=document.querySelector('.list-group');
//添加事件响应函数
function showMessage(event){
console.log(“点击了ul”);//
}
//为listGroup添加监听事件
listGroup.addEventListener('click',showMessage,false);

var lost=document.getElementById('lost');
function showMnotherMessage(event){
console.log('点击了lost');
}
lost.addEventListener('click',showMnotherMessage,false);
```

 **先点击其他图片，再点击lost图片，结果：** 

```
点击了ul
点击了lost
点击了ul
```

>修改传播方式：

```JavaScript
listGroup.addEventListener('click',showMessage,true);
```
 **点击lost图片,结果：** 
```
点击了ul
点击了lost
```

