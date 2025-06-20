from rest_framework import viewsets, permissions
from .models import Tag
from .serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

  def get_permissions(self):
    if self.action in ['create', 'update', 'destroy']:
      return [permissions.IsAdminUser()]
    return [permissions.AllowAny()]
