from django.contrib import admin

from core.mixins import ListLinksMixin
from .models import *


# Register your models here.
@admin.register(Comment)
class ModelAdmin(ListLinksMixin, admin.ModelAdmin):
    list_display = ('__str__', 'user', 'task', 'content', )
    list_filter = ("user", "task")
