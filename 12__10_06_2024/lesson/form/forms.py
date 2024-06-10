from django import forms

class MyForm(forms.Form):
    name = forms.CharField(max_length=10, label="Имя")
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(required=False, label="Почта")