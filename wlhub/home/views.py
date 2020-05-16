from django.shortcuts import render


def index(request):
    context = {
        "book": {
            "author": "Andjei Sapkovskiy",
            "name": "The Witcher 3",
            "category": "Fantasy"
        }
    }
    return render(request, 'home/index.html', context)
