from django.urls import path
from .views import task_list, task_details

urlpatterns = [
    path('', task_list, name='tasks-list'),
    path('<int:pk>', task_details, name='tasks-details'),
]
