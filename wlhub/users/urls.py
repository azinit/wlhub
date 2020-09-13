from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='account-index'),
    path('settings', settings, name='account-settings'),
    path('survey', survey, name='account-survey'),
    path('sign-in', sign_in, name='account-sign-in'),
    path('sign-up', sign_up, name='account-sign-up'),
    path('logout', logout, name='account-logout'),
]