from datetime import datetime, timedelta

from django.db import models
from django.db.models import QuerySet

from core.mixins import ModelStrMixin
from dictionaries.models import Subject, Tag
from reports.models import ReportStatus


class TaskState(ModelStrMixin, models.Model):
    """
    Состояние задачи
    :example "В работе", "Провалено", ...
    """

    class Meta:
        verbose_name = "Состояние задачи"
        verbose_name_plural = "Состояния задачи"

    name = models.CharField("Название", max_length=20)
    code = models.CharField("Кодовое обозначение", max_length=2)

    # TODO: add color (secondary, primary, ...)

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

    name = models.CharField("Название", max_length=20)
    value = models.IntegerField("Целочисленное значение приоритета")


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
    state = models.ForeignKey(TaskState, verbose_name="Состояние", on_delete=models.SET_NULL, blank=True, null=True,
                              default=1)
    report_status = models.ForeignKey(ReportStatus, verbose_name="Статус отчетности", on_delete=models.SET_NULL,
                                      null=True)
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

    @classmethod
    def open(cls) -> QuerySet:
        return Task.objects.filter(state__code__in=["IN", "WI", "NW"])

    @classmethod
    def closed(cls) -> QuerySet:
        return Task.objects.filter(state__code__in=["FL", "DN"])
