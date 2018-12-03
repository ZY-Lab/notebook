### Handlebars模版引擎用法二  
在上一篇文章中简单的介绍了怎么使用handlebars模板，这篇文章将介绍handlebars更多的语法，相信了解后，你会被它所吸引。  

#### 之前的例子：  
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

<div id="card">

</div>

<script src="js/jquery-2.1.1.js"></script>
<script src="js/handlebars-v4.0.11.js"></script>
<script id="card-template" type="text/x-handlebars-template">
    <div class="card">
        <div>姓名：{{name}}</div>
        <div>年龄：{{age}}</div>
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
    </div>
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

##### 给js中的data添加一条数据：  
```js
var data = [{
    name: "自酌一杯酒",
    age: 22,
    home: "中国",
    job: "WEB前端工程师"
}, {
    name: "Struggle",
    age: 22,
    home: "中国",
    job: "前端工程师"
}];
```  
handlebars模版里面就需要循环data里面的数据，用each循环 `{{#each this}}….{{/each}}` ，这样就能把每一条数据都显示出来了。这儿的this指的是整个数据  
```js
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>姓名：{{name}}</div>
        <div>年龄：{{age}}</div>
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
    </div>
    {{/each}}
</script>
```  

##### 给data数组里面添加点东西:  
```js
var data = [{
    name: "自酌一杯酒",
    age: 22,
    home: "中国",
    job: "WEB前端工程师",
    books: ["伪装的艺术", "欺骗的艺术", "陷阱的艺术"]
}, {
    name: "Struggle",
    age: 22,
    home: "中国",
    job: "前端工程师",
    books: ["与上帝博弈", "比上帝还狂妄"]
}];
```  

可以看出向数组中的每个json对象添加了一个books，让它完整的显示出来，这儿也用each循环它，但需要将this换成books, `{{#each books}}….{{/each}}` .  

```js
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>姓名：{{name}}</div>
        <div>年龄：{{age}}</div>
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
        <ul>
            {{#each books}}
            <li>
                {{this}}
            </li>
            {{/each}}
        </ul>
    </div>
    {{/each}}
</script>
```  
或者也可以用这种方式：  
```js
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>姓名：{{name}}</div>
        <div>年龄：{{age}}</div>
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
        <ul>
        {{#with books}}
            {{#each this}}
            <li>{{this}}</li>
            {{/each}}
        {{/with}}
        </ul>
    </div>
    {{/each}}
</script>
```  

##### 我们向data数组里面再添加一个json对象  
```js
var data = [{
    name: "自酌一杯酒",
    age: 22,
    home: "中国",
    job: "WEB前端工程师",
    books: ["伪装的艺术", "欺骗的艺术", "陷阱的艺术"]
}, {
    name: "Struggle",
    age: 22,
    home: "中国",
    job: "前端工程师",
    books: ["与上帝博弈", "比上帝还狂妄"]
}, {
    name: "千载名",
    home: "中国",
    job: "全栈工程师",
    books: []
}];
```  

##### 最后一条与前两条相比少了一个age，如果想没有age的不让`<li>`标签显示出来，我们可以用if做个判断将`<li>`标签包裹住。  
```js
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>姓名：{{name}}</div>
        {{#if age}}
        <div>年龄：{{age}}</div>
        {{/if}}
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
        <ul>
            {{#each books}}
            <li style="color: #f55;" >
                {{this}}
            </li>
            {{/each}}
        </ul>
    </div>
    {{/each}}
</script>
```  
##### 如果要给每个卡片排序  
可以用`{{@index}}`，但这样是从阿拉伯数字 0 开始的。如果想让排序从中文一开始，我们可以自定义一个名叫”chinese”的Helper，写在js里。注意：一定要写在 “得到模版中的html”的前面。这样↓
```js
<script>
    var data = [{
        name: "自酌一杯酒",
        age: 22,
        home: "中国",
        job: "WEB前端工程师",
        books: ["伪装的艺术", "欺骗的艺术", "陷阱的艺术"]
    }, {
        name: "Struggle",
        age: 22,
        home: "中国",
        job: "前端工程师",
        books: ["与上帝博弈", "比上帝还狂妄"]
    }, {
        name: "千载名",
        home: "中国",
        job: "全栈工程师",
        books: []
    }];

    Handlebars.registerHelper("chinese",function (value) {
        var arr = ["一","二","三"];
        return arr[value];
    });

    var t = $("#card-template").html(); //得到模版中的html
    var f = Handlebars.compile(t);//预编译模版
    var h = f(data); //将数据放入模板中

    $("#card").html(h); //显示在某一个标签里面

</script>
```  
handlebars模版中就这样写  
```js
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>{{chinese @index}}</div>
        <div>姓名：{{name}}</div>
        {{#if age}}
        <div>年龄：{{age}}</div>
        {{/if}}
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
        <ul>
            {{#each books}}
            <li style="color: #f55;" >
                {{this}}
            </li>
            {{/each}}
        </ul>
    </div>
    {{/each}}
</script>
```  
##### 我们将第一本书的书名的字体颜色加上一个红色，这儿也需要自定义一个Helper，我们给标签里做判断  

js中需要这样写  
```js
Handlebars.registerHelper("isfirst",function (value,options) {
    if (value == 0){
        return options.fn(this);
    }
});
```  
handlebars模版中：  
```js
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>{{chinese @index}}</div>
        <div>姓名：{{name}}</div>
        {{#if age}}
        <div>年龄：{{age}}</div>
        {{/if}}
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
        <ul>
            {{#each books}}
            <li {{#isfirst @index}} style="color: #f55;" {{/isfirst}}>
                {{this}}
            </li>
            {{/each}}
        </ul>
    </div>
    {{/each}}
</script>
```  

#### 完整的实例：  
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        * {
            box-sizing: border-box;
            -moz-box-sizing: border-box;
            -webkit-box-sizing: border-box;
        }

        .card {
            font-size: 22px;
            margin: 20px;
            padding: 10px;
            float: left;
            background: #5cffeb;
        }
    </style>
</head>
<body>

<div id="card">

</div>


<script src="js/jquery-2.1.1.js"></script>
<script src="js/handlebars-v4.0.11.js"></script>
<script id="card-template" type="text/x-handlebars-template">
    {{#each this}}
    <div class="card">
        <div>{{chinese @index}}</div>
        <div>姓名：{{name}}</div>
        {{#if age}}
        <div>年龄：{{age}}</div>
        {{/if}}
        <div>出生地：{{home}}</div>
        <div>职业：{{job}}</div>
        <ul>
            {{#each books}}
            <li {{#isfirst @index}} style="color: #f55;" {{/isfirst}}>
                {{this}}
            </li>
            {{/each}}
        </ul>
    </div>
    {{/each}}
</script>

<script>
    var data = [{
        name: "自酌一杯酒",
        age: 22,
        home: "中国",
        job: "WEB前端工程师",
        books: ["伪装的艺术", "欺骗的艺术", "陷阱的艺术"]
    }, {
        name: "Struggle",
        age: 22,
        home: "中国",
        job: "前端工程师",
        books: ["与上帝博弈", "比上帝还狂妄"]
    }, {
        name: "千载名",
        home: "中国",
        job: "全栈工程师",
        books: []
    }];

    Handlebars.registerHelper("chinese",function (value) {
        var arr = ["一","二","三"];
        return arr[value];
    });

    Handlebars.registerHelper("isfirst",function (value,options) {
        if (value == 0){
            return options.fn(this);
        }
    });

    var t = $("#card-template").html(); //得到模版中的html
    var f = Handlebars.compile(t);//预编译模版
    var h = f(data); //将数据放入模板中

    $("#card").html(h); //显示在某一个标签里面

</script>
``` 

</body>
</html>
