from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from core.mixins import LoginRequiredViewMixin
from core.utils import get_or_none
from tasks.forms import TaskForm
from tasks.models import Task
from comments.forms import CommentForm


class TasksListView(LoginRequiredViewMixin, ListView):
    model = Task
    template_name = "tasks/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.request.GET.get("category", "open")
        return context

    def get_queryset(self):
        user = self.request.user
        category = self.request.GET.get("category", "open")
        if category == 'open':
            return Task.open().filter(subject__area__user=user)
        if category == 'closed':
            return Task.closed().filter(subject__area__user=user)
        return []


@login_required
def task_details(request, pk: int):
    task = get_object_or_404(Task, pk=pk)

    context = {
        "task": task,
        "form_comment": CommentForm()
    }

    return render(request, 'task/index.html', context)


@login_required
def task_delete(request, pk: int):
    task: Task = get_or_none(Task, pk=pk)
    if not task:
        return redirect("tasks-details", pk=pk)

    task.delete()
    return redirect("tasks-list")


@login_required
def task_create(request):
    context = {}
    context["form"] = TaskForm()

    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            task: Task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("tasks-details", pk=task.pk)
        else:
            context["errors"] = ["Неверно заполнена форма. Проверьте введенные данные."]
    return render(request, "task/create.html", context=context)


@login_required
def task_edit(request, pk: int):
    task: Task = get_or_none(Task, pk=pk)
    if not task:
        return redirect("tasks-details", pk=pk)

    context = {}
    context["form"] = TaskForm(instance=task)
    context["task"] = task

    if request.POST:
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            next_task: Task = form.save(commit=False)
            next_task.save()
            return redirect("tasks-details", pk=task.pk)
        else:
            context["errors"] = ["Неверно заполнена форма. Проверьте введенные данные."]
    return render(request, "task/edit.html", context=context)
