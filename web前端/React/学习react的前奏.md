#### 学习react的前奏

##### 一、下载Chrome的React扩展程序
**这一步将对后面学习react很重要**

谷歌应用商店网址：https://chrome.google.com/webstore/category/extensions?hl=zh-CN
>*这里访问chrom应用商城需要翻墙*

推荐一个免费的翻墙工具：开眼
https://www.lanternchrome.top/
>*后面运行react项目的时候需要将开眼翻墙工具关掉*

##### 二、安装node.js

* node.js安装地址：https://nodejs.org/zh-cn/download/
* 将npm换成淘宝镜像的cnpm：

  `npm install -g cnpm --registry=https://registry.npm.taobao.org`

##### 三、使用npm创建dva-cli的项目

*dva 是一个基于 react 和 redux 的轻量应用框架

1.通过 npm/cnpm 安装 dva-cli:

`cnpm install dva-cli -g`

2.创建新应用:

`dva new dva-quickstart`

3.cd 进入 dva-quickstart 目录

`cd dva-quickstart`

4.启动开发服务器

`npm start`

##### 四、dva项目结构分析
>原文：https://github.com/pigcan/blog/issues/2

```
├── assets
│   └── yay.jpg
├── components
│   └── Example.js
├── models
│   └── example.js
├── routes
│   ├── IndexPage.css
│   └── IndexPage.js
├── services
│   └── example.js
├── tests
│   └── models
│       └── example-test.js
└── utils
│   └── request.js
├── index.css
├── index.js
├── router.js
```

`assets`: 我们可以把项目 assets 资源丢在这边

`components`: 纯组件，在 dva 应用中 components 目录中应该是一些 logicless 的 component, logic 部分均由对应的 route-component 来承载。在安装完 dva-cli 工具后，我们可以通过 dva g component componentName 的方式来创建一个 component。
`index.css`: 首页样式

`index.js`: dva 应用启动 五部曲，这点稍后再展开

`models`: 该目录结构用以存放 model，在通常情况下，一个 model 对应着一个 route-component，而 route-component 则对应着多个 component，当然这取决于你如何拆分，个人偏向于尽可能细粒度的拆分。在安装完 dva-cli 工具后，我们可以通过 dva g model modelName 的方式来创建一个 model。该 model 会在 index.js 中自动注册。

`router.js`: 页面相关的路由配置，相应的 route-component 的引入

`routes`: route-component 存在的地方，在安装完 dva-cli 工具后，我们可以通过 dva g route route-name 的方式去创建一个 `route-component`，该路由配置会被自动更新到 route.js 中。route-component 是一个重逻辑区，一般业务逻辑全部都在此处理，通过 connect 方法，实现 model 与 component 的联动。

`services`: 全局服务，如发送异步请求

`tests`: 测试相关

`utils`: 全局类公共函数

**dva 的五部曲**
```js
import './index.html';
import './index.css';
import dva from 'dva';

// 1. Initialize
const app = dva();

// 2. Plugins - 该项为选择项
//app.use({});

// 3. Model 的注册
//app.model(require('./models/example'));

// 4. 配置 Router
app.router(require('./router'));

// 5. Start
app.start('#root');
```

