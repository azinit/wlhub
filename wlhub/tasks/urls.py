from django.urls import path
from .views import index, task_details

urlpatterns = [
    path('<int:pk>', task_details, name='tasks-details'),
    path('', index, name='tasks-list'),
]
