# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,JsonResponse,HttpResponseRedirect
from models import *
from hashlib import sha1
from . import user_decorator

# Create your views here.

def index(request):
    return render(request,'ds_user/index.html')

def register(request):
    return render(request,'ds_user/register.html')

def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    s1 = sha1()
    s1.update(upwd)
    upwd2 = s1.hexdigest()
    user = User()
    user.uname = uname
    user.upasswd = upwd2
    user.ue_mail = uemail
    print 1
    user.save()
    print 2
    return redirect('/login/')

def register_exist(request):
    uname = request.GET.get('uname')
    count = User.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})


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
    tel = user.utel
    if tel == '':
        tel = "无"
        context = {'uname':user.uname,'utel':tel,'uemail':user.ue_mail}
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

