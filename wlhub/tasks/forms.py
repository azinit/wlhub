from django import forms
from .models import *


# https://docs.djangoproject.com/en/3.0/topics/forms/
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "details",
            "state",
            "priority",
            "subject",
            "activity",
            "report_status",
            # TODO: "tags",
            "end_at",
        )
