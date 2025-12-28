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
    
def ifview(request, age):
    print(age)
    return render(request=request,template_name='if.html',context={'age':age})

def forview(request):
    books = [
            {"bookname":"shuihuzhuan","author":"施耐庵"},
            {"bookname":"xiyouji","author":"wuchengen"}
        ]
    books2 = []
    context = {
        "books":books,
        "person":{
            "name":"zhangsan",
            "age":18,
            "height":180
        },
        "books2":books2
        }
    # list
    # items,keys,values
    return render(request=request,template_name='for.html',context=context)

def withview(request):
    books = [
            {"bookname":"shuihuzhuan","author":"施耐庵"},
            {"bookname":"xiyouji","author":"wuchengen"}
    ]
    context = {
        "books":books
    }
    # {% with bk1=books.1 %}
    # {% with books.1 as bk1 %}
    return render(request=request,template_name='with.html',context=context)
    
def urlview(request):
    return render(request=request,template_name='url.html')
    



    
    
    