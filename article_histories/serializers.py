from rest_framework import serializers
from .models import ArticleHistory

class ArticleHistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ArticleHistory
    fields = ['title', 'description', 'body', 'tags', 'created_at']
    read_only_fields = ['created_at']
