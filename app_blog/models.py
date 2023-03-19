
from django.contrib.auth.admin import User
from django.db import models


    
class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="avatar")
    display_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=300, blank=True, null=True)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=600, blank=True, null=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='related_blogs')
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

