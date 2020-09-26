from django.forms import ModelForm
from .models import ShortUrl
from django import forms


class UrlEditForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['hash', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }, format='%Y-%m-%dT%H:%M'),
        }


class UrlCreateForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['original_url', 'expiration_date']
        widgets = {
            'original_url': forms.URLInput(attrs={
                'formnovalidate': 'formnovalidate',
            }),
            'expiration_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }, format='%Y-%m-%dT%H:%M'),
        }