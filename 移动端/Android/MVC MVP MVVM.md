## MVC，MVP和MVVM差异

#### MVC

![](https://i.imgur.com/Ts6y4vd.png)

视图层（View）：一般采用XML文件进行界面的描述，使用的时候可以非常方便的引入，当然，也可以使用JavaScript+HTML等的方式作为View层，他的职责就是负责显示从Controller上获取到的数据（但是xml布局作为View来说功能很无力，所以通常Activity也会承担一部分View的工作）。

控制层（Controller）：Android的控制层的重任通常落在了众多的Activity的肩上，他们从模型层获取数据，将获取到的数据绑定到view上，并且还需要监听用户的输入等操作。

模型层（Model）：对数据库的操作、对网络等的操作都应该在Model里面处理，当然对业务计算，变更等操作也是必须放在的该层的。

#### MVP

![](https://i.imgur.com/aquKT05.png)

Presenter与Model，Presenter与View的通信都是双向的，View不与Model发生关系，都是通过Presenter来传递，所以Presenter的业务量会显的非常大，三层之间的交互关系为：

1.View接受用户的交互请求

2.View将请求转交给Presenter

3.Presenter操作Model进行数据库更新

4.数据更新之后，Model通知Presenter数据发生变化

5.Presenter更新View层的显示

Model层

该层通常是用来处理业务逻辑和实体模型。

View层

通常是一个Activity或者Fragment或者View，这取决于应用的结构，它会持有一个Presenter层的引用，所以View唯一做的事情就是在有用户交互等操作时调用Presenter层的方法。

Presenter层

该层用来作为一个中间层的角色，它接受Model层的数据，并且处理之后传递给View层，还需要处理View层的用户交互等操作。

View和Presenter的一对一关系意味着一个View只能映射到一个Presenter上，并且View只有Presenter的引用，没有Model的引用，所以Presenter和View是一个双向的交互。Presenter不管View层的UI布局，View的UI布局变更，Presenter层不需要做任何修改。

###MVVM

![](https://i.imgur.com/jzRCMQG.png)

　Model，View and ViewModel模式，MVVM 模式将 Presenter 改名为 ViewModel，基本上与 MVP 模式完全一致，ViewModel可以理解成是View的数据模型和Presenter的合体，MVVM采用双向绑定（data-binding）：View的变动，自动反映在 ViewModel，反之亦然，这种模式实际上是框架替应用开发者做了一些工作，开发者只需要较少的代码就能实现比较复杂的交互。 

Model

类似MVP

View

类似MVP

ViewModel

注意这里的“Model”指的是View的Model，跟上面那个Model不是一回事。所谓View的Model就是包含View的一些数据属性和操作的东西。


关键点总结：

MVC

Controller是基于行为，并且能够在view之间共享

Controller负责接收用户交互等操作，并且决定需要显示的视图。

MVP

View和Model更加的解耦了，Presenter负责绑定Model到View。

复杂的View可以对应多个Persenter。

Presenter保留有View层的事件逻辑，所有的点击之类的事件都直接委托给Presenter。

Presenter通过接口直接和View层解耦，所以更加方便的进行View的单元测试。

Presenter和其他两层都是双向调用的。

MVP有两种实现方式：”Passive View”，View基本包含0逻辑， Presenter作为View和Model的中间人，View和Model相互隔离，View和Model没有直接的数据绑定，取而代之的是View提供相关的setter方法供Persenter去调用，这么做的好处是View和Model干净的分离开了，所以更好的进行相关测试，缺点是需要提供很多的setter方法；”Supervising Controller”，Persenter处理用户交互等的操作，View和Model直接通过数据绑定连接，这种模式下，Persenter的任务就是将实体直接通过Model层传递给View层，这种方法的好处就是代码量少了，但是缺点就是测试难度增大，并且View的封装性变低。

MVVM

用户直接交互的是View。

View和ViewModel是多对一的关系。

View有ViewModel的引用，但是ViewModel没有任何关于View的信息。

支持View和ViewModel的双向数据绑定。





