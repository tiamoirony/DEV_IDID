from django.db import models
from django.conf import settings

# Create your models here.

# Shop (배달가게)
# Item (상품) : 가게 별로 취급하는 상품목록
# 한 상품은 한 가게에만 귀속됩니다. 한 상품이 다수 가게에 귀속될 수 없습니다.
# Order (유저 주문)
# 유저는 한 가게에 방문하여, 하나의 주문에서 다수의 상품을 구매할 수 있습니다.
# 각 상품은 한 주문 내에서 1개씩 구매함을 가정합니다.
# 생성된 주문은 수정할 수 없습니다. 즉 수정기능은 구현하지 않아도 됩니다.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)

    def __str__(self): 
        return self.name


class Item(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_set = models.ManyToManyField(Item)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.price for item in self.item_set.all())
