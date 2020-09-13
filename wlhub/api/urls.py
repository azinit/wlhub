from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tags-old', TagsAPIView.as_view(), name='api-tags-old'),
    # path('tags', TagsViewSet.as_view(), name='api-tags'),
]

app_name = 'api'
router = DefaultRouter()
router.register(r'tags', TagsViewSet, basename='api-tags')
urlpatterns += router.urls
