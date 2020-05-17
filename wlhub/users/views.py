from django.contrib.auth import logout as _logout
from django.shortcuts import render, redirect


def index(request):
    context = {}
    return render(request, 'users/index.html', context)


def sign_in(request):
    context = {}
    return render(request, 'sign-in/index.html', context)


def logout(request):
    _logout(request)
    return redirect('/')
