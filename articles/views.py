from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from realworld2.permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from .filters import ArticleFilter
from rest_framework.response import Response
from django.db.models import F

class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  filterset_class = ArticleFilter
  serializer_class = ArticleSerializer
  permission_classes = [IsAuthorOrReadOnly]
  lookup_field = 'slug'

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

  def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    if request.user.is_authenticated:
      Article.objects.filter(slug=instance.slug).update(views_count=F('views_count') + 1)
      instance.refresh_from_db()

    serializer = self.get_serializer(instance)
    return Response(serializer.data)
