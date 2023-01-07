from django.contrib import admin
from .models import Todo

# 모델을 어드민 사이트에서 관리 할수 잇게 
admin.site.register(Todo)
