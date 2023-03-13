from django.shortcuts import render, get_object_or_404
from app_blog.models import BlogUser, Blog, Post
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def view_user_profile(request, username):
    user = get_object_or_404(BlogUser, username=username.lower())
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
    latest_posts = Post.objects.order_by('-date_posted')
    return render(request, 'app_blog/home.html', {'posts': latest_posts})

class UserProfileView(DetailView):
    model = BlogUser
    context_object_name = 'user'
    slug_field = 'username'  # use the 'username' field as the slug field

    def get_object(self, queryset=None):
        # get the 'username' argument from the URL
        username = self.kwargs.get(self.slug_field)
        # retrieve the corresponding BlogUser object
        return get_object_or_404(BlogUser, **{self.slug_field: username})
    
class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        url = self.kwargs.get('url')
        return get_object_or_404(Blog, url=url)
    
class PostDetailView(DetailView):
    model = Post
    content_object_name = 'post'

    def get_object(self, queryset=None):
        blog_url = self.kwargs.get('blog_url')
        pk = self.kwargs.get('pk')
        blog = get_object_or_404(Blog, url=blog_url)
        post = get_object_or_404(Post, pk=pk, blog=blog)
        return post