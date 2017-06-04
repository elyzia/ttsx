# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class TypeInfo(models.Model):
    ttitel = models.CharField(max_length=20)# 分类名称
    isDelete = models.BooleanField(default=False)# 物理删除

    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)# 商品名称
    gpic = models.ImageField(upload_to='goods')# 商品图片
    gprice = models.DecimalField(max_digits=5,decimal_places=2)# 商品单价
    isDelete = models.BooleanField(default=False)# 商品物理删除
    gunit = models.CharField(max_length=20,default='500g')# 商品单位
    gclick = models.IntegerField()# 商品点击量，人气
    gjianjie = models.CharField(max_length=255)# 商品简介
    gkucun = models.IntegerField()# 商品库存量
    gcontent = HTMLField()# 商品详请
    gtype = models.ForeignKey(TypeInfo)# 自关联

    def __str__(self):
        return self.gtitle.encode('utf-8')