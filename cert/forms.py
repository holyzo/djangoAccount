from django import forms
from .models import CertPhoneInput
import pdb



class CertPhoneInputForm(forms.ModelForm):
    certType = 0

    class Meta:
        model = CertPhoneInput
        fields = ['name', 'socialSecurityNumberPre', 'gender', 'phone']

    '''
    name                        = models.CharField('name', max_length=128,
                                                    validators=[MinValueValidator(2),])
    socialSecurityNumberPre     = models.CharField('socialSecurityNumber',max_length=6,
                                                      validators=[ssNumberPre_validator,])
    gender                      = models.CharField('gender', max_length=1)
    phone                       = models.CharField('phone', max_length=11,
                                                   validators=[phone_validator,])
    certType = 0

    def clean_name(self):
        pdb.set_trace()

        return name

    def clean(self):
        clean_name = self.cleaned_data.get('name')
        if not clean_name:
            msg = 'The name must be provided 2-128 size letter'
            self.add_error('name', msg)
            raise forms.ValidationError(msg)

        #clean_socialSecurityNumberPre = self.cleaned_data.get('socialSecurityNumberPre')
    '''




class CertPhoneRecvNumberForm(forms.ModelForm):
    certType = 0
    name = ''
    phone = ''
'''
    certNum = models.CharField(max_length=6,
                              validators=[
                                RegexValidator("[0-9]{6}", "The cert number must be provided only number letter"),
                              ])
'''