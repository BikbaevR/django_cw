from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm Password')
    email = forms.EmailField(label='Email')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')



