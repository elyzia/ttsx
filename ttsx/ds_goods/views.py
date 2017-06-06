# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator,Page

# Create your views here.
def index(request):
    click = []# 保存６个点击量排序对象
    new = []# 保存６个按照新品排序对象
    for i in range(1,7):
        # 根据分类查找，按照点击量排序，降序，返回一个t_click对象
        t_click = GoodsInfo.objects.filter(gtype_id=i).order_by('-gclick')[0:3]
        # 根据分类查找，按照新品排序，降序，返回一个t_click对象
        t_new = GoodsInfo.objects.filter(gtype_id=i).order_by('-id')[0:4]
        click.append(t_click)
        new.append(t_new)
    context = {'t1_click':click[0],'t1_new':new[0],
               't2_click':click[1],'t2_new':new[1],
               't3_click':click[2],'t3_new':new[2],
               't4_click':click[3],'t4_new':new[3],
               't5_click':click[4],'t5_new':new[4],
               't6_click':click[5],'t6_new':new[5]
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
    page = paginator.page(gindex)# 显示第几页内容，创建一个ｐａｇｅ对象
    context = {'t_title':t_title,'t_new':t_new,'page':page,'gid':gid,'num':num}
    return render(request,'ds_goods/list.html',context)


def detail(request,gid):
    t_goods = GoodsInfo.objects.get(id=gid)# 根据id查找，返回一个GoodsInfo对象
    t_type = TypeInfo.objects.get(id=t_goods.gtype_id)# 根据分类查找，返回一个TypeInfo对象
    t_new = GoodsInfo.objects.filter(gtype_id=t_goods.gtype_id).order_by('-id')[0:2]# 根据分类查找，按照新品排序，返回一个对象
    t_goods.gclick = t_goods.gclick + 1
    t_goods.save()
    context = {'t_goods':t_goods,'t_type':t_type,'t_new':t_new}
    response = render(request,'ds_goods/detail.html',context)
    # 最近浏览
    liulan = request.COOKIES.get('liulan','')
    if liulan == '':
        response.set_cookie('liulan',gid)
    else:
        liulan_list = liulan.split(',')
        if gid in liulan_list:
            liulan_list.remove(gid)
        liulan_list.insert(0,gid)
        if len(liulan_list) > 5:
            liulan_list.pop()
        liulan2 = ','.join(liulan_list)
        response.set_cookie('liulan',liulan2)
    return response


from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        extra = super(MySearchView, self).extra_context()
        extra['title']=self.request.GET.get('q')
        return extra