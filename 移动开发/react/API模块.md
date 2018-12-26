##API模块

###ToastAndroid
方法：

show(message:string,duration:number)  static 静态方法，该设置toast消息的弹出

属性：

1.SHORT  静态int值，表示toast显示较短的时间

2.LONG   静态int值，表示otast显示较长的时间

###Alert弹出框

在Android平台上面最多只能指定三个按钮。Android平台的弹出框的按钮有'中间态','取消','确认'三种状态

1.如果你只有指定了一个按钮，那么该为'positive' (例如:确定)

2.如果你指定了两个按钮，那么该会'negative','positive' (例如:确定，取消)

3.如果你指定了三个按钮，那么该会'neutral','negative','positive'(例如:稍后再说,'确定','取消')

方法：

static alert(title:string,message?:string,buttons?:Buttons,type?:AlertType)  该会Alert模块显示弹框的静态方法，有四个参数，分别为标题，信息，按钮，以及按钮的风格类型

###Dimensions屏幕宽高

方法：

1.set(dims:{[key:string]:any})  static 静态方法，该方法应该只能被原生代码进行调用。@parm{object} dims参数作为屏幕宽高设置

2.get(dim:string)   static静态方法,进行初始化屏幕的宽和高信息 在runApplication方法之后就执行了，所以我们可以在任何requires的方法运行之前就可以获取到该信息。不过该信息可能会发生改变。具体我们往下看:

[注].屏幕尺寸信息一般可以直接进行使用的，但是有时候会发生变化(例如:屏幕的方向发生旋转)。因此如果基于该屏幕信息的业务逻辑或者相关样式设置需要在调用每次render渲染方法之后进行，而不是我们把该屏幕信息保存下来，后面直接使用。(例如:我在使用样式设置的时候，不要去使用StyleSheet方法，而是采用内联式方案)。即:什么时候需要使用屏幕信息，那就什么时候去调用该方法

实例代码:var {height,width}=Dimensions.get('window')

@param {string}  进行调用set方法，想要返回屏幕信息的名称

@return {Object?}  返回的屏幕尺寸信息

具体事例：

  		<Text style={styles.instructions}>
           当前屏幕宽度:+{Dimensions.get('window').width};
        </Text>
        <Text style={styles.instructions}>
           当前屏幕高度:'+{Dimensions.get('window').height};
        </Text>

###AppRegistry应用注册入口

当前AppRegistry模式是React Native中最基本的模块，也是最常用的模块。AppRegistry模块是React Native应用JavaScript运行的入口。应用的跟组件应用使用AppRegistry.registerComponent进行注册自己。然后原生系统就可以进行加载运行bundle文件包，最后就会可以调用AppRegistry.runApplication进行运行起来应用。

当一个视图被摧毁的时候，为了结束应用可以调用AppRegistry.unmountApplictionComponentAtRootTag方法。

属性方法：

2.1.registerConfig(config:Array<AppConfig>)  static 静态方法, 进行注册配置信息

2.2.registerComponent(appKey:string,getComponentFunc:ComponentProvider)  static静态方法，进行注册组件

2.3.registerRunnable(appKey:string,func:Function)  static静态方法 ，进行注册线程

2.4.registerAppKeys()  static静态方法，进行获取所有组件的keys值

2.5.runApplication(appKey:string,appParameters:any)  static静态方法, 进行运行应用

2.5.unmountApplicationComponentAtRootTag()  static静态方法，结束应用

###NetInfo(网络信息)使用

通过该NetInfo模块我们可以检测手机客户端设备联网/断网状态。

在Android平台上面为了获取网络状态，我们需要在android项目的AndroidManifest.xml文件中配置以下的权限:

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

Android平台的网络连接类型状态如下:

1.NONE   设备没有网络连接

2.BLUETOOTH  蓝牙数据连接

3.DUMMY   虚拟数据连接

4.ETHERNET  以太网数据连接

5.MOBILE  手机移动网络数据连接

6.MOBILE_DUN  拨号移动网络数据连接

7.MOBILE_HIPRI  高权限的移动网络数据连接

8.MOBILE_MMS   彩信移动网络数据连接

9.MOBILE_SUPL   SUP网络数据连接

10.VPN   虚拟网络连接 ，最低支持Android API 21版本

11.WIFI   无线网络连接

12.WIMAX   wimax网络连接

13.UNKNOWN  未知网络数据连接

isConnectionExpensive(判断连接的网络是否计费)

isConnected通过异步方法来获取当前与没有网络连接，具体检测代码实例如下:
	
	NetInfo.isConnected.fetch().done((isConnected) => {
	 
	  console.log('First, is ' + (isConnected ? 'online' : 'offline'));
	 
	});
	 
	function handleFirstConnectivityChange(isConnected) {
	 
	  console.log('Then, is ' + (isConnected ? 'online' : 'offline'));
	 
	  NetInfo.isConnected.removeEventListener(
	 
	    'change',
	 
	    handleFirstConnectivityChange
	 
	  );
	 
	}
	 
	NetInfo.isConnected.addEventListener(
	 
	  'change',
	 
	  handleFirstConnectivityChange
	 
	);


属性与方法

1.addEventListener(eventName:ChangeEventName,handler:Function)   静态方法，用设置网络变化事件监听器，同时需要传入回调的处理方法

2.removeEventListener(eventName:ChangeEventName,handler:Function)  静态方法, 用于移除网络事件变化监听器

3.fetch()   静态方法  检测当前网络连接状态

4.isConnectionExpensve(callback:(metered:?boolean,error?:string)=>void)   静态方法，检测当前连接的网络是否需要计费

5.isConnected :ObjectExpression 当前网络是否连接的属性

使用NetInfo模块之前千万不要忘记Android项目中的权限配置如下:

<uses-permission android:name="android.permission.INTERNET" />

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />