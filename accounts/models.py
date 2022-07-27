from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from django.utils.translation import gettext as _
from ably import common

phone_validator = RegexValidator(common.PATT_PHONE,
                                 "The phone number must be provided only number letter")
username_validator = RegexValidator(common.PATT_USERNAME,
                                    "The username must be provided alphabet and number letter")

class User(AbstractUser):
    username    = models.CharField(max_length=32, validators=[username_validator], unique=True)
    name        = models.CharField(max_length=128)
    email       = models.EmailField(validators=[EmailValidator], unique=True)
    phone       = models.CharField(min_length=10, max_length=11, validators=[phone_validator], unique=True)
    nickname    = models.CharField(max_length=32)

    REQUIRED_FIELDS = ["name", "email", "phone", "nickname"]
