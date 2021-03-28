from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'media', 'amount']
    list_display = ['name', 'description', 'media', 'amount']
    search_fields = ['name', 'amount']


class CustomUserAdmin(UserAdmin):
     list_display = ['first_name', 'last_name', 'email']
     search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
