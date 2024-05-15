from django.urls import path, re_path
from .views import index, about, contact, publication, delete_post, category_list, category_from_id

urlpatterns = [
    path('', index, name='index_page'),
    path('about', about, name='about_page'),
    path('contact', contact, name='contact_page'),
    path('post/info/<int:id>', publication),
    path('post/delete/<int:id>', delete_post),
    path('categories', category_list, name = 'categories'),
    path('post/categories/<int:id>', category_from_id, name = 'categ_id')
    # re_path(r'^post', publication),
]