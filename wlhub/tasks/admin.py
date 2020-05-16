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
# Register your models here.
admin.site.register(Area, admin.ModelAdmin)
admin.site.register(Subject, admin.ModelAdmin)
admin.site.register(Task, admin.ModelAdmin)
admin.site.register(ReportStatus, admin.ModelAdmin)
admin.site.register(TaskPriority, admin.ModelAdmin)
admin.site.register(TaskState, admin.ModelAdmin)
admin.site.register(Tag, admin.ModelAdmin)
