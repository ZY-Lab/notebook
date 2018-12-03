### ES6基础语法知识  

为了更方便的学习es6,需要引用babel  
```js
<script src="https://cdn.bootcss.com/babel-standalone/6.22.1/babel.min.js"></script>
```

##### 1.解构数组  
```js
function breakfast() {
    return ['蛋糕','奶茶','苹果'];
}
let [des,drink,fruit] = breakfast();
console.log(des,drink,fruit);//返回的是 蛋糕 奶茶 苹果   
```

##### 2.解构对象  
```js
function breakfast1() {
    return {desser:'蛋糕',tea:'奶茶',fruit:'苹果'};
}
let {desser=desser,tea=tea,fruit=fruit} = breakfast1();
console.log(desser,tea,fruit);//返回的是 蛋糕 奶茶 苹果   
```

##### 3.模板字符串  
```js
let dessert = '包子',
    drink = '豆浆';

let breakfast = `今天的早餐是${dessert}和${drink}`;
console.log(breakfast);   
```

##### 4.带标签的模板字符串Tagged Templates
```js
    let dessert = '包子',
        drink = '豆浆';

    let breakfast = kitchen`今天的早餐是 \n
        ${dessert}和${drink}`;

    function kitchen(strings,...values) {
        console.log(strings);
        console.log(values);

        let result = "";
        for (var i = 0; i<values.length; i++){
            result += strings[i];
            result += values[i];
        }
        result += strings[strings.length -1];
        return result;
    }
    console.log(breakfast)
```


##### 5.判断字符串是否包含其他字符串
```js
    let dessert = '包子',
        drink = '豆浆';
    let breakfast = `今天的早餐是 \n
            ${dessert}和${drink}!`;

    console.log( breakfast.startsWith("今天") );  //是否以什么开头
    console.log( breakfast.endsWith("!") );       //是否以什么结束
    console.log( breakfast.includes("早餐") );    //是否包含什么
```


##### 6.默认参数 - Default Parameter Values
```js
    function breakfast(dessert = 'cake',drink = 'tea') {
        return `${dessert}和${drink}`
    }
    console.log(breakfast())//返回的是  cake和tea
    console.log(breakfast('bread','milk')) //返回的是bread和milk
```


##### 7.展开操作符-Spread  ...点点点
```js
    let fruits = ['apple','banana'],
        foods = ['cake',...fruits];
    console.log(fruits)     //返回["apple", "banana"]
    console.log(...fruits)  //返回apple banana
    console.log(foods)      //返回["cake", "apple", "banana"]
    console.log(...foods)   //返回cake apple banana
```

##### 8.剩余符号操作符Rest ...
```js
    function breakfast(dessert,drink,...foods) {
        console.log(dessert,drink,foods);
    }
    breakfast('cake','tea','apple','banana') //返回的是 cake tea ["apple", "banana"]

    function breakfast2(dessert,drink,...foods) {
        console.log(dessert,drink,...foods);
    }
    breakfast2('cake','tea','apple','banana') //返回的是 cake tea apple banana
```

##### 9.解构参数 - Destructured Parameters
```js
    function breakfast(dessert,drink,{location,restaurant} = {}) {
        console.log(dessert,drink,location,restaurant);
    }
    breakfast('cake','milk',{location:'青岛',restaurant:'罗先生'})
```


##### 10.函数的名字-name属性
```js
    let breakfast1 = function () {}
    console.log(breakfast1.name) //返回的是breakfast1
    let breakfast2 = function superMilk() { }
    console.log(breakfast2.name) //返回的是superMilk
```

##### 11.箭头函数-Arrow Fuctions
```js
    const breakfast1 = dessert => dessert;
//    翻译成es5:
//    function breakfast1(dessert) {
//        return dessert;
//    }

    let breakfast2 = (dessert,drink) => {
        return dessert + drink
    };
//    翻译成es5:
//    function breakfast2(dessert, drink) {
//        return dessert + drink;
//    }
```

##### 12.对象表达式
```js
    let dessert = 'cake',drink = 'tea';
    let food = {
        dessert,
        drink,
        breakfast(){}
    }
    console.log(food)
```

##### 13.对象属性名,向里面添加数据用 .  和['']
```js
    let food ={};

    food.dessert = 'cake';
    food['hot drink']= 'tea';
    console.log(food)
```


##### 14.对比两个值是否相等-Object.is()
```js
    Object.is(+0,-0); //判断正零和负零是否相等
```


##### 15.把对象的值复制到另一个对象里 - Object.assign()
```js
    let breakfast = {};
    let food = {drink:'tea',dessert:'cake'};
    Object.assign(
        breakfast,
        food
    );
    console.log(breakfast) //返回{drink:'tea',dessert:'cake'}
```


##### 16.设置对象的 prototype - Object.setPrototypeOf()  可以创建对象后再改变对象
```js
    let breakfast = {
        getDrink(){
            return 'tea';
        }
    };
    let dinner = {
        getDrink(){
            return 'milk'
        }
    };
    let sunday = Object.create(breakfast);
    console.log(sunday.getDrink());  //返回 tea
    console.log(Object.getPrototypeOf(sunday) === breakfast); //返回 true
```


##### 17.__proto__  前后两个下划线
```js
    let breakfast = {
        getDrink(){
            return 'tea';
        }
    };
    let dinner = {
        getDrink(){
            return 'milk'
        }
    };

    let sunday  = {
        __proto__: breakfast
    }
    console.log(sunday.getDrink()); //返回tea

    sunday.__proto__ = dinner;
    console.log(sunday.getDrink()); //返回milk
```

##### 18.super
```js
    let breakfast = {
        getDrink(){
            return 'tea';
        }
    };
    let dinner = {
        getDrink(){
            return 'milk';
        }
    };

    let sunday  = {
        __proto__: breakfast,
        getDrink(){
            return super.getDrink() + 'water'
        }
    };
    console.log(sunday.getDrink())
```


##### 19.迭代器 - Iterators 轮流交换的意思
```js
    function chef(foods) {
        let i = 0;
        return {
            next(){
                let done = (i< foods.length);
                console.log(i)
                let value = done ? foods[i++] : undefined;

                return{
                    value: value,
                    done: done
                }
            }
        }
    }

    let thunder = chef(['apple','ege']);
    console.log(thunder.next()) //返回{value: "apple", done: true}
    console.log(thunder.next()) //返回{value: "ege", done: true}
    console.log(thunder.next()) //返回{value: undefined, done: false}
```


##### 20.生成器 - Generators
```js
    function* chef() {
        yield 'apple';
        yield 'ega';
    }
    let thunder = chef();
    console.log(thunder.next());
    console.log(thunder.next());
```


##### 21.Class - 类
```js
    class Chef {
        constructor(food){
            this.food = food;
        }

        cook(){
            console.log(this)
            console.log(this.food); //返回的是 apple
        }
    }
    let thunder = new Chef('apple');
    thunder.cook()
```


##### 22.get 得到 与 set 集
```js
    class Chef {
        constructor(food){
            this.food = food;
            this.dish = [];
        }
        get menu(){
            return this.dish;
        }
        set menu(dish){
            this.dish.push(dish);
        }
        cook(){
            console.log(this.food);
        }
    }

    let thunder = new Chef();
    console.log(thunder.menu = "apple") //返回apple
    console.log(thunder.menu = "tea")   //返回tea
    console.log(thunder.menu)           //返回["apple", "tea"]
```



##### 23.静态方法-staitc
```js
    class Chef {
        constructor(food){
            this.food = food;
            this.dish = [];
        }

        get menu(){
            return this.dish;
        }

        set menu(dish){
            this.dish.push(dish);
        }
        static cook(food){
            console.log(food); //返回的是  banana
        }
    }

    Chef.cook('banana');
```


##### 24.继承-extends
```js
    class Person{
        constructor(name,birthday) {
            this.name = name;
            this.birthday = birthday;
        }
        intro(){
            return `${this.name},出生日期在：${this.birthday}`
        }
    }

    class Chef extends  Person {
        constructor(name,birthday){
            super(name,birthday);
        }
    }
    let thunder = new Chef('thunder','1996-03-19');
    console.log(thunder.intro());
```


##### 25.set  一堆东西的集合
null   

##### 26.Map
null   

##### 27.Module 模块
null   