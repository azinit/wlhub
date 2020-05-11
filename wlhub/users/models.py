from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from core.mixins import ModelStrMixin


class SiteUser(AbstractUser):
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Tag(ModelStrMixin, models.Model):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=16)
