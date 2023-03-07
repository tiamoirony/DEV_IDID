from django import forms
from .models import Item


class OrderForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['count']
 