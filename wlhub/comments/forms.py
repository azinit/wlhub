from django import forms
from .models import *


# https://docs.djangoproject.com/en/3.0/topics/forms/
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "content",
        )
