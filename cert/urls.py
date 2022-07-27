
from django.urls import path
from .views import *

app_name = 'cert'

urlpatterns = [
    path('certPhone/', certPhone, name='certPhone'),
]
