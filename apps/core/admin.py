from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.unregister(User)

@admin.register(User)
class NewUserAdmin(UserAdmin):
  list_display = [
    'username',
    'first_name',
    'last_name',
    'is_active',
    'is_staff',
  ]

