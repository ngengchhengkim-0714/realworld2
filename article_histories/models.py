from django.db import models

class ArticleHistory(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  tags = models.ManyToManyField('tags.Tag', related_name='article_histories', blank=True)
  article = models.ForeignKey('articles.Article', related_name='article_histories', on_delete=models.CASCADE)

  class Meta:
    ordering = ['-created_at']
