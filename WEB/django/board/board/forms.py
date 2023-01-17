from django import forms
from .models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "content"]
        # exclude_fields = ['register_dttm']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
