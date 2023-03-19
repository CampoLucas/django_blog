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
from app_blog.views import ( UserLogin, UserSignUp, UserLogOut, UserDetail, UserUpdate, UserDelete, BlogDetail, UserBlogCreate, BlogUpdate, BlogDelete, 
    PostDetail, PostCreate, PostUpdate, PostDelete, HomeList, MessageDetail, MessageCreate, MessageDelete, MessageList, PostSearch )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeList.as_view(), name='home'),
    path('login', UserLogin.as_view(), name='login'),
    path('register', UserSignUp.as_view(), name='register'),
    path('logout', UserLogOut.as_view(), name='logout'),
    path('user/<pk>', UserDetail.as_view(), name='user-detail'),
    path('user/<pk>/update', UserUpdate.as_view(), name='user-update'),
    path('user/<pk>/delete', UserDelete.as_view(), name='user-delete'),
    path('user/<pk>/add-blog', UserBlogCreate.as_view(), name='user-add-blog'),
    path('blog/<pk>', BlogDetail.as_view(), name='blog-detail'),
    path('blog/<pk>/update', BlogUpdate.as_view(), name='blog-update'),
    path('blog/<pk>/delete', BlogDelete.as_view(), name='blog-delete'),
    path('blog/<pk>/add-post', PostCreate.as_view(), name='blog-add-post'),
    path('post/search', PostSearch.as_view(), name='post-search'),
    path('post/<pk>', PostDetail.as_view(), name='post-detail'),
    path('post/<pk>/update', PostUpdate.as_view(), name='post-update'),
    path('post/<pk>/delete', PostDelete.as_view(), name='post-delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)