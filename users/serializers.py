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

class LoginSerializer(serializers.ModelSerializer):
  token = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = User
    fields = ['username', 'email', 'password', 'token', 'bio', 'image']
    extra_kwargs = {
      'password': {'write_only': True, 'min_length': 8},
      'email': {'required': True, 'allow_blank': False},
      'username': {'required': False, 'allow_blank': True, 'read_only': True},
      'token': {'read_only': True}
    }

  def validate(self, attrs):
    user = User.objects.filter(email=attrs['email']).first()
    if user and user.check_password(attrs['password']):
      return user
    raise serializers.ValidationError("Invalid credentials")

  def get_token(self, obj):
    token = RefreshToken.for_user(obj)
    return str(token.access_token)
