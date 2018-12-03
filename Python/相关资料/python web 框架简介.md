###1、Flask ###
http://flask.pocoo.org/
**开发简单的网站，适合初学者。**
Flask 框架学会以后，学习各种插件的使用，例如：使用 WTForm + Flask-WTForm 来验证表单数据，用 SQLAlchemy + Flask-SQLAlchemy 来对你的数据库进行控制。
Ps:果壳网基于 Flask 开发的。
###2、Tornado ###
**传说中性能高高的框架**
支持异步处理的功能，适合做长连接，它不仅是Web框架，还是一个Web Server，同时提供了异步库。这是它的特点，其他框架不支持。
Tornado 的设计似乎更注重 RESTful URL。但 Tornado 提供了网站基本需要使用的模块外，剩下的则需要开发者自己进行扩展。例如数据库操作，虽然内置了一个 database 的模块（后来独立出去了，现在叫做 torndb）但是不支持 ORM，快速开发起来还是挺吃力的。如果需要 ORM 支持的话，还需要自己写一层将 SQLAlchemy 和 Tornado 联系起来。
###3、Bottle ###
**Bottle 和 Flask 都属于轻量级的 Web 框架**
###4、web.py ###
###5、web2py ###
这个框架是 Google 在 web.py 基础上二次开发而来的，兼容 GAE 。性能据说很高。缺点同样是对扩展支持不太好，需要自己进行扩展。
###6、Quixote ###
Quixote 的路由会有些特别。另外 Quixote 的性能据说也好。
###7、Pyramid ###
**Pyramid更适合做一个想「长久」的应用。**Pyramid由于自带多一些的功能（比如HTTP缓存），以及扩展的设计等原因，会让你做的改变尽量的少甚至于直接加代码即可。Pyramid把模板的使用插件化，切换模板引擎非常方便。

###8、Pylons ###
Pylons和Django的设计理念完全不同，Pylons本身只有两千行左右的Python代码，不过它还附带有一些几乎就是Pylons御用 的第三方模块。Pylons只提供一个架子和可选方案，你可以根据自己的喜好自由的选择Template、ORM、form、auth等组件，系统高度可 定制。
Pylons依赖于许多第三方库，它们并不是Pylons造，学Pylons的同时还得学这些库怎么使用，关键有些时候你都不知道你 要学什么。Pylons的学习曲线相对比Django要高的多。Pylons一度被誉为只适合高手使用的Python框架。
调试噩梦，因为牵涉到的模块多，一旦有错误发生就比较难定位问题处在哪里。可能是你写的程序的错、也可能是Pylons出错了、再或是SQLAlchemy出错了、搞不好是formencode有bug，反正很凌乱了。这个只有用的很熟了才能解决这个问题。
升级噩梦，安装Pylons大大小小共要安装近20个Python模块，各有各自的版本号，要升级Pylons的版本，哪个模块出了不兼容的问题都有可能，升级基本上很难很难。至今reddit的Pylons还停留在古董的0.9.6上，SQLAlchemy也还是0.5.3的版本，应该跟这条有关系。
Pylons和repoze.bfg的融合可能会催生下一个能挑战Django地位的框架。


##其他框架 ###
Diesel基于Greenlet的事件I/O框架
Diesel提供一个整洁的API来编写网络客户端和服务器。支持TCP和UDP。
