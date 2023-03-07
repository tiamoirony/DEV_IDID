from django.db import models


# Create your models here.
from django.contrib.auth.models import User

# 질문 모델
# 제목(Char-200), 내용(TextField), 작성날짜, 수정날짜 - DateTimeField
class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    price = models.PositiveBigIntegerField()
    count = models.IntegerField(default=0, verbose_name="개수")