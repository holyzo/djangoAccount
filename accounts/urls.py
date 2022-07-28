from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signup2/', signup2, name='signup2'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
