from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from app_blog.models import Post, Blog, BlogUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BlogUser
        fields = ('username', 'password1', 'password2', 'email', 'birthday', 'display_name')

class BlogUserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BlogUser
        fields = ('username', 'display_name', 'email', 'phone_number', 'birthday', 'bio', 'profile_picture', 'password', 'date_joined')