from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get-all-posts/', views.get_all_posts,name='get-all-posts'),
    path('create-post/', views.create_post,name='create-post'),
    path('delete-post/', views.delete_post , name='delete-post'),
     path('get-post/', views.get_post, name='get-post')
]
