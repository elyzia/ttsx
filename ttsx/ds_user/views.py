# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,JsonResponse,HttpResponseRedirect
from models import *
from hashlib import sha1
from . import user_decorator
from ds_goods.models import *
# Create your views here.


def register(request):
    return render(request,'ds_user/register.html')# 显示注册页

def register_handle(request):
    # 注册提交处理页面
    post = request.POST # 创建一个post对象
    uname = post.get('user_name')# 获取提交的名字属性
    upwd = post.get('pwd') #　获取提交的密码
    ucpwd = post.get('cpwd')# 获取提交的二次密码
    uemail = post.get('email')# 获取注册的邮箱

    s1 = sha1()# 创建一个sha1对象
    s1.update(upwd)# 将密码加密
    upwd2 = s1.hexdigest()# 获取加密后的密码
    user = User()# 创建一个ｕser对象
    user.uname = uname# 添加name属性
    user.upasswd = upwd2# 添加密码属性
    user.ue_mail = uemail# 添加邮箱属性
    user.save()# 将数据保存添加
    return redirect('/login/')# 注册成功跳转到登陆页

def register_exist(request):# 进行注册验证
    uname = request.GET.get('uname')# 获取用户输入的name
    count = User.objects.filter(uname=uname).count()# 在数据库查找获取到的名字个数
    return JsonResponse({'count':count})# 返回一个ｊｓｏｎ对象


def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'uname':uname,'error_name':0,'error_pwd':0}
    return render(request,'ds_user/login.html',context)

def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu',0)

    users = User.objects.filter(uname=uname)

    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].upasswd:
            url = request.COOKIES.get('ulr','/')
            red = HttpResponseRedirect(url)
            red.set_cookie('url','',max_age=-1)
            if jizhu != 0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            request.session.set_expiry(0)
            return red
        else:
            context = {'uname': uname, 'error_name': 0, 'error_pwd': 1}
            return render(request,'ds_user/login.html',context)
    else:
        context = {'uname': uname, 'error_name': 1, 'error_pwd': 0}
        return render(request, 'ds_user/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')

@user_decorator.login
def user_center_info(request):
    user = User.objects.get(id=request.session.get('user_id',''))
    goods_list = []
    goods_ids = request.COOKIES.get('liulan','')
    #最近浏览
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        for goods_ids in goods_ids1:
            goods_list.append(GoodsInfo.objects.get(id = int(goods_ids)))

    tel = user.utel
    if tel == '':
        tel = "无"
        context = {'uname':user.uname,'utel':tel,'uemail':user.ue_mail,'goods_list':goods_list}
    return render(request,'ds_user/user_center_info.html',context)

@user_decorator.login
def user_center_order(request):
    return render(request,'ds_user/user_center_order.html')

@user_decorator.login
def user_center_site(request):
    user = User.objects.get(id=request.session.get('user_id',''))
    if request.method == 'POST':
        post = request.POST
        user.rec_name = post.get('rec_name')
        user.rec_tel = post.get('rec_tel')
        user.rec_add = post.get('rec_add')
        user.rec_postcode = post.get('rec_postcode')
        user.save()
    return render(request,'ds_user/user_center_site.html',{'user':user})

