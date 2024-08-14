import traceback

from django.http import HttpResponse


class TestMiddleware:
    def __init__(self, get_response): #get_response либо ссылка на след Middleware либо View
        self._get_response = get_response

    def __call__(self, request):
        # print(request.path)
        # print('TestMiddleware before')
        # return HttpResponse('TestMiddleware')
        response = self._get_response(request)
        response['is_admin'] = True
        response.set_cookie('coockie_name', 'coockie_value')
        # print('TestMiddleware after')
        return response

    def process_view(self, request, view_func, *args, **kwargs):
        # print(view_func.__qualname__)
        # print(args)
        # print(kwargs)
        ...

    def process_exception(self, request, exception, *args, **kwargs):
        print(exception)
        return HttpResponse('Произошла ошибка')

class SecondMiddleware:
    def __init__(self, get_response): #get_response либо ссылка на след Middleware либо View
        self._get_response = get_response

    def __call__(self, request):
        # print('SecondMiddleware before')
        response = self._get_response(request)
        # print('SecondMiddleware after')
        return response



def my_middleware(custom_args):
    def decorated(func):
        def wrapped(*args, **kwargs):
            print('before')
            print(custom_args)
            result = func(*args, **kwargs)
            print('after')
            return result
        return wrapped
    return decorated
