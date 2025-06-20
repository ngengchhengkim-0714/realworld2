from django.db import models
from django.conf import settings
from articles.models import Article

class Comment(models.Model):
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
  article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

  class Meta:
    ordering = ['-created_at']
