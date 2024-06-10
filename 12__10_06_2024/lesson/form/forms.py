from django import forms
from .models import Student


class MyForm(forms.Form):
    name = forms.CharField(max_length=10, label="Имя")
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(required=False, label="Почта")



class StudentForm(forms.ModelForm):
    required_css_class = 'form'

    name = forms.CharField(label="Имя")

    class Meta:
        model = Student
        fields = 'name', 'age', 'email'
        # fields = '__all__'
