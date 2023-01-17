from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="종류")
    name = models.CharField(max_length=200, verbose_name="이름")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    price = models.PositiveBigIntegerField(verbose_name="가격")
    count = models.IntegerField(default=0, verbose_name="개수") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성날짜")
    

    def __str__(self):
        return self.name # 어드민 위치에 이름 으로 보여주는것