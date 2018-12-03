## Swift关键字inout - 让值类型以引用方式传递
两种参数传递方式
* 值类型：
传递的是参数的一个副本，这样在调用参数的过程中不会影响原始数据。

* 引用类型：
把参数本身引用(内存地址)传递过去，在调用的过程会影响原始数据。

在Swift众多数据类型中，只有class是引用类型。
其余的如Int,Float,Bool,Character,Array,Set,enum,struct全都是值类型。

让值类型以引用方式传递
有时候我们需要通过一个函数改变函数外面变量的值(将一个值类型参数以引用方式传递)，
这时，Swift提供的inout关键字就可以实现。

举例:

     /// 以下代码已更新到 Swift 4.0
    var value = 50
    print(value)  // 此时value值为50
    
    func increment(_ value: inout Int, _ length: Int = 10) {
        value += length
    }
    
    increment(&value)
    print(value)  // 此时value值为60，成功改变了函数外部变量value的值


即：声明函数时，在参数类型前面用inout修饰，函数内部实现改变外部参数
传入参数时(调用函数时)，在变量名字前面用&符号修饰表示，表明这个变量在参数内部是可以被改变的（可将改变传递到原始数据）

注意
inout修饰的参数是不能有默认值的(例子中length = 10被赋予默认值)，有范围的参数集合也不能被修饰；
一个参数一旦被inout修饰，就不能再被var和let修饰了。

例：交换两个变量值
    func swap(a: inout Int , b:inout Int){
    let temp = a
    a = b
    b = temp
   }
   var x = 20 , y = 30
   swap(a:&x , b:&y)
   print(x , y)