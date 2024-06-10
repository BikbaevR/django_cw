from django.shortcuts import render
from .forms import MyForm, StudentForm

from .models import Student


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            student = Student(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                email=form.cleaned_data['email']
            )
            student.save()
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['age'])
            # print(form.cleaned_data['email'])

    form = MyForm()
    cntx = {
        "form": form,
    }

    return render(request, 'forms/index.html', cntx)


def student(request):
    print('asdasdas')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()

    student_form = StudentForm()

    return render(request, 'forms/student.html', {'student_form': student_form})
