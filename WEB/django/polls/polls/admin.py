from django.contrib import admin
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

# admin.StackedInline : 아래로 쌓는 방식
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 필드의 순서, 사용할 필드
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]


admin.site.register(Question, QuestionAdmin)
