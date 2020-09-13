from django.urls import path
from .views import *

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks-list'),
    path('new', task_create, name='tasks-details--create'),
    path('<int:pk>/edit', task_edit, name='tasks-details--edit'),
    path('<int:pk>/delete', task_delete, name='tasks-details--delete'),
    path('<int:pk>', task_details, name='tasks-details'),
]
