from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'users/index.html', context)
