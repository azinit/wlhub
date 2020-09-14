from django.core.exceptions import PermissionDenied


def validate_task_access(user, task):
    """
    Валидация: Имеет ли пользователь доступ к задаче
    """
    if task.user != user:
        raise PermissionDenied()
