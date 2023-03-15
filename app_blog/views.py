from django.shortcuts import render, get_object_or_404
from app_blog.models import BlogUser, Blog, Post
from app_blog.forms import BlogForm, PostForm, BlogUserCreationForm, BlogUserUpdateForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView

class BlogUserSignUp(CreateView):
    form_class = BlogUserCreationForm
    template_name = 'registration/signup.html'
    next_page = reverse_lazy('home')

class BlogUserLogin(LoginView):
    next_page = reverse_lazy('home')

class BlogUserLogOut(LogoutView):
    next_page = reverse_lazy('home')

class BlogUserDetail(DetailView):
    model = BlogUser
    context_object_name = 'user'

class BlogUserUpdate(UpdateView):
    model = BlogUser
    form_class = BlogUserUpdateForm

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})

class BlogUserDelete(DeleteView):
    model = BlogUser
    success_url = reverse_lazy('home')
    
class BlogDetail(DetailView):
    model = Blog

class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        response = super().form_valid(form)
        # get the id of the newly created blog
        blog_id = self.object.id
        # set the success URL to the blog detail page for the newly created blog
        self.success_url = reverse('blog-detail', kwargs={'pk': blog_id})
        return response
    
class BlogUpdate(UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.pk})

class BlogDelete(DeleteView):
    model = Blog
    
    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.author.id})
    
class PostDetail(DetailView):
    model = Post
    content_object_name = 'post'
    
class PostCreate(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        response = super().form_valid(form)
        # get the id of the newly created post
        post_id = self.object.id
        # set the success URL to the post detail page for the newly created post
        self.success_url = reverse('post-detail', kwargs={'pk': post_id})
        return response

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostDelete(UpdateView):
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.blog.id})
    
class HomeList(ListView):
    model = Post
    template_name = 'app_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class MessageDetail(DetailView):
    pass

class MessageList(ListView):
    pass

class MessageCreate(CreateView):
    pass

class MessageDelete(DeleteView):
    pass