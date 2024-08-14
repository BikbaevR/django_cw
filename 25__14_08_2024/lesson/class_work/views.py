from django.http import HttpResponse
from .middleware import is_authenticated


@is_authenticated
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
