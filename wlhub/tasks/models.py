from django.contrib.auth import get_user_model
from django.db import models

from core.mixins import ModelStrMixin
from users.models import Tag


class Area(ModelStrMixin, models.Model):
    """
    Область задач
    :remark В частных случаях - Заказчик, Проект, Компания и т.д.
    :example ИТИС
    """

    class Meta:
        verbose_name = "Область задач"
        verbose_name_plural = "Области задач"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=32)
    description = models.TextField("Описание", blank=True, default="")


class Subject(ModelStrMixin, models.Model):
    """
    Субъект задачи
    :example Django (ИТИС)
    """

    class Meta:
        verbose_name = "Субъект задач"
        verbose_name_plural = "Субъекты задач"

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=32)
    description = models.TextField("Описание", blank=True, default="")


class TaskState(ModelStrMixin, models.Model):
    """
    Состояние задачи
    :example "В работе", "Провалено", ...
    """

    class Meta:
        verbose_name = "Состояние задачи"
        verbose_name_plural = "Состояния задачи"

    name = models.CharField("Название", max_length=16)


class TaskPriority(ModelStrMixin, models.Model):
    """
    Приоритет задачи
    :example "Важно (5)"
    """

    class Meta:
        verbose_name = "Приоритет задач"
        verbose_name_plural = "Приоритеты задач"

    name = models.CharField("Название", max_length=16)
    value = models.IntegerField("Целочисленное значение приоритета")


class ReportStatus(ModelStrMixin, models.Model):
    """
    Статус отчетности
    :example По готовности
    По сроку
    В конце месяца
    Еженедельно
    ...
    """

    class Meta:
        verbose_name = "Статус отчетности"
        verbose_name_plural = "Статусы отчетности"

    name = models.CharField("Название", max_length=16)


class Task(ModelStrMixin, models.Model):
    """
    Задача
    :example Семестровка (ИТИС/Django)
    """

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    name = models.CharField("Название", max_length=32)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    details = models.TextField("Детали задачи", default="")
    state = models.ForeignKey(TaskState, on_delete=models.SET_NULL, null=True)
    report_status = models.ForeignKey(ReportStatus, on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(TaskPriority, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
