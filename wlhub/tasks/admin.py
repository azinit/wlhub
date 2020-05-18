from django.contrib import admin

from core.mixins import ListLinksMixin
from tasks.models import (
    ReportStatus,
    TaskPriority,
    Subject,
    TaskState,
    Area,
    Task,
    Tag
)


@admin.register(Area)
class AreaAdmin(ListLinksMixin, admin.ModelAdmin):
    list_display = ('name', 'description', 'user')


@admin.register(Subject)
class SubjectAdmin(ListLinksMixin, admin.ModelAdmin):
    list_display = ('area', 'name', 'description')


@admin.register(Task)
class TaskAdmin(ListLinksMixin, admin.ModelAdmin):
    fields = ('name', 'subject', 'details', 'start_at', 'end_at', 'state', 'priority', 'report_status')
    list_display = ('name', 'subject', 'details', 'state', 'report_status', 'priority', 'start_at', 'end_at')


@admin.register(TaskState)
class TaskStateAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


admin.site.register(ReportStatus, admin.ModelAdmin)
admin.site.register(TaskPriority, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
