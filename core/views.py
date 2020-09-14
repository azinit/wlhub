from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
def error_404(request, *args, **kwargs):
    context = {
        "status_code": 404,
        "message": "Страница не найдена",
        "details": "Проверьте введенный адрес",
    }
    return render(request, "errors_page/index.html", status=404, context=context)


def error_500(request, *args, **kwargs):
    context = {
        "status_code": 500,
        "message": "Внутренняя ошибка сервера",
        "details": "Попробуйте позднее",
    }
    return render(request, "errors_page/index.html", status=500, context=context)


@staff_member_required(login_url=reverse_lazy("account-index"))
def debug_404(request):
    raise Http404("DEBUG: force call 404 error")


@staff_member_required(login_url=reverse_lazy("account-index"))
def debug_500(request):
    """
    Искусственно вызываем ошибку на сервере, с помощью обращения к несуществующему параметру
    """
    value = request.POST.some_not_exist_key
