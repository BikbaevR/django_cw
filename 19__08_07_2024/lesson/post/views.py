from django.shortcuts import render
from django.http import HttpResponse


from django.views import View #-
from django.views.generic import TemplateView#-
from .models import Post

def index(request):
    return HttpResponse('')



class IndexView(View):
    def get(self, request):
        return render(request, 'post/index.html')

    def post(self, request):
        # print('post')
        return render(request, 'post/index.html')


class IndexView2(TemplateView):
    template_name = 'post/index.html'
    extra_context = {
        'text': 'hello from template view'
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['objects'] = 'test'
        print(context)

        return context