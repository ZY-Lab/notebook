###根据极爱秀手机端通过RN实现页面效果

>首页效果展示

![输入图片说明](https://git.oschina.net/uploads/images/2017/0720/153348_b9225292_684224.png "img_main.png")

####一、创建项目，实现顶部搜索栏

  **页面分析**
左侧搜索框+右侧消息

![输入图片说明](https://git.oschina.net/uploads/images/2017/0720/143251_ee71e6c7_684224.png "img_message.png")


 **1、创建Header.js**  

 **2、添加搜索栏，设置样式** 

```JavaScript
  <View style={styles.container}>
 </View>
```

```JavaScript
 container: {
        flexDirection: 'row',   // 水平排布
        paddingLeft: 10,
        paddingRight: 10,
        paddingTop: Platform.OS === 'ios' ? 20 : 0,  // 处理iOS状态栏
        height: Platform.OS === 'ios' ? 68 : 48,   // 处理iOS状态栏
        backgroundColor: '#262626',
        alignItems: 'center'  // 使元素垂直居中排布, 当flexDirection为column时, 为水平居中
    }
```
 **3、左侧搜索框** 

```JavaScript
<View style={styles.searchBox}>

                    <Image source={require('./images/header/icon_search.png')} style={styles.searchIcon}/>
                    <TextInput
                        keyboardType='web-search'
                        placeholder='请输入关键词'
                        underlineColorAndroid={'transparent'}
                        style={styles.inputText}/>
                    {/*<Image source={require('./images/header/icon_voice.png')} style={styles.voiceIcon}/>*/}
                </View>
```

```JavaScript
 searchBox: {
        height: 30,
        flexDirection: 'row',
        flex: 1,  // 类似于android中的layout_weight,设置为1即自动拉伸填充
        borderRadius: 5,  // 设置圆角边
        backgroundColor: 'white',
        alignItems: 'center',
        marginLeft: 8,
        marginRight: 12
    }
```

 **4、右侧消息框**

```JavaScript
  <View style={styles.message}>
                    <Image source={require('./images/header/ic_action_message.png')} style={styles.scanIcon}/>
                    <Text style={{color:'#ffffff',fontSize:12}}>消息</Text>
                </View>
```
```JavaScript
scanIcon: {
        height: 23.7,
        width: 23.7,
        resizeMode: 'stretch'
    },
  message: {
        flexDirection: 'column',

    }
```
 **5、添加到页面**
创建HomePage.js,页面，将Header.js添加到HomePage中



```JavaScript
import Header from '../Header';

  render() {
        return (
            <View style={{flex: 1}}>
        <Header />
            
            </View >
        )
    }
```

####二、添加banner滚动栏
 **通过ViewPager实现滚动效果** 

```JavaScript
const BANNER_IMGS = [
    require('../images/banner/img_banner1.jpg'),
    require('../images/banner/img_banner2.jpg')，
    require('../images/banner/img_banner3.jpg')
];


  <ViewPager
                            style={{height:160}}
                            dataSource={this.state.dataSource}
                            renderPage={this._renderPage}
                            isLoop={true}
                            autoPlay={true}
                        />
```

**构造函数中初始化**

viewpager必须在构造函数中进行初始化

```JavaScript
  constructor(props) {
        super(props);
        // 用于构建DataSource对象
        var dataSource = new ViewPager.DataSource({
            pageHasChanged: (p1, p2) => p1 !== p2,
        });
        // 实际的DataSources存放在state中
        this.state = {
            dataSource: dataSource.cloneWithPages(BANNER_IMGS)
        }
    }
```

```JavaScript
  _renderPage(data, pageID) {
        return (
            <Image
                source={data}
                style={styles.page}/>
        );
    }
```


>ViewPager的相关属性
- dataSource: 设置数据源,
- renderPage: 渲染页面
- autoPlay: 是否自动播放
- initialPage: 设置第一页的索引加载
- isLoop: 是否无线滚动
- locked: 是否触摸滚动
- onChangePage: 回调
- renderPageIndicator: 自定义指示器样式的渲染

####三、添加四个按钮

![输入图片说明](https://git.oschina.net/uploads/images/2017/0720/161553_434a6c2c_684224.png "img_button.png")

 **1、封装一个Button的View,MenuButton.js** 

View主要包括图片和文字，垂直居中排列，并给添加点击事件

>通过TouchableWithoutFeedback 实现点击事件，该组件只支持一个子节点

```JavaScript
 <TouchableWithoutFeedback onPress={this._onClick}>
                <View style={{alignItems:'center',flex:1}}>
                    <Image style={styles.iconImg} source={this.props.renderIcon}/>
                    <Text style={styles.showText}>{this.props.showText}</Text>
                </View>
            </TouchableWithoutFeedback>
```

```JavaScript
 constructor(props) {
        super(props);
        this._onClick = this._onClick.bind(this);  // 需要在回调函数中使用this,必须使用bind(this)来绑定
    }

    _onClick() {
        if (this.props.onClick) {   // 在设置了回调函数的情况下
            this.props.onClick(this.props.showText, this.props.tag);  // 回调Title和Tag
        }
    }
```

设置样式

```JavaScript
 iconImg: {
        width: 60,
        height: 60,
        marginBottom: 2
    },
    showText: {
        fontSize: 16
    }
```

 **2、在HomePage.js中添加MenuButton** 
```
<MenuButton renderIcon={require('../images/home_icons/ic_1.png')}
                                        showText={'分类'} tag={'fl'}
                                        onClick={this._onMenuClick}/>
 <MenuButton renderIcon={require('../images/home_icons/ic_2.png')}
                                        showText={'购物车'} tag={'gwc'}
                                        onClick={this._onMenuClick}/>
                            <MenuButton renderIcon={require('../images/home_icons/ic_3.png')}
                                        showText={'我的商城'} tag={'wdsc'}
                                        onClick={this._onMenuClick}/>
                            <MenuButton renderIcon={require('../images/home_icons/ic_4.png')}
                                        showText={'签到'} tag={'qd'}
                                        onClick={this._onMenuClick}/>
```

添加点击事件

```
//构造参数中添加
this._onMenuClick = this._onMenuClick.bind(this);

添加点击方法，调用原生的Toast

 _onMenuClick(title, tag) {
        NativeModules.AndroidToast.androidToast(title);
    }

```

####四、添加“猜你喜欢”
```
 <View style={styles.menuView}>
                            <Image style={styles.tabIcon}  source={lineImg}/>
                            <Text style={{color:'#333333',fontSize:18,padding:10,paddingTop:13}}>猜你喜欢</Text>
                        </View>
```
####五、添加List列表
List列表位于搜索栏的底部，List的中包括了banner、四个按钮、产品列表
**1、添加ListView**
```
 <ListView
                style={{flex:1,backgroundColor:'#eeeeee'}}
                dataSource={this.state.listData}
                renderRow={this._renderRow}
                renderHeader={()=>{return(
                    <View>
                        <ViewPager
                            style={{height:160}}
                            dataSource={this.state.dataSource}
                            renderPage={this._renderPage}
                            isLoop={true}
                            autoPlay={true}
                        />
                        <View style={styles.menuView}>
                            <MenuButton renderIcon={require('../images/home_icons/ic_1.png')}
                                        showText={'分类'} tag={'fl'}
                                        onClick={this._onMenuClick}/>
                            <MenuButton renderIcon={require('../images/home_icons/ic_2.png')}
                                        showText={'购物车'} tag={'gwc'}
                                        onClick={this._onMenuClick}/>
                            <MenuButton renderIcon={require('../images/home_icons/ic_3.png')}
                                        showText={'我的商城'} tag={'wdsc'}
                                        onClick={this._onMenuClick}/>
                            <MenuButton renderIcon={require('../images/home_icons/ic_4.png')}
                                        showText={'签到'} tag={'qd'}
                                        onClick={this._onMenuClick}/>
                        </View>
                        {/*<View style={{marginTop:15,borderWidth:0.5,borderColor:'#ccc'}}/>*/}
                        <View style={styles.menuView}>
                            <Image style={styles.tabIcon}  source={lineImg}/>
                            <Text style={{color:'#333333',fontSize:18,padding:10,paddingTop:13}}>猜你喜欢</Text>
                        </View>

                    </View>)}}>
            </ListView>
```
**2、构造器中添加数据源**

```
  var ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
  this.state = {
           listData: ds
        }
```

暂时不明白怎么处理的数据
```
  componentWillMount() {
        fetch('http://m.jd.com/index/recommend.action?_format_=json&page=1')
            .then((res)=> res.json())
            .then((str)=> {
                let arr = JSON.parse(str.recommend).wareInfoList;

                var rows = [];
                for (let i = 0; i < arr.length; i += 2) {
                    var item = {id: i, left: null, right: null};
                    item.left = (arr[i]);
                    if (i < arr.length - 1) {
                        item.right = (arr[i + 1]);
                    }
                    rows.push(item);
                }
                var ds = this.state.listData.cloneWithRows(rows);

                this.setState({listData: ds});
            });
    }
```

**3、渲染列表样式**
效果图：
![输入图片说明](https://git.oschina.net/uploads/images/2017/0720/171832_74b4664d_684224.png "img_item.png")
```
    _renderRow(rowData) {
        return (
            <View style={{flexDirection:'row'}}>
                <TouchableWithoutFeedback style={{flex:1,alignItems:'center'}}
                                          onPress={()=>{this._onRecommendClick(rowData.left.wareId)}}>
                    <View style={{flex:1,backgroundColor:'white',marginLeft:10,marginRight:20,marginBottom:20,borderRadius:5}}>
                        <Image style={{width:40,height:40,position:'absolute', top:0,left:0}} source={require('../images/ic_jiaobiao.png')} />
                        <View style={{flex:1,alignItems:'center'}}>
                        <Image resizeMode={'stretch'} source={{uri:rowData.left.imageurl}}
                               style={{width:len,height:len}}/>
                        <Text numberOfLines={2} style={styles.recommendTitle}>{rowData.left.wname}</Text>
                        {/*<View style={{width:len,borderWidth:0.5,borderColor:'#d7d7d7'}}/>*/}
                        <View
                            style={{flexDirection:'row',width:len, marginTop: 6, marginBottom: 22,alignItems:'flex-start'}}>
                            <Text style={styles.priceText}>￥{rowData.left.jdPrice}</Text>
                        </View>

                    </View>

                    </View>
                </TouchableWithoutFeedback>
                <TouchableWithoutFeedback style={{flex:1,alignItems:'center'}}
                                          onPress={()=>{this._onRecommendClick(rowData.right.wareId)}}>
                    <View style={{flex:1,backgroundColor:'white',marginLeft:10,marginRight:20,marginBottom:20,borderRadius:5}}>
                        <Image style={{width:40,height:40,position:'absolute'}} source={require('../images/ic_jiaobiao.png')} />
                    <View style={{flex:1,alignItems:'center'}}>
                        <Image resizeMode={'stretch'} source={{uri:rowData.right.imageurl}}
                               style={{width:len,height:len}}/>
                        <Text numberOfLines={2} style={styles.recommendTitle}>{rowData.right.wname}</Text>
                        {/*<View style={{width:len,borderWidth:0.5,borderColor:'#d7d7d7'}}/>*/}
                        <View
                            style={{flexDirection:'row',width:len, marginTop: 6, marginBottom: 22,alignItems:'flex-start'}}>
                            <Text style={styles.priceText}>￥{rowData.right.jdPrice}</Text>
                        </View>

                    </View>

                    </View>
                </TouchableWithoutFeedback>
            </View>
        );
    }

```