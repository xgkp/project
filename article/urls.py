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
]