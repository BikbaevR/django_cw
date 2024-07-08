from django.shortcuts import render
from django.http import HttpResponse

from django.views import View  #-
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView  #-
from .models import Post
from .forms import *
from django.urls import reverse_lazy


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


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PostDeatilView(DetailView):
    model = Post
    template_name = 'post/post_info.html'
    # slug_field =
    # slug_url_kwarg =
    pk_url_kwarg = 'post_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post_list')

    # fields = '__all__'
    # model = Post

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data)
        form.instance.title = 'no title'
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    # form_class = PostForm
    template_name = 'post/post_update.html'
    success_url = reverse_lazy('post_list')

    form_class = PostForm
    model = Post
    pk_url_kwarg = 'post_id'

