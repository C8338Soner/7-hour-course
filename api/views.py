from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework import viewsets




class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  



# """
# class ArticleViewSet(viewsets.ViewSet):
  
  
#   def list(self, request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(articles, many= True)
#     return Response(serializer.data)
 
#   def create(self, request):
#     serializer = ArticleSerializer(data =request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#   def retrieve(self, request, pk=None):
#     queryset = Article.objects.all()
#     article = get_object_or_404(queryset, pk=pk)
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data)


#   def update(self, request, pk=None):
#     article = Article.objects.get(pk=pk)
#     serializer = ArticleSerializer(article, data = request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#   def destroy(self, request, pk=None):
#     article = Article.objects.get(pk=pk)
#     article.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
# """



#mixins
# class ArticleList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class ArticleDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    
#     lookup_field ='id'

#     def get(self, request, id):
#         return self.retrieve(request, id=id)

#     def put(self, request, id):
#         return self.update(request, id=id)

#     def delete(self, request,id):
#         return self.destroy(request, id=id)


# """
# USED APIView
# class ArticleList(APIView):
#  def get(self, request):
#   articles = Article.objects.all()
#   serializer = ArticleSerializer(articles, many = True)
#   return Response(serializer.data)


#  def post(self, request):
#   serializer = ArticleSerializer(data=request.data)
#   if serializer.is_valid():
#    serializer.save()
#    return Response(serializer.data, status = status.HTTP_201_CREATED)
#   return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# class ArticleDetail(APIView):
#  def get_object(self, id):
#   try:
#    return Article.objects.get(id=id)
#   except Article.DoesNotExist:
#    return Response(status=status.HTTP_404_NOT_FOUND)

#  def get(self, request, id):
#   article = self.get_object(id)
#   serializer = ArticleSerializer(article)
#   return Response(serializer.data)

#  def put(self, request, id):
#   article = self.get_object(id)
#   serializer = ArticleSerializer(article, data=request.data)
#   if serializer.is_valid():
#    serializer.save()
#    return Response(serializer.data)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  def delete(self, request, id):
#      article = self.get_object(id)
#      article.delete()
#      return Response(status=status.HTTP_204_NO_CONTENT)


# """


# """

#  USED FUNCTIONAL VIEW

# @api_view(['GET', 'POST'])
# def article_list(request):
#     # get all articales in

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':

#         serializer = ArticleSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return JsonResponse(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):

#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == 'PUT':

#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# """
