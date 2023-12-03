from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'username',
        'birth',
        'phone',
        'email',
        'address',
        'products',
        'money',
        'salary',
        'married',
        'main_bank',
        'save_type',
    )

    list_display_links = (
        'username',
        'birth',
        'phone',
        'email',
        'address',
        'products',
        'money',
        'salary',
        'married',
        'main_bank',
        'save_type',
    )