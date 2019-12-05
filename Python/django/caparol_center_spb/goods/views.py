from django.shortcuts import render
from .models import Good

def goods_list(request):
    all_goods = Good.objects.all()
    return render(request, 'goods/goods_list.html', {'all_goods':all_goods})
