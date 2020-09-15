from django.urls import path, re_path
from .views import *

urlpatterns = [
    # path('', task_list, name='comments'),
    re_path(r'^(?P<pk>\d+)/new$', comments_create, name='comment--create'),
    # path('<int:pk>/new', comments_create, name='comment--create'),
    # path('<int:pk>/edit', task_edit, name='tasks:edit'),
    # path('<int:pk>/delete', task_delete, name='tasks:delete'),
    # path('<int:pk>', task_details, name='tasks:view'),
]
