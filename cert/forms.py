from django import forms
from django.core.validators import RegexValidator
from django.db import models
from ably import common

phone_validator = RegexValidator(common.PATT_PHONE,
                                 "The phone number must be provided only number letter")

ssNumberPre_validator = RegexValidator(common.PATT_SOCIAL_SECURITY_NUMBER_PRE,
                                 "The social security number prefix must be provided only 6 numbers letter")


class CertPhoneInputForm(forms.Form):
    name                        = models.CharField(max_length=128)
    socialSecurityNumberPre   = models.CharField(max_length=6,
                                                      validators=[ssNumberPre_validator,])
    gender                      = models.CharField(max_length=1)
    phone                       = models.CharField(max_length=11,
                                                   validators=[phone_validator,])

class CertPhoneRecvNumberForm(forms.Form):
    certType = 0
    name = ''
    phone = ''

    certNum = models.CharField(max_length=6,
                              validators=[
                                RegexValidator("[0-9]{6}", "The cert number must be provided only number letter"),
                              ])