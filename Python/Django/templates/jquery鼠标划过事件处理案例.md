##jquery鼠标划过事件处理案例
```
    $($('nav ul li.dropdown').mouseover(function () {
        $(this).addClass("open");  //鼠标滑过回调增加class
        $(this).mouseout(function () {
            $(this).removeClass("open");//鼠标移出回调溢出class
        })
    }))
```
