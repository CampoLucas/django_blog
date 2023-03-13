"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_blog.views import view_user_profile, view_blog_page, view_post_page, login, register, home, UserProfileView, BlogDetailView, PostDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('@<str:username>', UserProfileView.as_view(), name='user_profile'),
    path('blog/<slug:url>', BlogDetailView.as_view(), name='blog_detail'),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('blog/<slug:blog_url>/<int:pk>', PostDetailView.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
