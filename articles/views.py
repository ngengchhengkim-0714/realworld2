from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from .filters import ArticleFilter

class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  filterset_class = ArticleFilter
  serializer_class = ArticleSerializer
  permission_classes = [IsAuthorOrReadOnly]
  lookup_field = 'slug'

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)
