from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/',         signup, name='signup'),
    path('forgotPassword/', forgotPassword, name='forgotPassword'),
    path('register/',       register, name='register'),
    path('login/',          login, name='login'),
    path('logout/',         logout, name='logout'),
    path('myInfo/',         myInfo, name='myInfo'),
]
