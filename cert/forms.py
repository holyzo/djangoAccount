from django import forms
from .models import CertPhoneInput, CertPhoneRecvNumber, ChangePassword
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import pdb



class CertPhoneInputForm(forms.ModelForm):
    certType = 0

    class Meta:
        model = CertPhoneInput
        fields = ['name', 'socialSecurityNumberPre', 'gender', 'phone']


class CertPhoneRecvNumberForm(forms.ModelForm):

    class Meta:
        model = CertPhoneRecvNumber
        fields = ['number']


class ChangePasswordForm(forms.ModelForm):

    class Meta:
        model = ChangePassword
        fields = ['password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }


    def cleaned_password1(self):
        pw1 = self.cleaned_data.get('password1')
        validate_password(pw1)


    def clean(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')

        if pw1 != pw2:
            msg = 'Password and Password confirm field must be same characters.'
            self.add_error('password2', msg)
            raise ValidationError(msg)