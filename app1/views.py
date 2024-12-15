from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def hello(request):
    return HttpResponse("Hello, Django!")
def greet(request):
    return render(request, 'hi.html', {'name': 'Aska Robo'})
def blog_list(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'blog_list.html', {'posts': posts})
def blog_detail(request, id):
    post = Post.objects.get(pk=id)  # Fetch post by primary key (id)
    return render(request, 'blog_detail.html', {'post': post})
