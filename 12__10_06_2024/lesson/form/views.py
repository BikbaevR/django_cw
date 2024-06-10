from django.shortcuts import render
from .forms import MyForm


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['age'])
            print(form.cleaned_data['email'])

    form = MyForm()
    cntx = {
        "form": form,
    }

    return render(request, 'forms/index.html', cntx)
