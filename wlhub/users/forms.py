from django import forms
from django.contrib.auth import get_user_model

from .models import *


# https://docs.djangoproject.com/en/3.0/topics/forms/
class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
        )
