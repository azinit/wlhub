from django.contrib.auth import get_user_model
from django.db import models


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
