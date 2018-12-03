### json、jq实现三级联动选择框方法一：

**html代码：**

```
    <select id="level1Class" class="column-select" name="level1Class">
        <option value="0">请选择栏目</option>
    </select>
    <select id="level2Class" class="column-select" name="level1Class">
        <option value="0">请选择栏目</option>
    </select>
    <select id="level3Class" class="column-select" name="level1Class">
        <option value="0">请选择栏目</option>
    </select>
```

**json数据：**

```js
    var fir_class = [{firId: 1,firName:"母婴儿童"},{firId: 2,firName:"美容彩妆"},{firId: 3,firName:"营养保健"}];
    var sec_class = [{secId: 1,secName:"奶粉",firId: 1},{secId: 2,secName:"营养辅食",firId: 1},
                        {secId: 3,secName:"面部护理",firId: 2},{secId: 4,secName:"男士护理",firId: 2},
                        {secId: 5,secName:"维生素",firId: 3},{secId: 6,secName:"胶囊",firId: 3}];
    var thi_class = [{thiID: 1,thiName:"品牌奶粉",secId: 1},{thiID: 2,thiName:"妈妈奶粉",secId: 1},
                        {thiID: 3,thiName:"粥/面条",secId: 2},
                        {thiID: 4,thiName:"洗面奶",secId: 3},
                        {thiID: 5,thiName:"男士洗面奶",secId: 4},
                        {thiID: 6,thiName:"维生素A",secId: 5},
                        {thiID: 7,thiName:"β胶囊",secId: 6}];
```

**js代码：**

```js
	classColunm();
    function classColunm() {
        $.each(fir_class, function (k, p) {
            var option = "<option value='" + p.firId + "'>" + p.firName + "</option>";
            $("#level1Class").append(option);
        });

        $("#level1Class").change(function () {
            var selValue = $(this).val();
            $("#level2Class option:gt(0)").remove();//gt(0)前1个元素后的所有元素

            $.each(sec_class, function (k, p) {
                if (p.firId == selValue) {
                    var option = "<option value='" + p.secId + "'>" + p.secName + "</option>";
                    $("#level2Class").append(option);
                }
            });
        });
        $("#level2Class").change(function () {
            var selValue = $(this).val();
            $("#level3Class option:gt(0)").remove();

            $.each(thi_class, function (k, p) {
                if (p.secId == selValue) {
                    var option = "<option value='" + p.Id + "'>" + p.thiName + "</option>";
                    $("#level3Class").append(option);
                }
            });
        });
        $("#level1Class").change(function () {
            $("#level3Class option:gt(0)").remove();
        });

    }
```

##### 思路：
先用jq遍历第一个json数据后放入第一个选择框中，将json定义的id值赋给option的value。当第一个选择框发生改变后触发后面的事件，如果第二个json数据中所对应的第一个josn的ID值等于它选择框的value值，那么在把第二个接送数据放入第二个下拉框中，第三个同理。

当前面的选择框发生改变后，清除后面的选择框的内容，保留第一个。

>$("#level3Class option:gt(0)").remove();

这句意思是移除下拉框中的内容，只保留第一个。gt(0)意思就是：大于0
