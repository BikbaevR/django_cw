from django import forms
from .models import *


class PostForm(forms.ModelForm):
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if title in ['slovo', 'plohoe']:
    #         raise forms.ValidationError(message='Заголовок неправильный')
    #     return title

    # def save(self, commit=True):
    #     title = self.cleaned_data['title']
    #     content = self.cleaned_data['content']
    #
    #     if title in ['slovo', 'plohoe']:
    #         raise forms.ValidationError(message='Заголовок неправильный')
    #
    #     super(PostForm, self).save(commit=commit)

    class Meta:
        model = Post
        fields = '__all__'


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
