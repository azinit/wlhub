from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
from tasks.models import Task


class Comment(models.Model):
    """
    Комментарий к задаче
    TODO: Сделать более общим
    """
    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField("Содержание", max_length=512)
    start_at = models.DateTimeField("Дата создания", blank=True, auto_now_add=True)
    updated_at = models.DateTimeField("Дата редактирования", blank=True, auto_now=True, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Связанная задача", related_name="comments")

    def __str__(self):
        return f'{self.user}#{self.pk} - {self.start_at}'
