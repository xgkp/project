from datetime import datetime, timedelta
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

def filterview(request):
    context = {
        'msg':'  hello Django template filter  ',
        'date': datetime.now(),
        'date2': datetime.now() + timedelta(days=5),
        'profile':'wo jiu shi wo bu yi yang de yan huo',
        'profile1':'',
        'list':[1,2,3,4,5],
        'num':69.34567,
        'safe':'<h1>我是安全的html代码</h1>',
        'stringtags':'<strong>hello world django template filter</strong>',
        'truncate':'Django模板语言提供了丰富的过滤器，可以对变量进行各种处理，比如字符串的截断、大小写转换、日期格式化等。',
        'truncate_html':'Django模板语言提供了<b>丰富的过滤器</b>，可以对变量进行各种处理，比如字符串的截断、大小写转换、日期格式化等。',
        }
    return render(request=request,template_name='filter.html',context=context)
    
def xfzindex(request):  
    articles = [
        {"title":"文章1","content":"这是文章1的内容"},
        {"title":"文章2","content":"这是文章2的内容"},
        {"title":"文章3","content":"这是文章3的内容"},
    ]
    return render(request=request,template_name='xfz_index.html',context={"articles":articles})

def xfzindex2(request):
    return render(request=request,template_name='xfz_index2.html')
    
    
    
    