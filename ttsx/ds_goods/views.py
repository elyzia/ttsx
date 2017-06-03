# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator,Page

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


def list(request,gid,gindex):
    num = request.GET.get('gnum')
    if num == '0':
        t_list = GoodsInfo.objects.filter(gtype_id=gid).order_by('-id')
    elif num == '1':
        t_list = GoodsInfo.objects.filter(gtype_id=gid).order_by('-gprice')
    else:
        t_list = GoodsInfo.objects.filter(gtype_id=gid).order_by('-gclick')
    t_new = GoodsInfo.objects.filter(gtype_id=gid).order_by('-id')[0:2]
    t_title = TypeInfo.objects.get(id=gid)
    paginator = Paginator(t_list,10)# 每页显示的数量
    page = paginator.page(gindex)# 显示第几页
    context = {'t_title':t_title,'t_new':t_new,'page':page,'gid':gid,'num':num}
    return render(request,'ds_goods/list.html',context)