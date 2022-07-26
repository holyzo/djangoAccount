from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class MyUserAdmin(UserAdmin):

    for field in UserAdmin.fieldsets:
        if field[0] == 'Personal info':
            field[1]['fields'] += ('nickname','phone')

admin.site.register(User, MyUserAdmin)
