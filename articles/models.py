from django.db import models
from tags.models import Tag
from django.conf import settings
from django.utils.text import slugify

class Article(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)
  description = models.TextField()
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
  views_count = models.PositiveIntegerField(default=0, editable=False)

  class Meta:
    ordering = ['-created_at']

  def save(self, *args, **kwargs):
    if not self.slug:
      base_slug = slugify(self.title)
      slug = base_slug
      i = 1
      while Article.objects.filter(slug=slug).exclude(pk=self.pk).exists():
          slug = f"{base_slug}-{i}"
          i += 1
      self.slug = slug
    super().save(*args, **kwargs)
