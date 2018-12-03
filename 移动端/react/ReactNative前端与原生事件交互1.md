###ReactNative前端与原生事件交互
#####一、点击页面按钮，原生向JavaScript端发送事件

**第一步：**创建MyModule
```java
public class MyModule extends ReactContextBaseJavaModule {

    public MyModule(ReactApplicationContext reactContext) {

        super(reactContext);

        //给上下文对象赋值
        Test.myContext=reactContext;
    }

    @Override
    public String getName() {

        return "MyModule";
    }


    @ReactMethod
    public void  NativeMethod()
    {
        //调用Test类中的原生方法。
        new Test().fun();
    }
}

```
**第二步：**创建MyPackage
```java
public class MyPackage implements ReactPackage {
    @Override
    public List<NativeModule> createNativeModules(ReactApplicationContext reactContext) {

        List<NativeModule> modules=new ArrayList<>();
        modules.add(new MyModule(reactContext));

        return modules;
    }

    @Override
    public List<Class<? extends JavaScriptModule>> createJSModules() {
        return Collections.emptyList();
    }

    @Override
    public List<ViewManager> createViewManagers(ReactApplicationContext reactContext) {
        return Collections.emptyList();
    }
}

```
**第三步：**创建Test
```java
public class Test {

     //定义上下文对象
    public static ReactContext myContext;

    //定义发送事件的函数
    public  void sendEvent(ReactContext reactContext, String eventName, @Nullable WritableMap params)
    {
        System.out.println("reactContext="+reactContext);

        reactContext
                .getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)
                .emit(eventName,params);
    }

    public  void fun()
    {
        //在该方法中开启线程，并且延迟3秒，然后向JavaScript端发送事件。
        new Thread(new Runnable() {
            @Override
            public void run() {

                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

               //发送事件,事件名为EventName
                WritableMap et= Arguments.createMap();
                sendEvent(myContext,"EventName",et);


            }
        }).start();

    }


}


```
**第四步：**index.android.js中处理
```JavaScript
import React, { Component } from 'react';
import {
 AppRegistry,
  StyleSheet,
  Text,
  DeviceEventEmitter,
  NativeModules,
  View
} from 'react-native';

export default class ReactAndroid extends Component {

    componentWillMount(){  
                      //监听事件名为EventName的事件
                    // DeviceEventEmitter.addListener('EventName', function() {  
                         
                    //      this.showState();

                    //      alert("send success");  
                    //      // this.showState();

                    //    }); 

                    DeviceEventEmitter.addListener('EventName', ()=> {  
                         
                         this.showState();
                         alert("send success");  

                       }); 
                
}

  constructor(props) {
    super(props);
    this.state = {
        content: '这个是预定的接受信息',
    }
}

  render() {
    return (
      <View style={styles.container}>

        <Text style={styles.welcome}
         onPress={this.callNative.bind(this)}
        >
          当你点我的时候会调用原生方法，原生方法延迟3s后会向前端发送事件。
          前端一直在监听该事件，如果收到，则给出alert提示!
        </Text>
        
        <Text style={styles.welcome} >
        {this.state.content}
         </Text>


      </View>
    );
  }

  callNative()
  {
    NativeModules.MyModule.NativeMethod();
  }
 
  showState()
  {
       this.setState({content:'已经收到了原生模块发送来的事件'})
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  instructions: {
    textAlign: 'center',
    color: '#333333',
    marginBottom: 5,
  },
});

AppRegistry.registerComponent('ReactAndroid', () => ReactAndroid);

```
