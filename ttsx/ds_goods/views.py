# coding=utf-8
from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    t1_click = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
    t1_new = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
    t2_click = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[0:3]
    t2_new = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[0:4]
    t3_click = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:3]
    t3_new = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
    t4_click = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
    t4_new = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    t5_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
    t5_new = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
    t6_click = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[0:3]
    t6_new = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]
    context = {'t1_click':t1_click,'t1_new':t1_new,'t2_click':t2_click,'t2_new':t2_new,
               't3_click':t3_click,'t3_new':t3_new,'t4_click':t4_click,'t4_new':t4_new,
               't5_click':t5_click,'t5_new':t5_new,'t6_click':t6_click,'t6_new':t6_new
            }
    return render(request,'ds_goods/index.html',context) # 显示主页
