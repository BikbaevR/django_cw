from django.http import HttpResponse
from django.shortcuts import render
from .middleware import my_middleware


@my_middleware('args')
def index(request):
    # return HttpResponse("Midleware")
    # print(5 / 0)
    # print(request.COOKIES)
    return render(request, 'index.html')