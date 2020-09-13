from django.shortcuts import render


# TODO: add mutations
# Create your views here.
def index(request):
    context = {}
    user = request.user
    context["areas"] = user.areas
    context["subjects"] = user.subjects
    context["tags"] = user.tags
    return render(request, "dictionaries/index.html", context=context)
