from django import forms

from post.models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title', 'image'
