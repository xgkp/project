"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse
from book import views

# def index(request):
#     return HttpResponse("welcome to first project");
    

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("s",index)
    # http://127.0.0.1:8000/book?id=3&name=666
    path('book',views.get_book_query_string),
    # http://127.0.0.1:8000/book/1
    path('book/<int:book_id>',views.get_book_query_int),
    # 字符串可传空格
    path('book/str/<str:book_id>',views.get_book_query_str),
    # slug可传-——
    path('book/slug/<slug:book_id>',views.get_book_query_slug,name='book_slug'),
    # path可传//
    path('book/path/<path:book_id>',views.get_book_query_path,name='book_path'),

    path('movie/', include("movie.urls"))
]
