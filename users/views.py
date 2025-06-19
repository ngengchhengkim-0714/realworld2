from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserProfileSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationView(APIView):
  def post(self, request, *args, **kwargs):
    """
    Handle user registration.
    """
    serializer = RegistrationSerializer(data=request.data['user'])
    if serializer.is_valid():
      serializer.save()
      return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
  def post(self, request, *args, **kwargs):
    """
    Handle user login.
    """
    serializer = LoginSerializer(data=request.data['user'])
    if serializer.is_valid():
      return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
  def get(self, request, username, *args, **kwargs):
    """
    Retrieve user profile by username.
    """
    user = User.objects.filter(username=username).first()

    if not user:
      return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(user)
    return Response({'profile': serializer.data}, status=status.HTTP_200_OK)
