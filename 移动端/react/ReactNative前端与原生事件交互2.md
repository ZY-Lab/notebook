###ReactNative前端与原生事件交互
#####一、点击页面按钮，弹出Android的Toast

**第一步：**创建MyNativeModule
```java
public class MyNativeModule extends ReactContextBaseJavaModule {
    private Context mContext;
    public MyNativeModule(ReactApplicationContext reactContext) {
        super(reactContext);
        mContext = reactContext;
    }

    @Override
    public String getName() {
        return "MyNativeModule";
    }
    @ReactMethod
    public void rnCallNative(String msg){

        Toast.makeText(mContext,msg,Toast.LENGTH_SHORT).show();

    }

}
```
**第二步：**创建MyReactPackage
```java
public class MyReactPackage implements ReactPackage{
    @Override
    public List<NativeModule> createNativeModules(ReactApplicationContext reactContext) {
        List<NativeModule> modules=new ArrayList<>();
        //将我们创建的类添加进原生模块列表中  
        modules.add(new MyNativeModule(reactContext));
        return modules;
    }

    @Override
    public List<Class<? extends JavaScriptModule>> createJSModules() {
        //返回值需要修改  
        return Collections.emptyList();
    }

    @Override
    public List<ViewManager> createViewManagers(ReactApplicationContext reactContext) {
        return Collections.emptyList();
    }
}

```
**第三步：**添加包管理文件
```java
 @Override
    protected List<ReactPackage> getPackages() {
      return Arrays.<ReactPackage>asList(
          new MainReactPackage(),
              new MyReactPackage()
      );
    }

```
**第四步：**index.android.js中处理
```JavaScript
   render() {
        return (
            <View style={styles.container}>

              <Text style={styles.welcome}
                    onPress={this.call_button.bind(this)}
              >
                React Native 调用原生方法!
              </Text>

              <Text style={styles.instructions}>
                To get started, edit index.android.js
              </Text>

              <Text style={styles.instructions}>
                Double tap R on your keyboard to reload,{'\n'}
                Shake or press menu button for dev menu
              </Text>

            </View>
        );
    }

    call_button(){

        NativeModules.MyNativeModule.rnCallNative('调用原生方法的Demo');
    }
```
