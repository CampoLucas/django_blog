from django.shortcuts import render, get_object_or_404
from app_blog.models import Blog, Post
from app_blog.forms import BlogForm, PostForm, BlogUserCreationForm, BlogUserUpdateForm, BlogUserLoginForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.admin import User
from django.http import HttpResponseForbidden

class BlogUserSignUp(CreateView):
    form_class = BlogUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

class BlogUserLogin(LoginView):
    next_page = reverse_lazy('home')
    authentication_form = BlogUserLoginForm

class BlogUserLogOut(LogoutView):
    next_page = reverse_lazy('home')

class BlogUserDetail(DetailView):
    model = User
    context_object_name = 'user'

class BlogUserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = BlogUserUpdateForm

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})
    
    def get_object(self, queryset=None):
        return self.request.user

    def get_form_kwargs(self):
        kwargs = super(BlogUserUpdate, self).get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

class BlogUserDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('home')
    
class BlogDetail(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_posts = self.object.related_posts.all().order_by('-date_posted')
        context['related_posts'] = related_posts
        return context

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        self.object = form.save()
        self.success_url = reverse_lazy('user-detail', kwargs={'pk': self.request.user.pk})
        return response
    
    def get_success_url(self):
        return self.success_url
    
class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.pk})
    
    def dispatch(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author != self.request.user:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    
    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.author.id})
    
class PostDetail(DetailView):
    model = Post
    content_object_name = 'post'
    success_url = reverse_lazy('home')
    
class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['pk']
        response = super().form_valid(form)
        self.object = form.save()
        return response
    
    def get_success_url(self):
        blog_id = self.kwargs['pk']
        return reverse('blog-detail', kwargs={'pk': blog_id})

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    
    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.blog.id})
    
class HomeList(ListView):
    model = Post
    template_name = 'app_blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostSearch(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        criteria = self.request.GET.get('criteria')
        result = Post.objects.filter(title__icontains=criteria).all()
        return result

class MessageDetail(LoginRequiredMixin, DetailView):
    pass

class MessageList(LoginRequiredMixin, ListView):
    pass

class MessageCreate(LoginRequiredMixin, CreateView):
    pass

class MessageDelete(LoginRequiredMixin, DeleteView):
    pass