from django.contrib.auth import get_user_model
from django.db import models

from core.mixins import ModelStrMixin


# Create your models here.
class Report(models.Model):
    """
    Отчет по задачам, нагруженности
    """

    class Meta:
        verbose_name = "Отчет по задачам"
        verbose_name_plural = "Отчеты по задачам"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField("Дата отчета", auto_now=True)


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
