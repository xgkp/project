from django.urls import path
from . import views 

app_name = 'newbook'

urlpatterns = [
   path('nb',views.newbook,name='newbook_view'),
] 