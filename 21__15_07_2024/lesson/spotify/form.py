from django import forms
from .models import *


class AddMusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = 'name', 'file', 'image', 'album', 'genres'
