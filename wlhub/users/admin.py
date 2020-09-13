from django.contrib import admin
from django.contrib.auth import get_user_model

from core.mixins import ListLinksMixin


@admin.register(get_user_model())
class UserAdmin(ListLinksMixin, admin.ModelAdmin):
    fields = (
        'is_superuser',
        'first_name',
        'last_name',
        'email',
        'username',
        'password',
        "thumb",
    )

    list_display = (
        'username',
        'first_name',
        'last_name',
        'email'
    )
