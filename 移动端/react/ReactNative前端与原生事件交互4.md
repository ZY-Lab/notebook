###ReactNative前端与原生事件交互4
#####一、Android原生向RN传递数据（通过回调函数的方式）
>**在MyNativeModule中添加dataToJS回调方法**

```java
public void dataToJS(Callback successBack,Callback errorBack){
      try {
          String result = "成功";
          if (TextUtils.isEmpty(result)) {
              result = "没有数据";
          }
          successBack.invoke(result);
      }catch (Exception  e){
          errorBack.invoke(e.getMessage());
      }
   }

```

>**在RN端接受native传递过来的数据**

```JavaScript
 CallAndroid2=()=>{
        //进行从Activity中获取数据传输到JS
        NativeModules.MyNativeModule.dataToJS((successBack) => {
                NativeModules.MyNativeModule.rnCallNative('JS界面:'+successBack);
            },
            (result) => {
                NativeModules.MyNativeModule.rnCallNative('JS界面:错误信息为:'+result);
            })
    }

```
