from django_filters import rest_framework as django_filters
from articles.models import Article
from django_filters import rest_framework as filters

class CharInFilter(filters.BaseInFilter, filters.CharFilter):
  pass

class ArticleFilter(django_filters.FilterSet):
  author = django_filters.CharFilter(field_name='author__username', lookup_expr='exact')
  tags = CharInFilter(field_name='tags__name', lookup_expr='in')
  created_at = django_filters.DateFromToRangeFilter()

  class Meta:
    model = Article
    fields = ['author', 'tags', 'created_at']
