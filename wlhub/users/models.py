from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.mixins import ModelStrMixin


class SiteUser(AbstractUser):
    email = models.EmailField('Email', unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    @property
    def tasks(self):
        from tasks.models import Task
        return Task.objects.filter(subject__area__user=self)

    @property
    def open_tasks(self):
        from tasks.models import Task
        return Task.open().filter(subject__area__user=self)

    @property
    def closed_tasks(self):
        from tasks.models import Task
        return Task.closed().filter(subject__area__user=self)

    @property
    def subjects(self):
        from tasks.models import Subject
        return Subject.objects.filter(area__user=self)

    @property
    def areas(self):
        from tasks.models import Area
        return Area.objects.filter(user=self)

    @property
    def workload(self):
        # TODO: impl
        return '80%'


class Tag(ModelStrMixin, models.Model):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=16)
