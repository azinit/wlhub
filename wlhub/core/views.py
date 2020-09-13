from django.shortcuts import render


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
