from django.urls import path

from .views import index, sign_in, logout, sign_up

urlpatterns = [
    path('', index, name='account-index'),
    path('sign-in', sign_in, name='account-sign-in'),
    path('sign-up', sign_up, name='account-sign-up'),
    path('logout', logout, name='account-logout'),
]