"""wlhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import error_404, error_500
from wlhub import settings

# Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="WLHub API",
        default_version='v1',
        description="API для работы с сервисом WLHub",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Routing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    path('comments/', include('comments.urls')),
    path('dictionaries/', include('dictionaries.urls')),
    path('api/', include('api.urls')),
    path('', include('home.urls')),
    # FIXME: temp
    path('debug/404', staff_member_required(error_404), name="debug-404"),
    path('debug/500', staff_member_required(error_500), name="debug-500"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "core.views.error_404"
handler500 = "core.views.error_500"

if settings.DEBUG:
    docs_urls = [
        path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    ]
    urlpatterns += [path('docs/', include(docs_urls))]
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
