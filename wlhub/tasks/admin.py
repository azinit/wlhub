from django.contrib import admin
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
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'user')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('area', 'name', 'description')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'subject', 'state', 'report_status', 'priority')


admin.site.register(ReportStatus, admin.ModelAdmin)
admin.site.register(TaskPriority, admin.ModelAdmin)
admin.site.register(TaskState, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
