from django.shortcuts import render


def index(request):
    context = {
        "book": "The Witcher 3"
    }
    return render(request, 'home/index.html', context)
