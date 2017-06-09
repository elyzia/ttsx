#coding=utf-8
from django.db import models
# Create your models here.

class OrderInfo(models.Model):
    '''订单'''
    oid = models.CharField(max_length=20,primary_key=True)#编号：时间＋用户编号
    user = models.ForeignKey('ds_user.User')# 用户
    odate = models.DateTimeField(auto_now_add=True)# 日期
    oIsPay = models.BooleanField(default=False)# 是否支付
    ototal = models.DecimalField(max_digits=10,decimal_places=2)# 订单金额
    oaddress = models.CharField(max_length=255)# 收货地址


class OrderDetailInfo(models.Model):
    '''订单详细列表'''
    goods = models.ForeignKey('ds_goods.GoodsInfo')# 商品
    order = models.ForeignKey(OrderInfo)# 订单
    pirce = models.DecimalField(max_digits=5,decimal_places=2)# 价格
    count = models.IntegerField()# 数量





