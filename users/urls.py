from django.urls import path

from .views import *

app_name = "account"

urlpatterns = [
    path('', index, name='index'),
    path('settings', settings, name='settings'),
    path('survey', SurveyForm.as_view(), name='survey'),
    path('sign-in', sign_in, name='sign-in'),
    path('sign-up', sign_up, name='sign-up'),
    path('logout', logout, name='logout'),
]
