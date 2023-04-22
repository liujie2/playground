import os

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import reverse, redirect


# Create your views here.
def index(request):
    return redirect('index:shop', permanent=True)


def myvariable(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


def shop(request):
    return render(request, 'index.html')


def page_not_found(request, exception):
    """全局404的配置函数"""
    return render(request, '404.html', status=404)


def page_error(request):
    """全局500的配置函数"""
    return  render(request, '500.html', status=500)

def upload(request):
    # 请求方法为POST，执行文件上传
    if request.method == "POST":
        # 获取上传的文件，如果没有，就默认为None
        myfile = request.FILES.get("myFile", None)
        if not myfile:
            return HttpResponse("no file for uploaded!")
        # 打开特定的文件进行二进制的写操作
        f = open(os.path.join("/Users/liujie/python/MyDjango/MyDjango/upload", myfile.name), 'wb+')
        # 分块写入文件
        for chunk in myfile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse("upload over!")
    else:
        # 请求方法为GET时，生成文件上传页面
        return render(request, 'upload.html')
