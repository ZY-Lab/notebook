###ReactNative前端与原生事件交互3
#####一、Android原生向RN传递数据

**第一步：**创建MyReactDelegate
```java
public class MyReactDelegate extends ReactActivityDelegate {
    public MyReactDelegate(Activity activity, @Nullable String mainComponentName) {
        super(activity, mainComponentName);
    }

    public MyReactDelegate(FragmentActivity fragmentActivity, @Nullable String mainComponentName) {
        super(fragmentActivity, mainComponentName);
    }
    @javax.annotation.Nullable
    @Override
    protected Bundle getLaunchOptions() {
        Bundle bundle = new Bundle();
        bundle.putString("bundle","androisdfsfsdf");
        return bundle;
    }
}

}
```

**第二步：**MainActivity中

```java
 @Override
    protected ReactActivityDelegate createReactActivityDelegate() {
        return new MyReactDelegate(this,getMainComponentName());
    }
}

```
**第三步：**RN中实现

```JavaScript
 var  initProps = this.props.bundle;
    return (
                <Text style={styles.instructions}>
                    {initProps}
                </Text>
        );
```
