from django.urls import path
from . import views
app_name = 'front'

urlpatterns = [
    path('addbook/', views.addbook, name='add_book'),
    path('avg/', views.avg, name='average_order_price'),    
    path('annotate/', views.annotate, name='annotate_book_orders'),
    path('count/', views.count, name='count_books'),
    path('maxmin/', views.maxandmin, name='max_min_book_price'),
]