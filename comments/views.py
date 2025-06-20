from rest_framework import viewsets, permissions
from comments.models import Comment
from comments.serializers import CommentSerializer
from realworld2.permissions import IsAuthorOrReadOnly
from articles.models import Article
from django.shortcuts import get_object_or_404

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [IsAuthorOrReadOnly]

  def get_article(self):
    return get_object_or_404(Article, slug=self.kwargs['article_slug'])

  def perform_create(self, serializer):
    serializer.save(author=self.request.user, article=self.get_article())

  def get_queryset(self):
    return self.queryset.filter(article__slug=self.kwargs['article_slug'])
