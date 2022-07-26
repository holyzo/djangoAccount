from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# TODO User 필드 맞춰줘야 함.
admin.site.register(User, UserAdmin)