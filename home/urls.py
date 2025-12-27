from django.urls import path
from . import views 
app_name = 'home'

urlpatterns = [
    path('index',views.index,name='home_index'),
    path('bd',views.bd,name='home_bd'),
    path('info',views.info,name='home_info')
]