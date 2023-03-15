from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import datetime

class BlogUser(AbstractUser):
    display_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='app_blog/assets/default_profile_picture.jpg', blank=True)
    bio = models.TextField(max_length=300, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='blog_users',
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_query_name='blog_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='blog_users',
        help_text=_('Specific permissions for this user.'),
        related_query_name='blog_user',
    )

    def __str__(self):
        return f"{self.id:02}. {self.username.lower()}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=600, blank=True, null=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='related_blogs')
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_pictures/', null=True, blank=True, default='app_blog/assets/default_blog_image.jpg')

    def __str__(self):
        return f"{self.id:04}. {self.title} ({self.related_posts.count()} posts)"

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='related_posts')
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id:03}. {self.title} (Blog: {self.blog.title})"
    
class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=3000)
    date = models.DateField(auto_now_add=True)

