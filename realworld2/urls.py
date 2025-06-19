"""
URL configuration for realworld2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from users.views import UserRegistrationView, UserLoginView, UserProfileView, UserDetailView
from tags.views import TagViewSet
from articles.views import ArticleViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
	path('admin/', admin.site.urls),
	path('users/', UserRegistrationView.as_view(), name='user_registration'),
	path('users/login/', UserLoginView.as_view(), name='user_login'),
    path('user/', UserDetailView.as_view(), name='user_update'),
    path('profiles/<str:username>/', UserProfileView.as_view(), name='user_profile'),
]
