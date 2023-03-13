from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app_blog.models import BlogUser, Blog, Post
from app_blog.forms import BlogUserUpdateForm, BlogUserCreationForm

class BlogUserAdmin(UserAdmin):
    form = BlogUserUpdateForm
    add_form = BlogUserCreationForm
    
    list_display = ('username', 'display_name', 'email', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

    fieldsets = (
        ('PROFILE', {'fields': ('display_name', 'username', 'bio', 'profile_picture')}),
        ('PERSONAL INFORMATION', {'fields': ('email', 'phone_number', 'birthday')}),
        ('SECURITY', {'fields': ('password',)}),
        ('DATES', {'fields': ('last_login', 'date_joined')}),
        ('PERMISSIONS', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'display_name', 'email', 'birthday', 'password1', 'password2'),
        }),
    )

admin.site.register(BlogUser, BlogUserAdmin)
admin.site.register(Blog)
admin.site.register(Post)
