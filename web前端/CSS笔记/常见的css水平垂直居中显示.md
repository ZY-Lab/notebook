## 常见的CSS水平垂直居中设置  

**让内容上下居中在布局时是经常写的，下面写了常见的4中上下居中方式，复制代码查看效果**  

#### css代码  
```  
<style>
    *{
        margin: 0;
        padding: 0;
    }
    body{
        padding:10px 50px;
    }
    .parent{
        width: 400px;
        height: 200px;
        background: #b99eff;
    }
    .child{
        width: 150px;
        height: 100px;
        background: #db6867;
    }

    /*flex水平居中和垂直居中*/
    .flex-parent{
        display: flex;  /* 给父元素设值*/
        justify-content: center; /* 水平居中 */
        align-items: center; /*垂直居中*/
    }
    .flex-child{

    }

    /*table水平垂直居中*/
    .table-parent{
        display: table-cell;
        text-align: center;  /*水平居中*/
        vertical-align: middle; /*垂直居中*/
    }
    .table-child{
        display: inline-block;
    }

    /*absolute+transform 水平垂直居中*/
    .transform-parent{
        position: relative;
    }
    .transform-child{
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    /*绝对定位方式+四个方向置0*/
    .position-parent{
        position:relative
    }
    .position-child{
        margin:auto;
        height: 100px;
        width: 100px;
        position: absolute;
        top: 0; left: 0; bottom: 0; right: 0;
    }

</style>
```  

#### html代码  
```  
    <h3>flex水平居中和垂直居中</h3>
    <div class="parent flex-parent">
        <div class="child flex-child">缺点：有兼容性问题</div>
    </div>

    <br><hr><br>

    <h3>table水平垂直居中</h3>
    <div class="parent table-parent">
        <div class="child table-child"></div>
    </div>

    <br><hr><br>

    <h3>absolute+transform 水平垂直居中</h3>
    <div class="parent transform-parent">
        <div class="child transform-child"></div>
    </div>

    <br><hr><br>

    <h3>绝对定位方式+四个方向置0</h3>
    <div class="parent position-parent">
        <div class="child position-child"></div>
    </div>
```  

> 以上四种上下居中方式，向父级元素里面添加元素时布局发生的改变会不一样，修改代码即可发现

