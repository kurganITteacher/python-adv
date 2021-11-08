from django.contrib.auth.forms import AuthenticationForm

from authapp.models import UserProfile


class MyAuthForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'password')
