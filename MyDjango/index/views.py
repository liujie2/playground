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