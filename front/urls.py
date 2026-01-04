from django.urls import path
from . import views
app_name = 'front'

urlpatterns = [
    path('addbook/', views.addbook, name='add_book'),
    path('avg/', views.avg, name='average_order_price'),    
    path('annotate/', views.annotate, name='annotate_book_orders'),
    path('count/', views.count, name='count_books'),
    path('maxmin/', views.maxandmin, name='max_min_book_price'),
    path('ft/', views.ftype, name='f_type_example'),
    path('ft2/', views.ftype2, name='f_type_example_2'),
    path('qt/', views.qtype, name='q_type_example'),
    path('fm/', views.form, name='message_form'),
]