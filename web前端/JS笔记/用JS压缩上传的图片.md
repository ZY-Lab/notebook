### 用JS压缩上传的图片  

现在网上的高清原图尺寸也有好几M甚至更大，而且现在手机像素高了拍出来的照片也特别大，所以有时候需要对用户上传图片时进行压缩处理。  

**图片压缩的原理：将图片重新画入到canvas画布里面，再将canvas转成图片的形式。**  


#### 图片压缩js代码：  
```js
function compressedImg(path, callback) {
    var img = new Image();
    img.src = path;
    img.onload = function () {
        var that = this;
        // 默认按比例压缩
        var w = that.width,
            h = that.height;
        // quality值越小，所绘制出的图像越模糊
        var quality = 0.7;  // 默认图片质量为0.7，
        //生成canvas
        var canvas = document.createElement('canvas');
        var ctx = canvas.getContext('2d');
        // 创建属性节点
        var anw = document.createAttribute("width");
        anw.nodeValue = w;
        var anh = document.createAttribute("height");
        anh.nodeValue = h;
        canvas.setAttributeNode(anw);
        canvas.setAttributeNode(anh);
        ctx.drawImage(that, 0, 0, w, h);
        var base64 = canvas.toDataURL('image/jpeg', quality);
        // 回调函数返回base64的值
        callback(base64);
    }
}
```  

#### 预览图片及压缩代码：  
```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>JS图片压缩</title>
</head>
<body>

<input type="file" accept="image/jpg,image/jpeg,image/png" name="file" onchange="selectImg(this)">
<br>
<img id="showImg" src="" alt="" width="">

<script src="jquery-2.1.1.js"></script>
<script>
    function selectImg(file) {
        if (!file.files || !file.files[0]) {
            return;
        }
        //定以一个读取文件的对象
        var reader = new FileReader();
        console.log("图片原始大小：" + file.files[0].size / 1024 + "KB");

        reader.onload = function (evt) {
            //获取的是图片的base64代码
            var replaceSrc = evt.target.result;
            //定义一个Image对象
            var image = new Image();
            image.src = replaceSrc;

            compressedImg(replaceSrc,function (base) {
                document.getElementById("showImg").src = base;
                console.log("压缩后：" + base.length / 1024 + "KB");
            });

            // 再将获取值赋给img标签
            $('#showImg').attr("src", replaceSrc);
        };
        reader.readAsDataURL(file.files[0]);
    }

    //图片压缩代码
    function compressedImg(path, callback) {
        var img = new Image();
        img.src = path;
        img.onload = function () {
            var that = this;
            // 默认按比例压缩
            var w = that.width,
                h = that.height;
            var quality = 0.7;  // 默认图片质量为0.7
            //生成canvas
            var canvas = document.createElement('canvas');
            var ctx = canvas.getContext('2d');
            // 创建属性节点
            var anw = document.createAttribute("width");
            anw.nodeValue = w;
            var anh = document.createAttribute("height");
            anh.nodeValue = h;
            canvas.setAttributeNode(anw);
            canvas.setAttributeNode(anh);
            ctx.drawImage(that, 0, 0, w, h);
            // quality值越小，所绘制出的图像越模糊
            var base64 = canvas.toDataURL('image/jpeg', quality);
            // 回调函数返回base64的值
            callback(base64);
        }
    }

</script>

</body>
</html>
```  

因为用canvas画布转化图片是base64代码的形式，上传我们需要转成Blob对象的形式，再上传。  

#### 上传压缩图片ajax部分代码:  
```js
//dataURL转成Blob对象
function dataURLtoBlob(dataURI) {
    var byteString = atob(dataURI.split(',')[1]);
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
    var ab = new ArrayBuffer(byteString.length);
    var ia = new Uint8Array(ab);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }
    return new Blob([ab], {type: mimeString});
}

//上传
var fd = new FormData();
function upform() {
    var img = $("#showImg").attr("src");
    if (img) {
        var blob = dataURLtoBlob(img);
        fd.append('file', blob);
    }
    $.ajax({
        type: "post",
        url: "假装有接口",
        data: fd,
        dataType: "json",
        async: false,
        processData: false,
        xhrFields: {
            withCredentials: true
        },
        success: function (data) {

        },
        error: function (err) {
            console.log(fd);
        }
    });
}
``` 