#### 继承
继承是面向对象中一个比较核心的概念。其他正统面向对象语言都会用两种方式实现继承：一个是接口实现，一个是继承。而ECMAScript只支持继承，不支持接口实现，而实现继承的方式依靠原型链完成。
```
//继承，通过原型链实现

function Box() {							//Box构造
	this.name = 'Lee';
}

function Desk() {							//Desk构造
	this.age = 100;
}

Desk.prototype = new Box();					//Desc继承了Box，通过原型，形成链条

var desk = new Desk();
alert(desk.age);
alert(desk.name);							//得到被继承的属性

function Table() {							//Table构造
this.level = 'AAAAA';
}							

Table.prototype = new Desk();				//继续原型链继承

var table = new Table();
alert(table.name);							//继承了Box和Desk

```
在JavaScript里，被继承的函数称为超类型(父类，基类也行，其他语言叫法)，继承的函数称为子类型(子类，派生类)。继承也有之前问题，比如字面量重写原型会中断关系，使用引用类型的原型，并且子类型还无法给超类型传递参数。
为了解决引用共享和超类型无法传参的问题，我们采用一种叫借用构造函数的技术，或者成为对象冒充(伪造对象、经典继承)的技术来解决这两种问题。
```
function Box(age) {
	this.name = ['Lee', 'Jack', 'Hello']
	this.age = age;
}

function Desk(age) {
	Box.call(this, age);						//对象冒充，对象冒充只能继承构造里的信息
}
var desk = new Desk(200);
alert(desk.age);
alert(desk.name);
desk.name.push('AAA');						//添加的新数据，只给desk
alert(desk.name);
```

借用构造函数虽然解决了刚才两种问题，但没有原型，复用则无从谈起。所以，我们需要原型链+借用构造函数的模式，这种模式成为**组合继承**。

```
function Box(age) {
	this.name = ['Lee', 'Jack', 'Hello']
	this.age = age;
}
//构造函数里的方法，放在构造里，每次实例化，都会分配一个内存地址，浪费，所以最好放在原型里，保证多次实例化只有一个地址

Box.prototype.run = function () {				
	return this.name + this.age;
};

function Desk(age) {
	Box.call(this, age);						//对象冒充
}

Desk.prototype = new Box();					//原型链继承

var desk = new Desk(100);
alert(desk.run());
```
还有一种继承模式叫做：**原型式继承**；这种继承借助原型并基于已有的对象创建新对象，同时还不必因此创建自定义类型。

```
//1.原型链继承，2.借用构造函数继承(对象冒充继承) 3.组合继承(结合前两种)

//4.原型式继承

//临时中转函数
function obj(o) {				 //o表示将要传递进入的一个对象
	function F() {}				//F构造是一个临时新建的对象，用来存储传递过来的对象
	F.prototype = o;			//将o对象实例赋值给F构造的原型对象
	return new F();			    //最后返回这个得到传递过来对象的对象实例
}

//F.prototype = o 其实就相当于 Desk.prototype = new Box();


//这是字面量的声明方式，相当于var box = new Box();
var box = {
	name : 'Lee',
	age : 100,
	family : ['哥哥','姐姐','妹妹']
};


//box1就等于new F()
var box1 = obj(box);
//alert(box1.name);
alert(box1.family);
box1.family.push('弟弟');
alert(box1.family);

var box2 = obj(box);
alert(box2.family);					//引用类型的属性共享了
```

寄生式继承把原型式+工厂模式结合而来，目的是为了封装创建对象的过程。
```
//5.寄生式继承 = 原型式 +工厂模式

//临时中转函数
function obj(o) {				
	function F() {}				
	F.prototype = o;			
	return new F();			
}

//寄生函数
function create(o) {
	var f = obj(o);
	f.run = function () {
		return this.name + '方法';
	}
	return f;
}

var box = {
	name : 'Lee',
	age : 100,
	family : ['哥哥','姐姐','妹妹']
};


var box1 = create(box);
alert(box1.run());
```

组合式继承是JavaScript最常用的继承模式；但，组合式继承也有一点小问题，就是超类型在使用过程中会被调用两次：一次是创建子类型的时候，另一次是在子类型构造函数的内部。
```
function Box(name) {
	this.name = name;
	this.arr = ['哥哥','妹妹','父母'];
}

Box.prototype.run = function () {
	return this.name;
};

function Desk(name, age) {
	Box.call(this, name);					//第二次调用Box
	this.age = age;
}

Desk.prototype = new Box();					//第一次调用Box
```
以上代码是之前的组合继承，那么**寄生组合继承**，解决了两次调用的问题。
```
//6.寄生组合继承

//临时中转函数
function obj(o) {				
	function F() {}				
	F.prototype = o;			
	return new F();			
}


//寄生函数
function create(box, desk) {
	var f = obj(box.prototype);
	f.constructor = desk;				//调整原型构造指针
	desk.prototype = f;
}

function Box(name, age) {
	this.name = name;
	this.age = age;
}

Box.prototype.run = function () {
	return this.name + this.age + '运行中...'
}

function Desk(name, age) {
	Box.call(this, name, age);				//对象冒充
}

//通过寄生组合继承来实现继承
create(Box, Desk);							//这句话用来替代Desk.prototype = new Box();


var desk = new Desk('Lee', 100);
alert(desk.run());
alert(desk.constructor);
```
























