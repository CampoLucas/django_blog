from django.shortcuts import render, get_object_or_404
from app_blog.models import BlogUser, Blog, Post

def view_user_profile(request, username):
    user = get_object_or_404(BlogUser, username=username)
    context = {'user': user}
    return render(request, 'app_blog/user_profile.html', context)

def view_blog_page(request ,blog_url):
    blog = get_object_or_404(Blog, url=blog_url)
    posts = blog.related_posts.all()
    user = blog.author
    context = {'blog': blog, 'posts': posts}
    return render(request, 'app_blog/blog_page.html', context)

def view_post_page(request, blog_url, post_url):
    blog = get_object_or_404(Blog, url=blog_url)
    post = get_object_or_404(Post, url=post_url, blog=blog)
    context = {'post': post}
    return render(request, 'app_blog/post_page.html', context)

def login(request):
    return render(request, 'app_blog/login.html')

def register(request):
    return render(request, 'app_blog/register.html')

def home(request):
    return render(request, 'app_blog/home.html')