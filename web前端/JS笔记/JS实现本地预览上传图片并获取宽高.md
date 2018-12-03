### JS实现本地预览上传图片并获取宽高  

我们在本地上传文件、图片是用file类型的表单，大多时候我们想让上传的图片先预览在我们本地，下面来看看代码吧。


#### HTML部分：  
```js
<input type="file" accept="image/jpg,image/jpeg,image/png" name="file" onchange="selectImg(this)">
<br>
<img id="showImg" src="" alt="" width="">
我们给上传表单的标签加一个  accept=”image/jpg,image/jpeg,image/png” ，这样会使打开文件的速度快一点。
```  

#### JS部分：  
```js
function selectImg(file) {
    if (!file.files || !file.files[0]) {
        return;
    }
    //定以一个读取文件的对象
    var reader = new FileReader();
   
    reader.onload = function (evt) {
        //获取的是图片的base64代码
        var replaceSrc = evt.target.result;
        // 再将获取值赋给img标签
        $('#showImg').attr("src", replaceSrc);
    };
    reader.readAsDataURL(file.files[0]);
}
```  
上面就实现了上传图片是本地预览图片了。  

我们可以通过下面这句代码获得图片的其他信息↓  

`console.log(file.files);`  

可以从上面的截图看到，有图片的名字、大小、格式等。但是没有图片的宽度和高度，获取图片的宽度和高度需要用到Image() 对象。  
```js
function selectImg(file) {
    if (!file.files || !file.files[0]) {
        return;
    }
    //定以一个读取文件的对象
    var reader = new FileReader();

    reader.onload = function (evt) {
        //获取的是图片的base64代码
        var replaceSrc = evt.target.result;

        //定义一个Image对象
        var image = new Image();
        image.src = replaceSrc;
        console.log("图片宽度：" + image.width + " px");
        console.log("图片高度：" + image.height + " px");

        // 再将获取值赋给img标签
        $('#showImg').attr("src", replaceSrc);
    };
    reader.readAsDataURL(file.files[0]);
}
```