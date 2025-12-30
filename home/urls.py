from django.urls import path
from . import views 
app_name = 'home'

urlpatterns = [
    path('index',views.index,name='home_index'),
    path('bd',views.bd,name='home_bd'),
    path('info',views.info,name='home_info'),
    path('if/<int:age>',views.ifview,name='if_view'),
    path('for',views.forview,name='for_view'),
    path('with',views.withview,name='with_view'),
    path('url',views.urlview,name='url_view'),
    path('filter',views.filterview,name='filter_view'),
    path('xfzindex',views.xfzindex,name='xfz_index'),
    path('xfzindex2',views.xfzindex2,name='xfz_index2'),
]