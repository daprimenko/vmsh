from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import capfirst
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class EmailUsernameForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            try:
                possible_user = User.objects.get(email=username)
                user = authenticate(username=possible_user.username, password=password)
            except User.DoesNotExist:
                user = None

        if user is not None and user.is_active:
            self.cleaned_data.update({'username': user.username})

        return super(EmailUsernameForm, self).clean()
