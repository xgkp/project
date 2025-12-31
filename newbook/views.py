from django.shortcuts import render
from django.db import connection
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
    
