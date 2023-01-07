
from django import forms
from .models import Photo # 현재 경로의 model.py 모둘에 있는 Photo 클래스 import 

# 클래스는 대문자로 시작
# 두개의 단어가 연결되는 이름 지정 : 카멜케이스 



class PhotoForm(forms.ModelForm):
    # 내부클래스 반드시 필요 mete 모델과 연동되는 모델은 만든다 
    class Meta:
        model = Photo
        # 모델 에서 사용할 필드들을 나열 튜플, 리스트
        fields = ['title','author','image', 'description','price']
        
        
        