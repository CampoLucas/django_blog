from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from app_blog.models import Post, Blog, BlogUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title...', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Feel free to write anything...', 'required': True}),
            
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title...', 'required': True}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitle...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class BlogUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = BlogUser
        fields = ('username', 'password1', 'password2', 'email', 'display_name')

class BlogUserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = BlogUser
        fields = ('username', 'display_name', 'email', 'bio', 'profile_picture', 'password')