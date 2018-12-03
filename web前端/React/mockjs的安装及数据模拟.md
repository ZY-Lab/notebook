#### 1.安装mock.js

>npm install mockjs --save-dev


#### 2.使用 Mock
```js
const Mock = require('mockjs')
```

**使用实例:**
```js
const data = Mock.mock({
    属性 list 的值是一个数组，其中含有 1 到 10 个元素
    list|1-10': [{
    属性 id 是一个自增数，起始值为 1，每次增 1
     'id|+1': 1
    }]
})
```

**输出结果:**
```
console.log(JSON.stringify(data, null, 4))
```
>此数组内容为随机输出:
>
    {
     "list": [
         {
             "id": 1
         },
         {
             "id": 2
         },
         {
             "id": 3
         }
     ]
    }


#### 3.数据模板定义规范 DTD
**数据模板中的每个属性由3部分构成：*属性名*、*生成规则*、*属性值*：**

* 属性名   name
* 生成规则 rule
* 属性值   value
`'name|rule': value`
>***注意：***
*属性名 和 生成规则 之间用竖线 | 分隔。
生成规则 是可选的。*

**生成规则有7种格式：**

1. 'name|min-max': value
2. 'name|count': value
3. 'name|min-max.dmin-dmax': value
4. 'name|min-max.dcount': value
5. 'name|count.dmin-dmax': value
6. 'name|count.dcount': value
7. 'name|+step': value

生成规则 的 含义 需要依赖 属性值的类型 才能确定。
属性值 中可以含有 @占位符。
属性值 还指定了最终值的初始值和类型。

**生成规则和示例：**
```js
// 配置 Mock 路径
const Mock = require('mockjs');
const Random = Mock.Random;
const data = Mock.mock({
  // 属性 list 的值是一个数组，其中含有 1 到 10 个元素
  'list|1-10': [{
    // 属性 key 是一个自增数，起始值为 1，每次增 1
    'key|+1': 1,
    //属性值是数组 Array 从属性值 array 中随机选取 1 个元素，作为最终值
    'name|1': ['面包', '奶粉', '衣服', '啤酒'],
    //从属性值 array 中顺序选取 1 个元素，作为最终值。
    'state|+1': ['出售中', '出售中', '已下架', '违规'],
    //生成一个浮点数,整数部分大于等于1、小于等于 100，小数部分保留2位。
    'price|1-100.2': 1,
    //生成一个大于等于 1、小于等于 100 的整数，属性值 100只是用来确定类型。
    //指示生成的日期和时间字符串的格式。默认值为 yyyy-MM-dd HH:mm:ss。
     time:Random.datetime('yyyy-MM-dd  HH:mm:ss'),
  }],
});
```
>输出结果:
 console.log(JSON.stringify(data, null, 4));
 console.log(data.list);
 module.exports = data.list;


#### 4.在其他地方引用数据模块
**导入数据模块所在的位置，将数据存到`data`里面**
```
import data from '../../mock/products';
```
以table为例引用data
```
<Table rowSelection={rowSelection} columns={columns} dataSource={data} />
```
>详细内容请查看：[mock文档](https://github.com/nuysoft/Mock/wiki)