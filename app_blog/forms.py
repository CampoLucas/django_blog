from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from app_blog.models import Post, Blog, Avatar

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
    display_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'display_name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('display_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}),
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'display_name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email', 'required': True}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'required': True}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password', 'required': True}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            Avatar.objects.create(user=user, display_name=self.cleaned_data['display_name'])
        return user

class BlogUserUpdateForm(UserChangeForm):
    display_name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'display_name'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    bio = forms.CharField(max_length=300, required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bio', 'rows': 3}))
    profile_picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = User
        fields = ('username', 'display_name', 'email', 'bio', 'profile_picture')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required': True}),
            'display_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'display_name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email', 'required': True}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'bio'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.avatar:
            self.fields['display_name'].initial = self.instance.avatar.display_name
            self.fields['bio'].initial = self.instance.avatar.bio
            self.fields['profile_picture'].initial = self.instance.avatar.profile_picture
    
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.avatar.display_name = self.cleaned_data['display_name']
        user.avatar.bio = self.cleaned_data['bio']

        if self.cleaned_data['profile_picture']:
            user.avatar.profile_picture = self.cleaned_data['profile_picture']

        if commit:
            user.avatar.save()
        return user

class BlogUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }