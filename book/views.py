from django.shortcuts import render, HttpResponse

# Create your views here.
def get_book_query_string(request):
    # book_id = request.GET['id']
    book_id = request.GET.get('id')
    name = request.GET.get('name')
    return HttpResponse(f"您查询的图书ID是:{book_id} 图书名称是:{name}")

def get_book_query_int(request, book_id):
    return HttpResponse(f"您查询的图书ID是:{book_id}")

def get_book_query_str(request, book_id):
    return HttpResponse(f"您查询的图书ID是:{book_id}")

def get_book_query_slug(request, book_id):
    return HttpResponse(f"您查询的图书ID是:{book_id}")

def get_book_query_path(request, book_id):
    return HttpResponse(f"您查询的图书ID是:{book_id}")