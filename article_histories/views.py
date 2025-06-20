from rest_framework import viewsets
from .models import ArticleHistory
from .serializers import ArticleHistorySerializer

class ArticleHistoryViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = ArticleHistory.objects.all()
  serializer_class = ArticleHistorySerializer
  lookup_field = 'slug'

  def get_queryset(self):
    slug = self.kwargs.get('slug')
    print(f"Fetching article history for slug: {self.queryset}")
    return self.queryset.filter(article__slug=slug)
