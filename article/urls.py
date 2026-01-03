from django.urls import path 
from . import views 

app_name = 'article'

urlpatterns = [
    path('add/', views.add, name='add_article'),
    path('detail/', views.detail, name='article_detail'),
    path('otm/', views.one_to_more, name='one_to_more'),
    path('add2/', views.adda2, name='add_article2'),
    path('dt2/', views.detaila2, name='article_detail2'),
    path('q1/', views.query1exact, name='query_1_exact'),
    path('addr/', views.addrange, name='add_range'),
    path('sr/', views.searchrange, name='search_range'),
    path('add4/', views.addtag4andart4, name='add_tag4_and_art4'),
    path('qr4/', views.querytag4andart4, name='query_tag4_and_art4'),
    path('q44/', views.query44, name='query_44'),
]