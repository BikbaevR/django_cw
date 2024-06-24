from django import forms
from .models import *


class PostForm(forms.ModelForm):

    def clean_title(self):
        title = self.cleaned_data['title']
        if title in ['slovo', 'plohoe']:
            raise forms.ValidationError(message='Заголовок неправильный')
        return title


    class Meta:
        model = Post
        fields = '__all__'
