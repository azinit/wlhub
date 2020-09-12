from django.contrib.auth.models import AbstractUser
from django.db import models


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
        from dictionaries.models import Subject
        return Subject.objects.filter(area__user=self)

    @property
    def areas(self):
        from dictionaries.models import Area
        return Area.objects.filter(user=self)

    @property
    def workload(self):
        # TODO: impl
        return '80%'
