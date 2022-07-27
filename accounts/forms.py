from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from ably import common
import re


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'phone', 'email', 'nickname']
