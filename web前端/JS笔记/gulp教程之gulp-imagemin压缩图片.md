#### 简介： 
使用gulp-imagemin压缩图片文件（包括PNG、JPEG、GIF和SVG图片），很多人安装gulp-imagemin都会出现错误，我也查了很多资料，也不知道所以然，我的做法是出错再重新安装，如果你知道问题所在，请一定告诉我！ 
#### 1、安装nodejs/全局安装gulp/本地安装gulp/创建package.json和gulpfile.js文件 
#### 2、本地安装gulp-imagemin 

###### 2.1、安装：命令提示符执行 cnpm install gulp-imagemin –save-dev 
###### 2.2、注意：没有安装cnpm请使用 npm install gulp-imagemin –save-dev 
###### 2.3、说明：–save-dev 保存配置信息至 package.json 的 devDependencies 节点。
#### 3、配置gulpfile.js 
###### 3.1、基本使用
```
var gulp = require('gulp'),
    imagemin = require('gulp-imagemin');

gulp.task('testImagemin', function () {
    gulp.src('src/img/*.{png,jpg,gif,ico}')
        .pipe(imagemin())
        .pipe(gulp.dest('dist/img'));
});
```
###### 3.2、gulp-imagemin其他参数
```
var gulp = require('gulp'),
    imagemin = require('gulp-imagemin');

gulp.task('testImagemin', function () {
    gulp.src('src/img/*.{png,jpg,gif,ico}')
        .pipe(imagemin({
            optimizationLevel: 5, //类型：Number  默认：3  取值范围：0-7（优化等级）
            progressive: true, //类型：Boolean 默认：false 无损压缩jpg图片
            interlaced: true, //类型：Boolean 默认：false 隔行扫描gif进行渲染
            multipass: true //类型：Boolean 默认：false 多次优化svg直到完全优化
        }))
        .pipe(gulp.dest('dist/img'));
});
```
###### 3.3、深度压缩图片
```
var gulp = require('gulp'),
    imagemin = require('gulp-imagemin'),
    //确保本地已安装imagemin-pngquant [cnpm install imagemin-pngquant --save-dev]
    pngquant = require('imagemin-pngquant');

gulp.task('testImagemin', function () {
    gulp.src('src/img/*.{png,jpg,gif,ico}')
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],//不要移除svg的viewbox属性
            use: [pngquant()] //使用pngquant深度压缩png图片的imagemin插件
        }))
        .pipe(gulp.dest('dist/img'));
});
```
###### 3.4、只压缩修改的图片。
压缩图片时比较耗时，在很多情况下我们只修改了某些图片，没有必要压缩所有图片，使用”gulp-cache”只压缩修改的图片，没有修改的图片直接从缓存文件读取（C:\Users\Administrator\AppData\Local\Temp\gulp-cache）。
```
var gulp = require('gulp'),
    imagemin = require('gulp-imagemin'),
    pngquant = require('imagemin-pngquant'),
    //确保本地已安装gulp-cache [cnpm install gulp-cache --save-dev]
    cache = require('gulp-cache');

gulp.task('testImagemin', function () {
    gulp.src('src/img/*.{png,jpg,gif,ico}')
        .pipe(cache(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        })))
        .pipe(gulp.dest('dist/img'));
});
```
#### 4、执行任务 
###### 4.1、命令提示符执行：gulp testImagemin