from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hi/', views.greet, name='greet'),
    path('posts/', views.blog_list, name='blog_list'),  # List of posts
    path('post/<int:id>/', views.blog_detail, name='blog_detail'),  # Single post detail
]