##React Native进阶

###使用导航器跳转页面

####React Navigation
首先是在你的应用中安装此库：

	yarn add react-navigation

然后你就可以快速创建一个有两个页面（Main和Profile）的应用了：

	import {
	  StackNavigator,
	} from 'react-navigation';
	
	const App = StackNavigator({
	  Main: {screen: MainScreen},
	  Profile: {screen: ProfileScreen},
	});

其中每一个screen组件都可以单独设置导航选项，例如导航头的标题。还可以使用navigation属性中的方法去跳转到别的页面：

	class MainScreen extends React.Component {
	  static navigationOptions = {
	    title: 'Welcome',
	  };
	  render() {
	    const { navigate } = this.props.navigation;
	    return (
	      <Button
	        title="Go to Jane's profile"
	        onPress={() =>
	          navigate('Profile', { name: 'Jane' });
	        }
	      />
	    );
	  }
	}

###处理触摸事件

####可点击的组件

在需要捕捉用户点击操作时，可以使用"Touchable"开头的一系列组件。这些组件通过onPress属性接受一个点击事件的处理函数。当一个点击操作开始并且终止于本组件时（即在本组件上按下手指并且抬起手指时也没有移开到组件外），此函数会被调用。
	
	class MyButton extends Component {
	  _onPressButton() {
	    console.log("You tapped the button!");
	  }
	
	  render() {
	    return (
	      <TouchableHighlight onPress={this._onPressButton}>
	        <Text>Button</Text>
	      </TouchableHighlight>
	    );
	  }
	}

可点击的组件需要给用户提供视觉反馈，例如是哪个组件正在响应用户的操作，以及当用户抬起手指后会发生什么。用户也应该可以通过把手指移到一边来取消点击操作。

具体使用哪种组件，取决于你希望给用户什么样的视觉反馈：

1.一般来说，你可以使用TouchableHighlight来制作按钮或者链接。注意此组件的背景会在用户手指按下时变暗。

2.在Android上还可以使用TouchableNativeFeedback，它会在用户手指按下时形成类似墨水涟漪的视觉效果。

3.TouchableOpacity会在用户手指按下时降低按钮的透明度，而不会改变背景的颜色。

4.如果你想在处理点击事件的同时不显示任何视觉反馈，则需要使用TouchableWithoutFeedback。

###图片

####静态图片资源

从0.14版本开始，React Native提供了一个统一的方式来管理iOS和Android应用中的图片。要往App中添加一个静态图片，只需把图片文件放在代码文件夹中某处，然后像下面这样去引用它：

	Image source={require('./my-icon.png')} />	

####静态非图片资源

上面描述的require语法也可以用来静态地加载你项目中的声音、视频或者文档文件。大多数常见文件类型都支持，包括.mp3, .wav, .mp4, .mov, .htm 和 .pdf等（完整列表请看 packager defaults）。

需要注意的是视频必须指定尺寸而不能使用flex样式，因为我们目前还不能从非图片资源中获取到尺寸信息。对于直接链接到Xcode或者Android资源文件夹的视频，则不会有这个限制。

####使用混合App的图片资源

如果你在编写一个混合App（一部分UI使用React Native，而另一部分使用平台原生代码），也可以使用已经打包到App中的图片资源（以拖拽的方式放置在Xcode的asset类目中，或是放置在Android的drawable目录里）。注意此时只使用文件名，不带路径也不带后缀：

	<Image source={{uri: 'app_icon'}} style={{width: 40, height: 40}} />

对于放置在Android的assets目录中的图片，还可以使用asset:/ 前缀来引用：

	<Image source={{uri: 'asset:/app_icon.png'}} style={{width: 40, height: 40}} />
注意：这一做法并没有任何安全检查。你需要自己确保图片在应用中确实存在，而且还需要指定尺寸。

####网络图片

很多要在App中显示的图片并不能在编译的时候获得，又或者有时候需要动态载入来减少打包后的二进制文件的大小。这些时候，与静态资源不同的是，你需要手动指定图片的尺寸。同时我们强烈建议你使用https以满足iOS App Transport Security 的要求。
	
	// 正确
	<Image source={{uri: 'https://facebook.github.io/react/img/logo_og.png'}}
	       style={{width: 400, height: 400}} />
	
	// 错误
	<Image source={{uri: 'https://facebook.github.io/react/img/logo_og.png'}} />

####网络图片的请求参数

你可以在Image组件的source属性中指定一些请求参数，如下面的示例：

	<Image source={{
	  uri: 'https://facebook.github.io/react/img/logo_og.png',
	  method: 'POST',
	  headers: {
	    Pragma: 'no-cache'
	  },
	  body: 'Your Body goes here'
	}}
	style={{width: 400, height: 400}} />

###定时器

setTimeout, clearTimeout

setInterval, clearInterval

setImmediate, clearImmediate

requestAnimationFrame, cancelAnimationFrame

requestAnimationFrame(fn)和setTimeout(fn, 0)不同，前者会在每帧刷新之后执行一次，而后者则会尽可能快的执行（在iPhone5S上有可能每秒1000次以上）。

setImmediate则会在当前JavaScript执行块结束的时候执行，就在将要发送批量响应数据到原生之前。注意如果你在setImmediate的回调函数中又执行了setImmediate，它会紧接着立刻执行，而不会在调用之前等待原生代码。

Promise的实现就使用了setImmediate来执行异步调用。

####InteractionManager

原生应用感觉如此流畅的一个重要原因就是在互动和动画的过程中避免繁重的操作。在React Native里，我们目前受到限制，因为我们只有一个JavaScript执行线程。不过你可以用InteractionManager来确保在执行繁重工作之前所有的交互和动画都已经处理完毕。

应用可以通过以下代码来安排一个任务，使其在交互结束之后执行：

	InteractionManager.runAfterInteractions(() => {
	   // ...需要长时间同步执行的任务...
	});

我们来把它和之前的几个任务安排方法对比一下：

requestAnimationFrame(): 用来执行在一段时间内控制视图动画的代码

setImmediate/setTimeout/setInterval(): 在稍后执行代码。注意这有可能会延迟当前正在进行的动画。

runAfterInteractions(): 在稍后执行代码，不会延迟当前进行的动画。

触摸处理系统会把一个或多个进行中的触摸操作认定为'交互'，并且会将runAfterInteractions()的回调函数延迟执行，直到所有的触摸操作都结束或取消了。

InteractionManager还允许应用注册动画，在动画开始时创建一个交互“句柄”，然后在结束的时候清除它。
	
	var handle = InteractionManager.createInteractionHandle();
	// 执行动画... (`runAfterInteractions`中的任务现在开始排队等候)
	// 在动画完成之后
	InteractionManager.clearInteractionHandle(handle);
	// 在所有句柄都清除之后，现在开始依序执行队列中的任务

####务必在卸载组件前清除定时器！

我们发现很多React Native应用发生致命错误（闪退）是与计时器有关。具体来说，是在某个组件被卸载（unmount）之后，计时器却仍然在运行。要解决这个问题，只需铭记在unmount组件时清除（clearTimeout/clearInterval）所有用到的定时器即可：
	
	import React,{
	  Component
	} from 'react';
	
	export default class Hello extends Component {
	  componentDidMount() {
	    this.timer = setTimeout(
	      () => { console.log('把一个定时器的引用挂在this上'); },
	      500
	    );
	  }
	  componentWillUnmount() {
	    // 请注意Un"m"ount的m是小写
	
	    // 如果存在this.timer，则使用clearTimeout清空。
	    // 如果你使用多个timer，那么用多个变量，或者用个数组来保存引用，然后逐个clear
	    this.timer && clearTimeout(this.timer);
	  }
	};