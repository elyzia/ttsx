from django.shortcuts import render,redirect
from django.db import transaction
from django.http import HttpResponse
from datetime import datetime
from ds_goods.models import *
from ds_cart.models import *
from models import *
# Create your views here.


@transaction.atomic
def order(request):
    post = request.POST
    address = post.get('address')
    cart_id = post.getlist('cart_id')
    sid = transaction.savepoint()
    # try:
    order = OrderInfo()
    now = datetime.now()
    uid = request.session['user_id']
    print uid
    order.oid = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
    order.odate = now
    order.ototal = 0
    order.oaddress = address
    order.user_id = uid
    order.save()
    total = 0

    for cid in cart_id:
        cart = CartInfo.objects.get(id=cid)
        if cart.goods.gkucun >= cart.count:
            cart.goods.gkucun -= cart.count
            cart.goods.save()
            detail = OrderDetailInfo()

            detail.goods = cart.goods
            detail.order = order
            detail.pirce = cart.goods.gprice
            detail.count = cart.count
            detail.save()

            total += cart.goods.gprice*cart.count
            cart.delete()
        else:
            transaction.savepoint_rollback(sid)
            return redirect('/cart/order/')
    order.ototal = total
    order.save()
    transaction.savepoint_commit(sid)
    return redirect('/user_center_order/')

    # except:
        # transaction.savepoint_rollback(sid)
        # return redirect('/cart/order/')


