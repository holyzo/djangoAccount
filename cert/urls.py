
from django.urls import path
from .views import *

app_name = 'cert'

urlpatterns = [
    path('certPhone/',              certPhone, name='certPhone'),
    path('certPhoneRecvNumber/',    certPhoneRecvNumber, name='certPhoneRecvNumber'),
    path('changePassword/',         changePassword, name='changePassword'),
]
