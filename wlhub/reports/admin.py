from django.contrib import admin
from reports.models import *

# Register your models here.
admin.site.register(Report, admin.ModelAdmin)
admin.site.register(ReportStatus, admin.ModelAdmin)