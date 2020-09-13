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
    def tags(self):
        from dictionaries.models import Tag
        return Tag.objects.filter(user=self)

    @property
    def has_survey_voice(self):
        return len(self.surveys.all()) > 0

    @property
    def workload(self):
        if not len(self.tasks):
            return '0%'

        percent = len(self.open_tasks) / len(self.tasks) * 100
        fixed = "%.1f" % percent
        return f'{fixed}%'


class UserSurvey(models.Model):
    """
    Анкета от пользователя
    """

    class Meta:
        verbose_name = "Анкета от пользователя"
        verbose_name_plural = "Анкеты от пользователей"

    user = models.ForeignKey(SiteUser, verbose_name="Пользователь", on_delete=models.DO_NOTHING, related_name="surveys")
    is_student = models.BooleanField("Являюсь Студентом")
    is_employee = models.BooleanField("Являюсь Сотрудником компании")
    is_employer = models.BooleanField("Являюсь Учредителем компании")
    is_manager = models.BooleanField("Являюсь Менеджером")
    is_freelancer = models.BooleanField("Являюсь Фрилансером")
    rate = models.IntegerField("Оценка сервиса")

    def __str__(self):
        return f'{self.user} ({self.rate}/5)'
