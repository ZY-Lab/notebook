## 如何用node.js发送邮件  
### 一、准备工作  
##### 1、新建一个目录，这儿取名叫email  

##### 2、在email目录里创建一个package.json
`cnpm init`  

##### 2、在email目录里安装nodemailer模块   
`cnpm install nodemailer --save`   

##### 3、在email目录里面新建一个js文件，这儿取名叫main  

### 二、代码部分  
```js
var nodemailer = require('nodemailer');//导入模块

var transporter = nodemailer.createTransport({
    service: 'QQ', //
    auth: {
        user: 'XXXXXXX@qq.com', //邮箱帐号
        pass: 'XXXXXXXXXXXX' //这儿是指授权码，在邮箱设置里获取
    }
});

var mailOptions = {
    from: 'XXXXXXX@qq.com', // 发送者邮箱
    to: 'XXXXXXX@qq.com', // 接受者邮箱
    subject: 'Hello', // 邮件主题
    text: '这个一封测试邮件', // 明文
    html: '<div>这是一封测试邮件</div>',// html body
    attachments: [ //发送附件
        {
            filename: 'bz001.jpg', //附件名字
            path: './img/bz001.jpg'  //附件所在的本地路径
        }
    ]
};

transporter.sendMail(mailOptions, function(error, info){
    if(error){
        console.log(error);
    }else{
        console.log('Message sent: ' + info.response);
    }
});
```  

>最后`node main.js`就发送邮件了
