from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import NewBook,Tag
# Create your views here.

def newbook(request):
    # 获取游标对象
    cursor = connection.cursor()
    # 执行SQL语句
    cursor.execute("SELECT * FROM book_back")
    # 获取所有数据
    books = cursor.fetchall()

    # one = cursor.fetchone()

    context = {
        'books': books,
    }
    print(books)
    for book in books:
        print(book)
    return render(request=request,template_name='newbook.html', context=context)
    
def addnewbook(request):
    # book = NewBook(name='西游记', author='吴承恩', price=29.8)    
    book = NewBook(name='三国演义', author='吴承恩2', price=99.9)    
    book.save()
    return HttpResponse(f"已添加新书成功：{book.name} 作者：{book.author} 价格：{book.price}")  

def querynewbookall(request):
    books = NewBook.objects.all()
    for book in books:
        print(f"书名：{book.name} 作者：{book.author} 价格：{book.price}")
    return HttpResponse(f"查询所有新书成功，数量：{books.count()}")


def filter(request):
    # 可以多个条件,逗号隔开
    books = NewBook.objects.filter(name='西游记')
    for book in books:
        print(f"书名：{book.name} 作者：{book.author} 价格：{book.price}")
    return HttpResponse(f"过滤新书成功，数量：{books.count()}")


def get(request):
        # 可以多个条件,逗号隔开
    try:
        book = NewBook.objects.get(name='不存在的书名')
    except NewBook.DoesNotExist:
        return HttpResponse("没有找到对应的书籍")
        # book = NewBook.objects.get(id=1)
        print(f"书名：{book.name} 作者：{book.author} 价格：{book.price}")
        return HttpResponse(f"获取唯一，数量：{book.id}")

def order(request):
    books = NewBook.objects.all().order_by('published_date')
    for book in books:
        print(f"书名：{book.name} 作者：{book.author} 价格：{book.price}")
    return HttpResponse(f"排序新书成功，数量：{books.count()}")

def update(request):
    book = NewBook.objects.get(id=1)
    book.price = 39.9
    book.save()
    return HttpResponse(f"更新新书成功：{book.name} 价格：{book.price}")
    
def delete(request):
    book = NewBook.objects.get(price=99.9)
    book.delete()
    return HttpResponse(f"删除新书成功：{book.name}")

def tag(request):
    tag = Tag(name='历史')
    tag.save()
    return HttpResponse(f"添加标签成功：{tag.name}")
    
    