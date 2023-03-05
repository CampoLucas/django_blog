from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

class BlogUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(max_length=300, blank=True)
    url = models.SlugField(max_length=200, unique=True, editable=False)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id:02}. {self.username.lower()}"
    
    def save(self, *args, **kwargs):
        self.url + slugify(self.username)
        super().save(*args, **kwargs)

