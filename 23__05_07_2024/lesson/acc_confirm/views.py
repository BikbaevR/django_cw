from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegisterForm, SignInForm


def register(request):
    regForm = RegisterForm()
    if request.method == 'POST':
        regForm = RegisterForm(request.POST)
        if regForm.is_valid():
            regForm.save()

    context = {'regForm': regForm}
    return render(request, 'acc/index.html', context)


def signIn(request):
    signInForm = SignInForm()
    print('asdasdasds')
    print(signInForm)
    if request.method == 'POST':
        signInForm = SignInForm(request.POST)
        if signInForm.is_valid():
            username = signInForm.cleaned_data['username']
            password = signInForm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('')

    context = {'signInForm': signInForm}
    return render(request, 'acc/sign.html', context)
