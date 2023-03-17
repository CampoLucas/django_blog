from django.contrib.auth.backends import BaseBackend
from .models import BlogUser

class BlogUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = BlogUser.objects.get(username=username)
            if user.check_password(password):
                return user
        except BlogUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return BlogUser.objects.get(pk=user_id)
        except BlogUser.DoesNotExist:
            return None