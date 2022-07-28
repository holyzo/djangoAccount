from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms
from ably import common
import re

from django.contrib.auth import get_user_model

class ViewUserForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'name', 'phone', 'email', 'nickname']


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'password1', 'password2', 'phone', 'email', 'nickname']
