from django import forms
from django.contrib.auth import get_user_model
from .models import UserSurvey


# https://docs.djangoproject.com/en/3.0/topics/forms/
class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            "thumb",
            "username",
            "email",
        )


class UserSurveyForm(forms.ModelForm):
    class Meta:
        model = UserSurvey
        fields = (
            "is_student",
            "is_employee",
            "is_employer",
            "is_manager",
            "is_freelancer",
        )
