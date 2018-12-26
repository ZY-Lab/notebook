##React Native 使用Chrome调试

谷歌 Chrome 开发工具，是基于谷歌浏览器内含的一套网页制作和调试工具。开发者工具允许网页开发者深入浏览器和网页应用程序的内部。该工具可以有效地追踪布局问题，设置 JavaScript 断点并可深入理解代码的最优化策略。 Chrome 开发工具一共提供了8大组工具：

•Element 面板： 用于查看和编辑当前页面中的 HTML 和 CSS 元素。

•Network 面板：用于查看 HTTP 请求的详细信息，如请求头、响应头及返回内容等。

•Source 面板：用于查看和调试当前页面所加载的脚本的源文件。

•TimeLine 面板： 用于查看脚本的执行时间、页面元素渲染时间等信息。

•Profiles 面板：用于查看 CPU 执行时间与内存占用等信息。

•Resource 面板：用于查看当前页面所请求的资源文件，如 HTML，CSS 样式文件等。

•Audits 面板：用于优化前端页面，加速网页加载速度等。

•Console 面板：用于显示脚本中所输出的调试信息，或运行测试脚本等。

提示：对于调试React Native应用来说，Sources和Console是使用频率很高的两个工具。

####如何通过 Chrome调试React Native程序

第一步：启动远程调试

在Developer Menu下单击”Debug JS Remotely” 启动JS远程调试功能。此时Chrome会被打开，同时会创建一个“http://localhost:8081/debugger-ui.” Tab页。

第二步：打开Chrome开发者工具

在该“http://localhost:8081/debugger-ui.”Tab页下打开开发者工具。打开Chrome菜单->选择更多工具->选择开发者工具。你也可以通过快捷键(Command⌘ + Option⌥ + I on Mac, Ctrl + Shift + I on Windows)打开开发者工具。

####巧用Sources面板

![](https://i.imgur.com/JqOw1it.jpg)

Sources 面板可以让你看到你所要检查的页面的所有脚本代码，并在面板选择栏下方提供了一组标准控件，提供了暂停，恢复，步进等功能。在窗口的最下方的按钮可以在遇到异常(exception)时强制暂停。源码显示在单独的标签页，通过点击 打开文件导航面板，导航栏中会显示所有已打开的脚本文件。

心得：Chrome开发着工具中的Sources面板几乎是我最常用的功能面板。通常只要是开发遇到了js报错或者其他代码问题，在审视一遍自己的代码而一无所获之后，我首先就会打开Sources进行js断点调试。



