import string
import random

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from .forms import *
from .models import MainUser


def generate_token_string(length=20):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def check_authorised(request):
    return True if len(request.session.get('is_authorised')) > 0 else False


def authorised(request, token, user):
    # request['is_authorised'] = True
    request.session['is_authorised'] = token
    user[0].token = token
    user[0].save()


def logout(request):
    # request['is_authorised'] = True
    request.session['is_authorised'] = ''


def index(request):
    print(request.session.get('is_authorised'))
    return render(request, 'app/index.html')


def registration(request):
    registerForm = RegisterForm()
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():

            password = registerForm.cleaned_data['password']
            password2 = registerForm.cleaned_data['password2']

            if password != password2:
                return redirect('registration')

            user_exsists = MainUser.objects.filter(name=registerForm.cleaned_data['username'])

            print(user_exsists)

            if not user_exsists:
                newUser = MainUser.objects.create(
                    name=registerForm.cleaned_data['username'],
                    password=registerForm.cleaned_data['password'],
                    email=registerForm.cleaned_data['email'],
                    is_admin=False)
                newUser.save()
                return redirect('index')

    context = {'registerForm': registerForm}
    return render(request, 'app/registration.html', context)

def login(request):
    if check_authorised(request):
        raise ValidationError('You are already logged in')
        return redirect('index')
    loginForm = LoginForm()
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = MainUser.objects.filter(name=username)
            print(user)
            if user:
                if user[0].password == password:
                    authorised(request, generate_token_string(), user)
                    return redirect('index')
                else:
                    print('неверный пароль')

    context = {'loginForm': loginForm}
    return render(request, 'app/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')

# def first_page(request):
#
#     request.session['test_key'] = 'test_value'
#
#     return HttpResponse("Hello, world. You're at the first page.")
#
#
# def second_page(request):
#
#     print(request.session.get('test_key', default='default'))
#
#     return HttpResponse("Hello, world. You're at the second page.")
