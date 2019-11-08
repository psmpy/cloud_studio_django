# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile as User

class RegisterForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = User
    fields = ('username', 'email')

