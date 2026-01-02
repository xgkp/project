from django.urls import path 
from . import views 

app_name = 'article'

urlpatterns = [
    path('add/', views.add, name='add_article'),
    path('detail/', views.detail, name='article_detail'),
]