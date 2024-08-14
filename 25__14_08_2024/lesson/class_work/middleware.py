from django.http import HttpResponse
from django.shortcuts import redirect

import time


def is_authenticated(func):
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        response = func(request, *args, **kwargs)

        if request.user.is_staff:
            print('staf')
            response.set_cookie('is_admin', True)

        return response
    return wrapper


class TimeCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_now = time.time()
        response = self.get_response(request)
        time_elapsed = time.time() - time_now

        with open('time.txt', 'a', encoding='utf-8') as f:
            f.write(f"Запрос на путь - '{request.path}'. Время -  {str(time_elapsed)} \n")

        return response
