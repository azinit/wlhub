from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.utils import get_or_none
from tasks.models import Task


@login_required
def task_list(request):
    user = request.user
    context = {
        "tasks": Task.objects.filter(subject__area__user=user)
    }
    return render(request, 'tasks/index.html', context)


def task_details(request, pk: int):
    task = get_or_none(Task, pk=pk)
    context = {
        "task": task
    }
    return render(request, 'task/index.html', context)
