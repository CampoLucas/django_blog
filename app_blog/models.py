from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class BlogUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    bio = models.TextField(max_length=300, blank=True)
    url = models.SlugField(max_length=200, unique=True, editable=False)
    date_registered = models.DateTimeField(auto_now_add=True)

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
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.username)
        super().save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=600, blank=True)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE, related_name='author')
    date_created = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=200, unique=True, editable=False)

    def __str__(self):
        return f"{self.id:04}. {self.title} ({self.related_posts.count()} posts)"
    
    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super().save(*args, **kwargs)

class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='related_posts')
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    url = models.SlugField(max_length=200, unique=True, editable=False)

    STATE_CHOICES = (
        (True, 'Published'),
        (False, 'Draft'),
    )
    state = models.BooleanField(choices=STATE_CHOICES, default=False)
    
    def __str__(self):
        state_str = 'Published' if self.state else 'Draft'
        return f"{self.id:03}. {self.title} (Blog: {self.blog.title}) ({state_str})"
    
    def save(self, *args, **kwargs):
        self.url = f"post_{self.pk}"
        super().save(*args, **kwargs)

