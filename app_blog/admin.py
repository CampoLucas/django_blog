from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_blog.models import BlogUser, Blog, Post

class BlogUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

admin.site.register(BlogUser)
admin.site.register(Blog)
admin.site.register(Post)
