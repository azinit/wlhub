from django import forms
from .models import *


# https://docs.djangoproject.com/en/3.0/topics/forms/
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "subject",
            "details",
            "state",
            "report_status",
            "priority",
            "tags",
            "end_at",
        )
