from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='login'), name='dispatch')
class CategoryView(ListView):
    model = Genre
    template_name = 'spotify/index.html'
    context_object_name = 'genres'


#Миксины

@method_decorator(login_required(login_url='login'), name='dispatch')
class OneCategoryView(DetailView):
    model = Genre
    template_name = 'spotify/music.html'
    context_object_name = 'genres'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = context.get('genres')
        context['musics'] = genre.musics.all()
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class MusicDetail(DetailView):
    model = Music
    template_name = 'spotify/one_music.html'
    context_object_name = 'music'


    def get(self, request, *args, **kwargs):
        History.objects.create(
            music=Music.objects.get(pk=self.kwargs['pk']),
            user=self.request.user
        )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        music = context.get('music')
        genres = music.genres.all()
        context['genre'] = genres
        context['genres_str'] = ', '.join(map(lambda genre: genre.name, genres))
        return context
