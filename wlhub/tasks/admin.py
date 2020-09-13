from django.contrib import admin

from core.mixins import ListLinksMixin
from tasks.models import *


@admin.register(Task)
class TaskAdmin(ListLinksMixin, admin.ModelAdmin):
    fields = ('name', 'subject', 'details', 'start_at', 'end_at', 'state', 'priority', 'report_status', "activity", "link")
    list_display = (
        'name', 'subject', 'details', 'state', 'report_status', 'priority', 'start_at', 'end_at', "updated_at", "activity")
    list_filter = (
        "subject__area__user",
        "state",
        "report_status",
        "priority",
        "activity",
    )


@admin.register(TaskState)
class TaskStateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


@admin.register(TaskActivity)
class TaskActivityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TaskPriority)
class TaskPriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
