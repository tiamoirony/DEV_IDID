from django.db import models
from user.models import User

from taggit.managers import TaggableManager

# Create your models here.
# 글 등록, 수정, 삭제, 조회 
#
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='작성자')
    title = models.CharField(verbose_name='제목', max_length=255, blank=False)
    content = models.TextField(verbose_name='네용')
    image = models.ImageField(blank=True, null=True, verbose_name='이미지')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='작성날짜') # 글이 처음 등록 될때 자동으로 입력
    modified_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜') # 글을 수정할 때마다 자동으로 입력 
    likes = models.ManyToManyField(User, related_name='likes',blank=True)
    tags =  TaggableManager()
    
    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='작성자')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,verbose_name='원본글')
    content = models.TextField(verbose_name='네용')
    image = models.ImageField(blank=True, null=True, verbose_name='이미지')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='작성날짜')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='수정날짜')
    
    def __str__(self) -> str:
        return '%s-%s' % (self.id, self.user)