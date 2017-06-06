from django.db import models
from ds_goods.models import *
from ds_user.models import *
# Create your models here.

class CartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    user = models.ForeignKey(User)