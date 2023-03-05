from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_blog.models import BlogUser, Blog, Post

admin.site.register(BlogUser)
admin.site.register(Blog)
admin.site.register(Post)
