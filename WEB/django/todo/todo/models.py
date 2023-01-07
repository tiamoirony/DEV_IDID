from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    
    
    # 오브젝트 대신 타이틀로 목록 만들기 
    def __str__(self) -> str:
        return self.title
    
