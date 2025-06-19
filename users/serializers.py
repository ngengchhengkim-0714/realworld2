from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'bio', 'image']


class RegistrationSerializer(serializers.ModelSerializer):
  token = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'bio', 'image', 'token']
    extra__kwargs = {
      'password': {'write_only': True, 'min_length': 8},
      'email': {'required': True, 'allow_blank': False}
    }

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user

  def get_token(self, obj):
    token = RefreshToken.for_user(obj)
    return str(token.access_token)
