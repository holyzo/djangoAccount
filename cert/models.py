from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from ably import common

phone_validator = RegexValidator(common.PATT_PHONE,
                                 "The phone number must be provided only number letter")

ssNumberPre_validator = RegexValidator(common.PATT_SOCIAL_SECURITY_NUMBER_PRE,
                                 "The social security number prefix must be provided only 6 numbers letter")

class CertPhoneInput(models.Model):
    name = models.CharField('name', max_length=128,
                            validators=[])
    socialSecurityNumberPre = models.CharField('socialSecurityNumber', max_length=6,
                                               validators=[ssNumberPre_validator, ])
    gender = models.CharField('gender', max_length=1)
    phone = models.CharField('phone', max_length=11,
                             validators=[phone_validator, ])
