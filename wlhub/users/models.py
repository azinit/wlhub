from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    email = models.EmailField('Email', unique=True)
    thumb = models.ImageField("Аватар пользователя", blank=True, null=True, upload_to="gallery")

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
        from dictionaries.models import Subject
        return Subject.objects.filter(area__user=self)

    @property
    def areas(self):
        from dictionaries.models import Area
        return Area.objects.filter(user=self)

    @property
    def workload(self):
        if not len(self.tasks):
            return '0%'

        percent = len(self.open_tasks) / len(self.tasks) * 100
        fixed = "%.1f" % percent
        return f'{fixed}%'
