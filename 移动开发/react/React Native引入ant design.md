###React Native中使用ant design
####一、安装和初始化
需要在命令行中安装相应工具,并且需要安装安装 yarn
```
npm install -g yarn
npm install -g create-react-app  # web 项目
npm install -g create-react-native-app  # react-native 项目


```
####二、创建项目
```
create-react-app antm-demo  # web 项目
create-react-native-app antm-demo  # react-native 项目
```

**启动项目**

```
yarn start
```
**运行项目**
```
yarn run android
```
####三、引入 antd-mobile
```
yarn add antd-mobile
yarn add babel-plugin-import --dev

```

####四、修改某些配置
1、修改 .babelrc 配置，并重新启动服务
```
{
  "presets": ["babel-preset-expo"],
  "plugins": [["import", { "libraryName": "antd-mobile" }]],
  "env": {
    ...
  }
}
```
2、修改 App.js, 引入 antd-mobile 按钮组件。
```
...
import { Button } from 'antd-mobile';

...
render() {
  return (
    ...
    <Button>antd-mobile button</Button>
    ...
  );
}
```
