from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from app_blog.models import Post, Blog, BlogUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title...', 'required': True}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Feel free to write anything...', 'required': True}),
            
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'required': True}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitle'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class BlogUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BlogUser
        fields = ('display_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}),
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'display_name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email', 'required': True}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'required': True}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'required': True}),
        }

class BlogUserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BlogUser
        fields = ('username', 'display_name', 'email', 'bio', 'profile_picture', 'password')

class BlogUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    class Meta:
        model = BlogUser
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}),
        }