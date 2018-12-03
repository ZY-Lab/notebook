#React学习

###React JSX

React 使用 JSX 来替代常规的 JavaScript。

JSX 是一个看起来很像 XML 的 JavaScript 语法扩展。

可以在js里面写标签。

可以在 JSX 中使用 JavaScript 表达式。表达式写在花括号 {} 中。实例如下：

	ReactDOM.render(
	    <div>
	      <h1>{1+1}</h1>
	    </div>
	    ,
	    document.getElementById('example')
	);

在 JSX 中不能使用 if else 语句，但可以使用 conditional (三元运算) 表达式来替代。以下实例中如果变量 i 等于 1 浏览器将输出 true, 如果修改 i 的值，则会输出 false.
	
	ReactDOM.render(
	    <div>
	      <h1>{i == 1 ? 'True!' : 'False'}</h1>
	    </div>
	    ,
	    document.getElementById('example')
	);

在react中 标签用className 代替class。

###React 组件

可以将一个页面分成很多的小组件 然后通过这些小组件来合成大的组件。

React.createClass 方法用于生成一个组件类HelloMessage。

<HelloMessage /> 实例组件类并输出信息。

	var HelloMessage = React.createClass({
	  render: function() {
	    return <h1>Hello World！</h1>;
	  }
	});
	 
	ReactDOM.render(
	  <HelloMessage />,
	  document.getElementById('example')
	);

###React State和Props

通过 props 和 state 来传递数据。

通过 getInitialState为state设置一个默认值。 然后通过this.state.xxx来获取数据， 通过setState()来改变state数据。


通过 getDefaultProps为props设置一个默认值。 然后通过this.props.xxx来获取数据。

####什么时候用props,什么时候用state

我们已经知道可以通过props和state两种方式向组件传递数据，props是只读的不能被改变，而 state 是用来反映一个组件的状态，是可以改变的。因此，当组件所需要的数据在调用时是已经确定的，不频繁发生变化的，就可以使用props来传递，相反，当组件所需要的数据在调用时不能确定，需要等待异步回调时才能确定，比如ajax请求数据，input的onchange事件，这时就需要使用state来记录和改变这些值得变化。

###React 组件生命周期

componentWillMount 在渲染前调用,在客户端也在服务端。

componentDidMount 在第一次渲染后调用，只在客户端。之后组件已经生成了对应的DOM结构，可以通过this.getDOMNode()来进行访问。

componentWillReceiveProps 在组件接收到一个新的prop时被调用。这个方法在初始化render时不会被调用。

shouldComponentUpdate 返回一个布尔值。在组件接收到新的props或者state时被调用。在初始化时或者使用forceUpdate时不被调用。  

componentWillUpdate 在组件接收到新的props或者state但还没有render时被调用。在初始化时不会被调用。

componentDidUpdate 在组件完成更新后立即调用。在初始化时不会被调用。

componentWillUnmount 在组件从 DOM 中移除的时候立刻被调用。

###React事件

设置输入框 input 通过调用OonChange事件来监听input的变化 然后去修改state。

 onChange={this.handleChange}

 handleChange: function(event) {
   this.setState({value: event.target.value});
 },

通过 event.target.value 来获取输入框的值。

Button点击事件  onClick 事件来修改数据

onClick={this.handleChange}

handleChange: function(event) {
   this.setState({value: '菜鸟教程'})
},

当你需要从子组件中更新父组件的 state 时，你需要在父组件通过创建事件句柄 (handleChange) ，并作为 prop (updateStateProp) 传递到你的子组件上

父组件 

updateStateProp = {this.handleChange}
handleChange: function(event) {
  this.setState({value: '菜鸟教程'})
},

子组件 

onClick = {this.props.updateStateProp}

具体事例 

	var Content = React.createClass({
	  render: function() {
	    return  <div>
	              <button onClick = {this.props.updateStateProp}>点我</button>
	              <h4>{this.props.myDataProp}</h4>
	           </div>
	  }
	});
	var HelloMessage = React.createClass({
	  getInitialState: function() {
	    return {value: 'Hello Runoob!'};
	  },
	  handleChange: function(event) {
	    this.setState({value: '菜鸟教程'})
	  },
	  render: function() {
	    var value = this.state.value;
	    return <div>
	            <Content myDataProp = {value} 
	              updateStateProp = {this.handleChange}></Content>
	           </div>;
	  }
	});
	ReactDOM.render(
	  <HelloMessage />,
	  document.getElementById('example')
	);

###React Refs

eact 支持一种非常特殊的属性 Ref ，你可以用来绑定到 render() 输出的任何组件上。

绑定一个 ref 属性到 render 的返回值上：

	<input ref="myInput" />

var input = this.refs.myInput;通过this.refs获取支撑实例。


###ES6写法
####引入模块
	
	import '模块文件地址'
	
	import 组件 from '模块文件地址'

####导出模块

用export default实现

####定义组件的属性类型和默认属性

	  static defaultProps = {
	        autoPlay: false,
	        maxLoops: 10,
	    };  // 注意这里有分号
	    static propTypes = {
	        autoPlay: React.PropTypes.bool.isRequired,
	        maxLoops: React.PropTypes.number.isRequired,
	        posterFrameSrc: React.PropTypes.string.isRequired,
	        videoSrc: React.PropTypes.string.isRequired,
	    };  // 注意这里有分号

####初始化STATE

	constructor(props){
	        super(props);
	        this.state = {
	            loopsRemaining: this.props.maxLoops,
	        };
	    }


###调用方法

需要通过bind来绑定this引用，或者使用箭头函数（它会绑定当前scope的this引用）来调用：

	  handleOptionsButtonClick(e){
	        this.setState({showOptionsModal: true});
	    }
在初始化中
this.handleOptionsButtonClick = this.handleOptionsButtonClick.bind(this);

