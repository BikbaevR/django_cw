from django import forms

class MyForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()