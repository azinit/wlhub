from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.utils import get_or_none
from tasks.models import Task


@login_required
def task_list(request):
    user = request.user

    tasks = []
    category = request.GET.get("category", "open")
    if category == 'open':
        tasks = Task.open().filter(subject__area__user=user)
    if category == 'closed':
        tasks = Task.closed().filter(subject__area__user=user)

    context = {
        "tasks": tasks,
        "category": category
    }
    return render(request, 'tasks/index.html', context)

@login_required
def task_details(request, pk: int):
    task = get_or_none(Task, pk=pk)
    context = {
        "task": task
    }
    return render(request, 'task/index.html', context)

@login_required
def task_delete(request, pk: int):
    task: Task = get_or_none(Task, pk=pk)
    if not task:
        return redirect("tasks-details", pk=pk)

    task.delete()
    return redirect("tasks-list")
