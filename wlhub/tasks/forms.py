from django import forms
from .models import *


# https://docs.djangoproject.com/en/3.0/topics/forms/
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "state",
            "details",
            "subject",
            "report_status",
            "priority",
            # TODO: "tags",
            "end_at",
        )
