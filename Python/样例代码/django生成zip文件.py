# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 14:39
# @Author  : Wall_js
# @File    : 生成zip文件夹下载
# @Company : ZY
import datetime
import zipfile
import tempfile
from django.utils import timezone
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse


def download_message(self, request, queryset):
    filename = timezone.localtime(timezone.now()).strftime('%Y%m%d%H%M%S') + '.zip'
    temp = tempfile.TemporaryFile()
    archive = zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED)
    for obj in queryset:
        name = obj.MESSAGE_ID + '.xml'
        archive.writestr(name, obj.data)
        obj.status = '已下载'
        obj.is_active = False
        obj.save()
    archive.close()
    wrapper = FileWrapper(temp)
    response = StreamingHttpResponse(wrapper)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename=' + filename
    response['Content-Length'] = temp.tell()
    temp.seek(0)
    return response
