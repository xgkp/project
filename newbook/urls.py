from django.urls import path
from . import views 

app_name = 'newbook'

urlpatterns = [
   path('nb',views.newbook,name='newbook_view'),
   path('add',views.addnewbook,name='add_newbook'),
   path('queryall',views.querynewbookall,name='query_newbook_all'),
   path('filter',views.filter,name='filter_newbook'),
   path('get',views.get,name='get_newbook'),
   path('order',views.order,name='order_newbook'),
   path('update',views.update,name='update_newbook'),
   path('delete',views.delete,name='delete_newbook'),
   path('tag',views.tag,name='tag_newbook'),
] 