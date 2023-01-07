# 장고 폼
# 	1) 폼 생성에 필요한 데이터를 폼 클래스로 구조화
# 	2) 폼 클래스의 데이터를 렌더링하여 HTML 폼 작성
# 	3) 사용자로부터 제출된 폼과 데이터를 수신하고 처리

# 바인딩 폼 - 아래 코드처럼 데이터와 폼이 연결된 상태
# form = NameForm(request.POST)

from django import forms
from .models import Musician


class NameForm(forms.Form):
    '''
    일반 폼
    '''
    # input type='text' 생성
    name = forms.CharField(max_length=20, label='Your Name')
    
    
    # 추가 검증 시 메소드의 이름은 clean 이 들어가도록 해야 함 관례?
    # def clean(self):
    #     cleaned_data = super().clean()
        
    #     name = cleaned_data['name']
        
    #     if name != '홍길동':
    #         raise forms.ValidationError('이름을 확인해 주세요')
        
    
    # clean_요소명(필드명)
    def clean_name(self):
        cleaned_data = super().clean()
        
        name = cleaned_data['name']
        
        if name != '홍길동':
            raise forms.ValidationError('이름을 확인해 주세요')
        
        

class MusicianForm(forms.ModelForm):
    '''
    모델 폼
    '''
    class Meta:
        model = Musician
        fields = '__all__' # fields = [필요한 필드] or (필요한 필드)
        # exclude = ['제외할 필드']