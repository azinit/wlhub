from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='tasks-list'),
    path('<int:pk>/delete', task_delete, name='tasks-details--delete'),
    path('<int:pk>', task_details, name='tasks-details'),
]
