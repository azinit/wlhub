from django.shortcuts import redirect

from core.utils import get_or_none
from tasks.models import Task
from .models import Comment
from .forms import CommentForm


# Create your views here.
def comments_create(request, pk: int):
    task = get_or_none(Task, pk=pk)
    if task is None:
        return redirect("tasks:list")

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment: Comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
    return redirect("tasks:view", pk=task.pk)
