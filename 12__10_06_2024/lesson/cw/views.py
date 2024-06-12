from django.shortcuts import render
from .forms import PostForm, CategoryForm

from .models import Post, Category
# Create your views here.

def index(request):
    if request.method == 'POST':
        print('dasdasdasdsadasd')
        form = PostForm(request.POST)
        if form.is_valid():
            print('valid dasdasdasdsadasd')
            form.save()

    post = PostForm()

    return render(request, 'cw/index.html', {'post': post})




def posts(request):
    posts = Post.objects.all()
    return render(request, 'cw/posts.html', {'posts': posts})



def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()

    category_form = CategoryForm()
    return render(request, 'cw/add_category.html', {'category_form': category_form})



def list_category(request):
    category_list = Category.objects.all()
    return render(request, 'cw/list_category.html', {'category_list': category_list})


# def change_category(request, category_id):
#     category_obj = Category.objects.get(pk=category_id)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()