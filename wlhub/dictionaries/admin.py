from django.contrib import admin

from core.mixins import ListLinksMixin
from dictionaries.models import *


# Register your models here.
@admin.register(Tag)
class TagAdmin(ListLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'user')
    list_filter = ("user", )


@admin.register(Area)
class AreaAdmin(ListLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'user')


@admin.register(Subject)
class SubjectAdmin(ListLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'area', 'description')
