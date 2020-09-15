from django.urls import path, re_path
from .views import *

app_name = "comments"

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/new$', comments_create, name='create'),
    # path('<int:pk>/new', comments_create, name='create'),
]
