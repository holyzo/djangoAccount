from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.validators import RegexValidator
from ably import common

phone_validator = RegexValidator(common.PATT_PHONE,
                                 "The phone number must be provided only number letter")

class CertPhoneInputForm(forms.Form):
    name                        = models.CharField(max_length=128)
    socialSecurityNumberFront   = models.DecimalField(min_length=6, max_length=6)
    gender                      = models.DecimalField(min_length=1, max_length=1)
    phone                       = models.CharField(min_length=10,
                                                   max_length=11,
                                                   validators=[phone_validator,])

class CertPhoneRecvNumberForm(forms.Form):
    certType = 0
    name = ''
    phone = ''

    certNum = models.CharField(min_length=6, max_length=6,
                              validators=[
                                RegexValidator("[0-9]{6}", "The cert number must be provided only number letter"),
                              ])