## 安装
- npm install whatwg-fetch --save-dev; 要么
- bower install fetch; 要么
- yarn add whatwg-fetch
> 导入：import fetch from 'dva/fetch';

## 用法
#### HTML

```
fetch('/users.html')
  .then(function(response) {
    return response.text()
  }).then(function(body) {
    document.body.innerHTML = body
  })
```
#### JSON

```
fetch('/users.json')
  .then(function(response) {
    return response.json()
  }).then(function(json) {
    console.log('parsed json', json)
  }).catch(function(ex) {
    console.log('parsing failed', ex)
  })
```
#### Response metadata

```
fetch('/users.json').then(function(response) {
  console.log(response.headers.get('Content-Type'))
  console.log(response.headers.get('Date'))
  console.log(response.status)
  console.log(response.statusText)
})
```
#### Post form

```
var form = document.querySelector('form')

fetch('/users', {
  method: 'POST',
  body: new FormData(form)
})
```
#### Post JSON

```
fetch('/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Hubot',
    login: 'hubot',
  })
})
```
#### File upload

```
var input = document.querySelector('input[type="file"]')

var data = new FormData()
data.append('file', input.files[0])
data.append('user', 'hubot')

fetch('/avatars', {
  method: 'POST',
  body: data
})
```
*注意事项*
- 即使响应是HTTP 404或500，则返回的Promise fetch() 也不会拒绝HTTP错误状态。相反，它将正常解析，只会拒绝网络故障或阻止请求完成。
- 默认情况下，fetch 不会从服务器发送或接收任何Cookie，如果站点依赖于维护用户会话，则会导致未经身份验证的请求。

## 处理HTTP错误状态
要使fetchPromise拒绝HTTP错误状态，即在任何非2xx状态下，定义一个自定义响应处理程序：
```
function checkStatus(response) {
  if (response.status >= 200 && response.status < 300) {
    return response
  } else {
    var error = new Error(response.statusText)
    error.response = response
    throw error
  }
}

function parseJSON(response) {
  return response.json()
}

fetch('/users')
  .then(checkStatus)
  .then(parseJSON)
  .then(function(data) {
    console.log('request succeeded with JSON response', data)
  }).catch(function(error) {
    console.log('request failed', error)
  })
```
## 发送Cookie
要自动发送当前域的Cookie，credentials必须提供该选项：
```
fetch('/users', {
  credentials: 'same-origin'
})
```
“同源”值使得fetch与Cookie相似的XMLHttpRequest类似。否则，Cookie将不会被发送，导致这些请求不保留认证会话。

对于CORS请求，使用“include”值允许将凭据发送到其他域：
```
fetch('https://example.com:1234/users', {
  credentials: 'include'
})
```