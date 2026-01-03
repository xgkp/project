from django.shortcuts import render,HttpResponse
from .models import book,bookoder
from django.db.models import Avg, Count, F, Q,Sum,Max,Min

# Create your views here.


def addbook(request):
    book1 = book(title='Django入门', author='张三', published_date='2024-01-15', price=50)
    book2 = book(title='Python高级编程', author='李四', published_date='2024-02-20', price=60)
    book3 = book(title='数据科学基础', author='王五', published_date='2024-03-10', price=70)
    book1.save()
    book2.save()
    book3.save()

    order1 = bookoder(book=book1, sale_price=45)
    order2 = bookoder(book=book2, sale_price=55)
    order3 = bookoder(book=book3, sale_price=65)
    order4 = bookoder(book=book1, sale_price=40)
    order5 = bookoder(book=book2, sale_price=50)
    order1.save()
    order2.save()
    order3.save()
    order4.save()
    order5.save()
    return HttpResponse("添加图书 和订单成功")

def avg(request):
    avg_price = bookoder.objects.aggregate(Avg('sale_price'))
    return HttpResponse(f"订单的平均销售价格是: {avg_price['sale_price__avg']}")

def annotate(request):
    title_total = book.objects.annotate(total=Sum('bookoder__sale_price')).values('title', 'total')
    for item in title_total:
        print(f"书名: {item['title']}, 订单总销售价格: {item['total']}")
    return HttpResponse("每本书的订单总销售价格已打印在控制台")



def count(request):
    # book_count = book.objects.count()
    # book_count = count['total']
    count = book.objects.aggregate(total=Count('id'))
    print(f"图书总数是: {count['total']}")
    return HttpResponse(f"图书总数是: {count['total']}")

def maxandmin(request):
    result = book.objects.aggregate(max_price=Max('price'), min_price=Min('price'))
    print(f"图书的最高价格是: {result['max_price']}, 最低价格是: {result['min_price']}")
    max_price = book.objects.aggregate(max_price=Max('price'))
    min_price = book.objects.aggregate(min_price=Min('price'))
    return HttpResponse(f"图书的最高价格是: {max_price['max_price']}, 最低价格是: {min_price['min_price']}")
    
    
        
