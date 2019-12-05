from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.goods_list, name = 'goods_list')
]