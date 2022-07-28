from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from ably import common, settings

import pdb

phone_validator = RegexValidator(common.PATT_PHONE,
                                 "The phone number must be provided only number letter")

ssNumberPre_validator = RegexValidator(common.PATT_SOCIAL_SECURITY_NUMBER_PRE,
                                 "The social security number prefix must be provided only 6 numbers letter")


def getDefaultPasswordValidators(settings):
    validators = []
    pdb.set_trace()
    for ele in settings.AUTH_PASSWORD_VALIDATORS:
        validators.append(ele['NAME'])

    return validators


class CertPhoneInput(models.Model):
    name = models.CharField('name', max_length=128,
                            validators=[])
    socialSecurityNumberPre = models.CharField('socialSecurityNumber', max_length=6,
                                               validators=[ssNumberPre_validator, ])
    gender = models.CharField('gender', max_length=1)
    phone = models.CharField('phone', max_length=11,
                             validators=[phone_validator, ])


class CertPhoneRecvNumber(models.Model):
    number = models.CharField('number', max_length=6,
                            validators=[ssNumberPre_validator,])


class ChangePassword(models.Model):
    password1 = models.CharField('password1', max_length=128)
    password2 = models.CharField('password2', max_length=128)