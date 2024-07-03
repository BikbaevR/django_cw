from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'headHunter/index.html')


# @login_required(login_url='login')
def profile_view(request):
    ctx = {
        'resume_list': request.user.resumes.all(),
        'request_list': Request.objects.filter(resume__user=request.user).all(),
       }
    return render(request, 'headHunter/profile.html', ctx)
