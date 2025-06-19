from rest_framework import serializers
from .models import Article
from tags.models import Tag
from users.serializers import UserSerializer

class ArticleSerializer(serializers.ModelSerializer):
  tags = serializers.SlugRelatedField(
    many=True,
    slug_field='name',
    queryset=Tag.objects.all()
  )
  author = UserSerializer(read_only=True)

  class Meta:
    model = Article
    fields = ['title', 'slug', 'description', 'body', 'author', 'tags', 'created_at', 'updated_at']
    read_only_fields = ['author', 'created_at', 'updated_at', 'slug']

  def to_internal_value(self, data):
    if 'article' in data:
      data = data['article']
    return super().to_internal_value(data)
