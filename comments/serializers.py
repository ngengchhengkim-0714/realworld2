from rest_framework import serializers
from comments.models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
  author = UserSerializer(read_only=True)

  class Meta:
    model = Comment
    fields = ['id', 'body', 'created_at', 'updated_at', 'author']
    read_only_fields = ['id', 'author', 'created_at', 'updated_at']
    extra_kwargs = {
      'body': {'required': True},
      'author': {'required': True},
    }

  def to_internal_value(self, data):
    if 'comment' in data:
      data = data['comment']
    return super().to_internal_value(data)
