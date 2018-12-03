## word-wrap、white-space和word break的区别

#### word-wrap语法：
##### word-wrap ： normal | break-word
    normal ： 默认值，单词如果单词超长，会冲出边界（单个单词超长，在当前行显示）
    break-word ： 将内容在边界内换行，当单词在当前行放不下时，会自动切换到下一行（单个单词超长，在下一行显示）

#### word-break语法：
##### word-break:normal | break-all | keep-all
    normal：如果设置为默认值时中文则到边界处的汉字换行，如果是英文整个单词换行，如果出现某个单词长度过长，则会撑破容器，如果边框为固定属性，则后面部分将无法显示；（单个单词长度超过容器长度）
    break-all：可以强行截断英文单词，强行换行
    keep-all：不允许字断开。如果是中文将把前后标点符号内的一个汉字短语整个换行，英文单词也整个换行，如果出现某个英文字符长度超过边界，则后面的部分将撑破容器，如果边框为固定属性，则后面部分无法显示

#### white-space语法：（浏览器处理折行时的空白符）
##### white-space：normal | nowrap | pre-wrap | pre-line | inherit
    normal：默认，浏览器忽略空白符
    nowrap：文本不会换行，文本会在在同一行上继续，直到遇到 <br> 标签为止。
    pre-wrap：保留空白符，但是正常地进行换行。
    pre-line：合并空白符，但是保留换行符。
    inherit：继承父元素的设置

##### 最好的处理方式是：（单词折行，超出隐藏）
    word-wrap:break-word;
    overflow:hidden;
