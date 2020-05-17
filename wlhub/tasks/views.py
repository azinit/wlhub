from django.shortcuts import render

from core.utils import get_or_none
from tasks.models import Task


def index(request):
    context = {}
    return render(request, 'tasks/index.html', context)


def task_details(request, pk: int):
    task = get_or_none(Task, pk=pk)
    context = {
        "task": task
    }
    return render(request, 'task/index.html', context)
