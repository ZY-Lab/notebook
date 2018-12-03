#### 一、安装
```
npm install --save react-cropper
```
##### 二、使用
```
import React, {Component} from 'react';
import Cropper from 'react-cropper';
import 'cropperjs/dist/cropper.css'; // see installation section above for versions of NPM older than 3.0.0
// If you choose not to use import, you need to assign Cropper to default
// var Cropper = require('react-cropper').default

class Demo extends Component {
  _crop(){
    // image in dataUrl
    console.log(this.refs.cropper.getCroppedCanvas().toDataURL());
  }

  render() {
    return (
      <Cropper
        ref='cropper'
        src='http://fengyuanchen.github.io/cropper/img/picture.jpg'
        style={{height: 400, width: '100%'}}
        // Cropper.js options
        aspectRatio={16 / 9}
        guides={false}
   />
    );
  }
}
```
*注意：使用的过程中不要忘记引入==cropperjs/dist/cropper.css==，否则插件不显示。*

- aspectRatio： 纵横比；
- guides：true为带有栅格线，false则无；
##### 三、上传图片
```
<input type="file" onChange={this.onChange} />
```
函数onChange：
 ```
onChange(e) {
    e.preventDefault();
    let files;
    if (e.dataTransfer) {
      files = e.dataTransfer.files;
    } else if (e.target) {
      files = e.target.files;
    }
    const reader = new FileReader();
    reader.onload = () => {
      this.setState({ src: reader.result });
    };
    reader.readAsDataURL(files[0]);
  }
```
##### 五、裁剪与显示
```
<div className="box">
    <Button onClick={this.cropImage} >确定</Button>
    <img src={this.state.cropResult}  />
</div>
```
函数cropImage
```
  cropImage() {
    if (typeof this.cropper.getCroppedCanvas() === 'undefined') {
      return;
    }
    this.setState({
      cropResult: this.cropper.getCroppedCanvas().toDataURL(),
    });
  }
```

