from datetime import datetime, timedelta

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

    def __str__(self):
        return f'{self.area}/{self.name}'


class TaskState(ModelStrMixin, models.Model):
    """
    Состояние задачи
    :example "В работе", "Провалено", ...
    """

    class Meta:
        verbose_name = "Состояние задачи"
        verbose_name_plural = "Состояния задачи"

    name = models.CharField("Название", max_length=16)
    code = models.CharField("Кодовое обозначение", max_length=2)

    def __str__(self):
        return self.name


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
    subject = models.ForeignKey(Subject, verbose_name="Субъект задачи", on_delete=models.CASCADE)
    details = models.TextField("Детали задачи", default="")
    state = models.ForeignKey(TaskState, verbose_name="Состояние", on_delete=models.SET_NULL, blank=True, null=True, default=1)
    report_status = models.ForeignKey(ReportStatus, verbose_name="Статус отчетности", on_delete=models.SET_NULL, null=True)
    priority = models.ForeignKey(TaskPriority, verbose_name="Приоритет", on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    start_at = models.DateField("Дата создания", blank=True, default=datetime.today())
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    end_at = models.DateField("Дата завершения", blank=True, default=datetime.today() + timedelta(days=7))

    @property
    def is_wip(self):
        return self.state.code == "WI"

    @property
    def label(self):
        return f'{"WIP: " if self.is_wip else ""}{self.name}'
