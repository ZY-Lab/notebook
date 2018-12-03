##django 打印快递面单##
####一、单独打印快递面单####
######1、html页面js调起打印功能######

	<script type="text/javascript">
        function CloseAfterPrint() {
            if (tata = document.execCommand("print")) {
                window.close();
            }
            else setTimeout("CloseAfterPrint();", 1000);
        }
        window.onload = function () {
            CloseAfterPrint();
            window.print();
        };
    </script>
####二、批量打印快递面单####
######1、获取多个面单页面代码######
选择print下的much_print_shunfeng_model.html页面，使用render_to_string渲染页面会返回整个页面的代码，前台上传所有订单的订单号，循环渲染所选订单的页面代码，一个data就是一个面带页面的代码，其中重复的代码可以拿出来，放到指定模板上
	
    order_list = request.POST.getlist('order_list[]')
    all_data = ""
    for i in order_list:
            order = get_object_or_404(Order, pk=i)
	        data = render_to_string('print/much_print_shunfeng_model.html', {
                        'order': order,
                        'print_date': print_date,
                        'print_time': print_time,
                        'mail_no_type': mail_no_type
                    })
                    all_data = data + all_data
######2、渲染到指定模板######
render_to_string返回的是safestring格式代码，与string类型相加后会变成string类型，转换成safestring类型渲染到页面，页面上会识别html代码

	return render(request, 'print/much_express_print_list.html', {'order': SafeString(all_data)})      
######3、注意######    
前台向后台传输的所有订单的订单号时，不要用get传，使用post请求