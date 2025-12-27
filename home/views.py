from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print('home/index')
    return render(request=request,template_name='index.html')

def bd(request):
    return render(request=request,template_name='bd.html')

def info(request):
    username = '课堂'
    book = {"bookname":"shuihuzhuan","author":"施耐庵"}
    class Person:
        def  __init__(self,realname):
            self.realname = realname + "123"
    context = {
        "username":username,
        "book":book,
        "books":[
            {"bookname":"shuihuzhuan","author":"施耐庵"},
            {"bookname":"xiyouji","author":"wuchengen"}
        ],
        "person":Person("真实姓名:")
        }
    
    return render(request=request,template_name='info.html',context=context)
    
    