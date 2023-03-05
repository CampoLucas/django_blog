from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_blog.models import BlogUser

admin.site.register(BlogUser)
