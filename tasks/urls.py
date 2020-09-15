from django.urls import path
from .views import *

app_name = "tasks"

urlpatterns = [
    path('', TasksListView.as_view(), name='list'),
    path('new', task_create, name='create'),
    path('<int:pk>/edit', task_edit, name='edit'),
    path('<int:pk>/delete', task_delete, name='delete'),
    path('<int:pk>', task_details, name='details'),
]
