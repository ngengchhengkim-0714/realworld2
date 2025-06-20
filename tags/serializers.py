from rest_framework import serializers
from .models import Tag
from rest_framework.validators import UniqueValidator

class TagSerializer(serializers.ModelSerializer):
  name = serializers.CharField(
    min_length=3,
    max_length=50,
    required=True,
    allow_blank=False,
    validators=[UniqueValidator(queryset=Tag.objects.all())]
  )
  class Meta:
    model = Tag
    fields = ['name']

  def to_internal_value(self, data):
    data = data['tag']
    return super().to_internal_value(data)
