
from .models import Article
from .serializers import ArticleSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class ArticleViewSet(viewsets.ModelViewSet):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  permissions_class = [IsAuthenticated]
  authentication_classes = (TokenAuthentication,)
 


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  

