from django.shortcuts import render, get_object_or_404
from app_blog.models import Blog, Post
from app_blog.forms import BlogForm, PostForm, BlogUserCreationForm, BlogUserUpdateForm, BlogUserLoginForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.admin import User
from django.http import HttpResponseForbidden, Http404

class DispatchPermissions(UserPassesTestMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

class UserPermissions(DispatchPermissions):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        user_id = self.kwargs.get("pk")
        user = Blog.objects.get(id=user_id)
        return user == self.request.user

class BlogPermissions(DispatchPermissions):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        blog_id = self.kwargs.get("pk")
        blog = Blog.objects.get(id=blog_id)
        return blog.author == self.request.user

class PostPermissions(DispatchPermissions):
    def test_func(self):
        if self.request.user.is_staff:
            return True
        post = self.get_object()
        return post.blog.author == self.request.user   

class UserSignUp(CreateView):
    form_class = BlogUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

class UserLogin(LoginView):
    next_page = reverse_lazy('home')
    authentication_form = BlogUserLoginForm

class UserLogOut(LogoutView):
    next_page = reverse_lazy('home')

class UserDetail(DetailView):
    model = User
    context_object_name = 'user'

class UserUpdate(LoginRequiredMixin, UserPermissions, UpdateView):
    model = User
    form_class = BlogUserUpdateForm

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.pk})
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not self.request.user.is_superuser and self.request.user != obj:
            raise Http404
        return obj

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

class UserDelete(LoginRequiredMixin, UserPermissions, DeleteView):
    model = User
    success_url = reverse_lazy('home')
    
class UserBlogCreate(LoginRequiredMixin, UserPermissions, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author_id = self.kwargs['pk']
        response = super().form_valid(form)
        self.object = form.save()
        self.success_url = reverse_lazy('user-detail', kwargs={'pk': self.kwargs['pk']})
        return response
    
    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.pk})
    
class BlogDetail(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        related_posts = self.object.related_posts.all().order_by('-date_posted')
        context['related_posts'] = related_posts
        return context

class BlogUpdate(LoginRequiredMixin, BlogPermissions, UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy('blog-detail', kwargs={'pk': self.object.pk})  

class BlogDelete(LoginRequiredMixin, BlogPermissions, DeleteView):
    model = Blog
    
    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.author.id})
    
class PostDetail(DetailView):
    model = Post
    content_object_name = 'post'
    success_url = reverse_lazy('home')
    
class PostCreate(LoginRequiredMixin, BlogPermissions, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.blog_id = self.kwargs['pk']
        response = super().form_valid(form)
        self.object = form.save()
        return response
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostUpdate(LoginRequiredMixin, PostPermissions, UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostDelete(LoginRequiredMixin, PostPermissions, DeleteView):
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