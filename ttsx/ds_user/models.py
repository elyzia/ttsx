# coding=utf-8
from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(max_length=20) # 用户名
    upasswd = models.CharField(max_length=40) # 用户密码
    ue_mail = models.CharField(max_length=30)# 用户邮箱
    utel = models.CharField(max_length=11)# 用户电话
    rec_name = models.CharField(max_length=20, default='')  # 收件人姓名
    rec_tel = models.CharField(max_length=11,default='') # 收件人电话
    rec_add = models.CharField(max_length=255,default='') # 收件人地址
    rec_postcode = models.CharField(max_length=6,default='') # 收件人邮编
    class Meta:
        db_table = "user"



