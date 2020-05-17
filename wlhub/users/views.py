from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'users/index.html', context)


def sign_in(request):
    context = {}
    return render(request, 'sign-in/index.html', context)
