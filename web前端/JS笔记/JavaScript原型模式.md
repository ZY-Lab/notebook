#### 原型的方法创建对象
我们创建的每个函数都有一个prototype(原型)属性，这个属性是一个对象，它的用途是包含可以由特定类型的所有实例共享的属性和方法。逻辑上可以这么理解：prototype通过调用构造函数而创建的那个对象的原型对象。使用原型的好处可以让所有对象实例共享它所包含的属性和方法。也就是说，不必在构造函数中定义对象信息，而是可以直接将这些信息添加到原型中。
```
function Box() {}			//构造函数函数体内什么都没有，这里如果有，叫做实例属性，实例方法

Box.prototype.name = 'Lee';				//原型属性
Box.prototype.age = 100;					//原型属性
Box.prototype.run = function () {		//原型方法
	return this.name + this.age + '运行中...';
};

var box1 = new Box();
```
比较一下原型内的方法地址是否一致：
```
var box1 = new Box();
var box2 = new Box();
alert(box1.run == box2.run);					//true，方法的引用地址保持一致
```
回顾构造函数
```
function Box(name, age) {
	this.name = name;										//实例属性
	this.age = age;
	this.run = function () {								//实例方法
		return this.name + this.age + '运行中...';
	};
}
var box1 = new Box('Lee', 100);	//实例化后地址为1
var box2 = new Box('Lee', 100);  //实例化后地址为2
alert(box1.run == box2.run);	//false		//因为他们比较的是引用地址，
```
*
//如果是原型方法，那么他们地址是共享的，大家都是一样
//如果是实例方法，不同的实例化，他们的方法地址是不一样的，是唯一的
*


在原型模式声明中，多了两个属性，这两个属性都是创建对象时自动生成的。__proto__属性是实例指向原型对象的一个指针，它的作用就是指向构造函数的原型属性constructor。通过这两个属性，就可以访问到原型里的属性和方法了。

PS：IE浏览器在脚本访问__proto__会不能识别，火狐和谷歌浏览器及其他某些浏览器均能识别。虽然可以输出，但无法获取内部信息。


```
alert(box1.prototype);			//这个属性是一个对象，访问不到
alert(Box.prototype);			//使用构造函数名(对象名)访问prototype
alert(box1.__proto__);			//这个属性是一个指针指向prototype原型对象


alert(box1.constructor);			//构造属性，可以获取构造函数本身
												//作用是被原型指针定位，然后得到构造函数本身
												//其实就是对象实例对应的原型对象的作用
```
判断一个对象实例(对象引用)是不是指向了原型对象，基本上，只要实例化了，他自动指向的,可以使用isPrototypeOf()方法来测试。
```
alert(Box.prototype.isPrototypeOf(box));		//只要实例化对象，即都会指向
```

###### 原型模式的执行流程：
1.先查找构造函数实例里的属性或方法，如果有，立刻返回；
2.如果构造函数实例里没有，则去它的原型对象里找，如果有，就返回；

虽然我们可以通过对象实例访问保存在原型中的值，但却不能访问通过对象实例重写原型中的值。

```
var box1 = new Box();
alert(box1.name);							//Lee，原型里的值
delete box1.name;							//删除实例中的属性
//delete Box.prototype.name;			//删除原型中的属性（不常用）
//Box.prototype.name = 'KK';			//覆盖原型中的属性（不常用）

box1.name = 'Jack';
alert(box.1name);							//Jack，就近原则，

var box2 = new Box();						
alert(box2.name);							//Lee，原型里的值，没有被box1修改
```

如何判断属性是在构造函数的实例里？可以使用hasOwnProperty()函数来验证：
```
alert(box1.hasOwnProperty('name'));			//实例里有返回true，否则返回false
```

in操作符会在通过对象能够访问给定属性时返回true，无论该属性存在于实例中还是原型中。
```
alert('name' in box1);						//true，存在实例中或原型中
```
我们可以通过hasOwnProperty()方法检测属性是否存在实例中，也可以通过in来判断实例或原型中是否存在属性。那么结合这两种方法，可以判断原型中是否存在属性。
```
//判断只有原型中有属性，
function isProperty(object, property) {
	return !object.hasOwnProperty(property) && (property in object)
}
var box = new Box();
alert(isProperty(box, 'name'))					//true，如果原型有
```

###### 为了让属性和方法更好的体现封装的效果，并且减少不必要的输入，原型的创建可以使用字面量的方式：

//使用字面量的方式创建原型对象，这里{}就是对象，是Object，new Object就相当于{}
```
function Box() {};
Box.prototype = {
	constructor : Box,			//强制指向Box
	name : 'Lee', 
	age : 100,
	run : function () {
		return this.name + this.age + '运行中...';
	}
};
```
使用构造函数创建原型对象和使用字面量创建对象在使用上基本相同，但还是有一些区别，字面量创建的方式使用constructor属性不会指向实例，而会指向Object，构造函数创建的方式则相反。
```
var box = new Box();
alert(box instanceof Box);
alert(box instanceof Object);
alert(box.constructor == Box);				//字面量方式，返回false，否则，true
alert(box.constructor == Object);				//字面量方式，返回true，否则，false
```

如果想让字面量方式的constructor指向实例对象，那么可以这么做：
```
Box.prototype = {
	constructor : Box,						//直接强制指向即可
};
```

PS：字面量方式为什么constructor会指向Object？因为Box.prototype={};这种写法其实就是创建了一个新对象。而每创建一个函数，就会同时创建它prototype，这个对象也会自动获取constructor属性。所以，新对象的constructor重写了Box原来的constructor，因此会指向新对象，那个新对象没有指定构造函数，那么就默认为Object。

原型模式创建对象也有自己的缺点，它省略了构造函数传参初始化这一过程，带来的缺点就是初始化的值都是一致的。而原型最大的缺点就是它最大的优点，那就是共享。
原型中所有属性是被很多实例共享的，共享对于函数非常合适，对于包含基本值的属性也还可以。但如果属性包含引用类型，就存在一定的问题：


```
//原型的缺点

function Box() {}

Box.prototype = {
	constructor : Box, 
	name : 'Lee', 
	age : 100,
	family : ['哥哥','姐姐','妹妹'],
	run : function () {
		return this.name + this.age + '运行中...'
	}
};
var box1 = new Box();
alert(box1.family);
box1.family.push('弟弟');			//在第一个实例修改后引用类型，保持了共享
alert(box1.family);

var box2 = new Box();
alert(box2.family);					//共享了box1添加后的引用类型的原型
```
为了解决构造传参和共享问题，可以组合构造函数+原型模式
```
//组合构造函数+原型模式

function Box(name, age) {		//保持独立的用构造函数
	this.name = name;
	this.age = age;
	this.family = ['哥哥','姐姐','妹妹'];
}

Box.prototype = {					//保持共享的用原型
	constructor : Box,
	run : function () {
		return this.name + this.age + '运行中...'
	}
};


var box1 = new Box('Lee', 100);
//alert(box1.run());
alert(box1.family);
box1.family.push('弟弟');		
alert(box1.family);

var box2 = new Box('Jack', 200);
//alert(box2.run());
alert(box2.family);					//引用类型没有使用原型，所以没有共享
```
PS：这种混合模式很好的解决了传参和引用共享的大难题。是创建对象比较好的方法。

原型模式，不管你是否调用了原型中的共享方法，它都会初始化原型中的方法，并且在声明一个对象时，构造函数+原型部分让人感觉又很怪异，最好就是把构造函数和原型封装到一起。为了解决这个问题，我们可以使用**动态原型模式**。


```
//动态原型模式

//可以将原型封装到构造函数里
function Box(name, age) {		
	this.name = name;
	this.age = age;
	this.family = ['哥哥','姐姐','妹妹'];
	
	if (typeof this.run != 'function') {				//判断this.run是否存在
		Box.prototype.run = function() {
			return this.name + this.age + '运行中...'
		};
	}
}
var box = new Box('Lee', 100);
alert(box.run());
```

当第一次调用构造函数时，run()方法发现不存在，然后初始化原型。当第二次调用，就不会初始化，并且第二次创建新对象，原型也不会再初始化了。这样及得到了封装，又实现了原型方法共享，并且属性都保持独立。

以上讲解了各种方式对象创建的方法，如果这几种方式都不能满足需求，可以使用一开始那种模式：**寄生构造函数**。
```
//寄生构造函数 = 工厂模式 + 构造函数
function Box(name, age) {
	var obj = new Object();
	obj.name = name;
	obj.age = age;
	obj.run = function () {
		return this.name + this.age + '运行中...'
	};
	return obj;
}


var box1 = new Box('Lee', 100);
alert(box1.run());

var box2 = new Box('Jack', 200);
alert(box2.run());
```

寄生构造函数，其实就是工厂模式+构造函数模式。这种模式比较通用，但不能确定对象关系，所以，在可以使用之前所说的模式时，不建议使用此模式。
在什么情况下使用寄生构造函数比较合适呢？假设要创建一个具有额外方法的引用类型。由于之前说明不建议直接
```
String.prototype.addstring，可以通过寄生构造的方式添加。
function myString(string) {					
	var str = new String(string);
	str.addstring = function () {
		return this + '，被添加了！';
	};
	return str;
}

var box = new myString('Lee');				//比直接在引用原型添加要繁琐好多
alert(box.addstring());
```

在一些安全的环境中，比如禁止使用this和new，这里的this是构造函数里不使用this，这里的new是在外部实例化构造函数时不使用new。这种创建方式叫做稳妥构造函数。 
```
function Box(name , age) {
	var obj = new Object();
    obj.name = name;
	obj.age = age;
	obj.run = function () {
		return name + age + '运行中...';		//直接打印参数即可
	};
	return obj;
}
var box = Box('Lee', 100);					//直接调用函数
alert(box.run());

```


PS：稳妥构造函数和寄生类似














