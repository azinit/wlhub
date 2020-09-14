from django.db import models
from core.mixins import ModelStrMixin

from django.contrib.auth import get_user_model


# Create your models here.
class Tag(ModelStrMixin, models.Model):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=32)


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
        return f'{self.area} | {self.name}'
