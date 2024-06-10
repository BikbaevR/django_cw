from django import forms
from .models import Student


class MyForm(forms.Form):
    name = forms.CharField(max_length=10, label="Имя")
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(required=False, label="Почта")



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = 'name', 'age', 'email'
