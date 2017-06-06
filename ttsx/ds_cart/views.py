from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from ds_user.user_decorator import *
from models import *


# Create your views here.

@login
def cart(request,gid,count):
    carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
    if len(carts)==0:
        cart = CartInfo()
        cart.goods_id = int(gid)
        cart.count = int(count)
        cart.user_id = request.session['user_id']
        cart.save()
    else:
        cart = carts[0]
        cart.count += count
        cart.save()
    if request.is_ajax():
        return JsonResponse({'count': CartInfo.objects.filter(user_id=request.session['user_id']).count()})

    else:
        return redirect('cart/list')

@login
def list(request):
    return HttpResponse('OK')



