from django.urls import path
from .views import index, sign_in, logout

urlpatterns = [
    path('', index, name='account-index'),
    path('sign-in', sign_in, name='account-sign-in'),
    path('logout', logout, name='account-logout'),
]