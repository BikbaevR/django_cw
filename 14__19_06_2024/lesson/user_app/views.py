from django.shortcuts import render, redirect
from .form import UserAuthForm, SignInForm
from django.contrib.auth import login, authenticate, logout


def register(request):
    if request.method == 'POST':
        reg_form = UserAuthForm(request.POST)
        print("""1""")
        if reg_form.is_valid():
            print("""2""")
            user = reg_form.save()
            login(request, user)
            return redirect('profile')

    register_form = UserAuthForm()
    context = {'register_form': register_form}
    return render(request, 'user_app/register.html', context)



def login_view(request):
    if request.method == 'POST':
        fw = SignInForm(request.POST)
        print('login 1')
        if fw.is_valid():
            print('login 2')
            username = fw.cleaned_data['username']
            password = fw.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')

    login_form = SignInForm()
    context = {'login_form': login_form}
    return render(request, 'user_app/login.html', context)


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    ctx = {'user': request.user}
    return render(request, 'user_app/profile.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('login')