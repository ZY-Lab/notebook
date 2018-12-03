##Django模版获取当前页面url

使用{{ request.get_full_path }}或者{{ request.path }}，取决于你是想输出全路径还是相对路径。
检查在settings.py里，'django.core.context_processors.request'，
是否已经被加到TEMPLATE_CONTEXT_PROCESSORS里