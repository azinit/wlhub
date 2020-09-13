from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .serializers import TagSerializer
from dictionaries.models import Tag


# Create your views here.
class TagsViewSet(viewsets.ModelViewSet):
    """
    list:
    Получить список пользовательских тегов

    create:
    Создать пользовательский тег

    read:
    Получить пользовательский тег

    update:
    Обновить пользовательский тег

    delete:
    Удалить пользовательсий тег
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)
