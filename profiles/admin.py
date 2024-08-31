from django.contrib import admin
from profiles.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
admin.site.register(User)
