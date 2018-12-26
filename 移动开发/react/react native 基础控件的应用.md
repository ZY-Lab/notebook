####React Native基础控件应用

- **React：**基础框架，主要涉及实现的理念，不能做网页开发和移动开发
- **React.js：**在React框架的基础之上发展的，专门用来做网页开发的
- **ReactNative：**用来做移动开发的

#####1、React的开发------编写Hello World
```
import React, { Component } from 'react';
import { AppRegistry, Text } from 'react-native';

class HelloWorldApp extends Component {
  render() {
    return (
      <Text>Hello world!</Text>
    );
  }
}

// 注意，这里用引号括起来的'HelloWorldApp'必须和你init创建的项目名一致
AppRegistry.registerComponent('HelloWorldApp', () => HelloWorldApp);
```
**注：**AppRegistry模块则是用来告知React Native哪一个组件被注册为整个应用的根容器。你无需在此深究，因为一般在整个应用里AppRegistry.registerComponent这个方法只会调用一次。上面的代码里已经包含了具体的用法，你只需整个复制到index.ios.js或是index.android.js文件中即可运行。

#####2、 Props属性
（1）大多数组件在创建时就可以使用各种参数来进行定制。用于定制的这些参数就称为**props（属性）**。

（2）**通过显示一张图片为例：**
在创建一个图片时，可以传入一个名为source的prop来指定要显示的图片的地址，以及使用名为style的prop来控制其尺寸。



```JavaScript
import React, { Component } from 'react';
import { AppRegistry, Image } from 'react-native';

class Bananas extends Component {
  render() {
    let pic = {
      uri: 'https://upload.wikimedia.org/wikipedia/commons/d/de/Bananavarieties.jpg'
    };
    return (
      <Image source={pic} style={{width: 193, height: 110}} />
    );
  }
}

AppRegistry.registerComponent('Bananas', () => Bananas);
```
#####3、State（状态）
#####4、样式
（1）所有的核心组件都接受名为style的属性。这些样式名基本上是遵循了web上的CSS的命名，只是按照JS的语法要求使用了驼峰命名法，例如将background-color改为backgroundColor。

**实际开发中组件的样式会越来越复杂，我们建议使用StyleSheet.create来集中定义组件的样式。**

（2）**例子**


```JavaScript
import React, { Component } from 'react';
import { AppRegistry, StyleSheet, Text, View } from 'react-native';

class LotsOfStyles extends Component {
    render() {
        return (
            <View>
                <Text style={styles.red}>just red</Text>
                <Text style={styles.bigblue}>just bigblue</Text>
                <Text style={[styles.bigblue, styles.red]}>bigblue, then red</Text>
                <Text style={[styles.red, styles.bigblue]}>red, then bigblue</Text>
                <Text style={[styles.green]}>啦啦啦啦啦啦啦</Text>
            </View>
        );
    }
}
const styles = StyleSheet.create({
    bigblue: {
        color: 'blue',
        fontWeight: 'bold',
        fontSize: 30,
    },
    red: {
        color: 'red',
    },
    green: {
        color: 'green',
        fontSize:60
    },
});
AppRegistry.registerComponent('FirstTest', () => LotsOfStyles);
```
**页面效果**
![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/104020_d684d3d3_684224.png "在这里输入图片标题")
**注：常见的做法是按顺序声明和使用style属性，以借鉴CSS中的“层叠”做法（即后声明的属性会覆盖先声明的同名属性）。**

#####4、高度与宽度
（1）指定宽高

在样式中指定固定的width和height。React Native中的尺寸都是无单位的，表示的是与设备像素密度无关的逻辑像素点。

```JavaScript
import React, { Component } from 'react';

import { AppRegistry, View } from 'react-native';

class FixedDimensionsBasics extends Component {
  render() {
    return (
      <View>
        <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{width: 100, height: 100, backgroundColor: 'skyblue'}} />
        <View style={{width: 150, height: 150, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};
// 注册应用(registerComponent)后才能正确渲染
// 注意：只把应用作为一个整体注册一次，而不是每个组件/模块都注册
AppRegistry.registerComponent('AwesomeProject', () => FixedDimensionsBasics);
```
**页面效果**
![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/112004_41afc263_684224.png "在这里输入图片标题")


（2）弹性（Flex）宽高

在组件样式中使用flex可以使其在可利用的空间中动态地扩张或收缩。**一般而言我们会使用flex:1来指定某个组件扩张以撑满所有剩余的空间。**如果有多个并列的子组件使用了flex:1，则这些子组件会平分父容器中剩余的空间。如果这些并列的子组件的flex值不一样，则谁的值更大，谁占据剩余空间的比例就更大（即占据剩余空间的比等于并列组件间flex值的比）。

**组件能够撑满剩余空间的前提是其父容器的尺寸不为零。**如果父容器既没有固定的width和height，也没有设定flex，则父容器的尺寸为零。其子组件如果使用了flex，也是无法显示的。

```JavaScript
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';


class FlexDimensionsBasics extends Component {
    render() {
        return (
            // 试试去掉父View中的`flex: 1`。
            // 则父View不再具有尺寸，因此子组件也无法再撑开。
            // 然后再用`height: 300`来代替父View的`flex: 1`试试看？
            <View style={{flex: 1}}>
                <View style={{flex: 1, backgroundColor: 'powderblue'}} />
                <View style={{flex: 2, backgroundColor: 'skyblue'}} />
                <View style={{flex: 3, backgroundColor: 'steelblue'}} />
            </View>
        );
    }
};
// 注册应用(registerComponent)后才能正确渲染
// 注意：只把应用作为一个整体注册一次，而不是每个组件/模块都注册
AppRegistry.registerComponent('FirstTest', () => FlexDimensionsBasics);
```

**页面效果**
 ![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/114710_e5421336_684224.png "在这里输入图片标题")

#####5、使用Flexbox布局
React Native中使用flexbox规则来指定某个组件的子元素的布局。Flexbox可以在不同屏幕尺寸上提供一致的布局结构。

一般来说，使用flexDirection、alignItems和 justifyContent三个样式属性就已经能满足大多数布局需求。


**flexDirection的默认值是column而不是row，而flex也只能指定一个数字值。**

（1）Flex Direction

在组件的style中指定flexDirection可以决定布局的主轴。子元素是应该沿着水平轴(row)方向排列，还是沿着竖直轴(column)方向排列呢？默认值是竖直轴(column)方向。

```JavaScript
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';

class FlexDirectionBasics extends Component {
  render() {
    return (
      // 尝试把`flexDirection`改为`column`看看
      <View style={{flex: 1, flexDirection: 'row'}}>
        <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};

AppRegistry.registerComponent('AwesomeProject', () => FlexDirectionBasics);
```
**页面效果**

![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/140249_f345bcc4_684224.png "在这里输入图片标题")

**flexDirection: 'column'  页面效果**
![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/140431_30a017fa_684224.png "在这里输入图片标题")

（2）Justify Content
在组件的style中指定justifyContent可以决定其子元素沿着主轴的排列方式。
- flex-start
- center
- flex-end
- space-around
- space-between

```JavaScript
import React, { Component } from 'react';
import { AppRegistry, View } from 'react-native';

class JustifyContentBasics extends Component {
  render() {
    return (
      // 尝试把`justifyContent`改为`center`看看
      // 尝试把`flexDirection`改为`row`看看
      <View style={{
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'space-between',
      }}>
        <View style={{width: 50, height: 50, backgroundColor: 'powderblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'skyblue'}} />
        <View style={{width: 50, height: 50, backgroundColor: 'steelblue'}} />
      </View>
    );
  }
};

AppRegistry.registerComponent('AwesomeProject', () => JustifyContentBasics);
```

**页面效果**

![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/141733_c813e001_684224.png "在这里输入图片标题")

**justifyContent: 'flex-start'  页面效果**

![输入图片说明](https://git.oschina.net/uploads/images/2017/0711/141742_d3a894b9_684224.png "在这里输入图片标题")