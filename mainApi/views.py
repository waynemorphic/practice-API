from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from mainApi.serializers import ArticleSerializer
from mainApi.models import Article
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, parse
from rest_framework import status
# Create your views here.

class ArticlesData(APIView):
    # GET method
    def get(self, request):
        # serializer queryset
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    # POST method    
    def post(self, request, format = None):     
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
            
            # if not valid
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):        
    # get a single article depending on their primary key   
    def get(self, request, pk):
        try:
            articles = Article.objects.get(pk = pk)
            serializer = ArticleSerializer(articles)
            return Response(serializer.data)
        
        except Article.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    # alter the details of an article
    def put(self, request, pk):
        articles = Article.objects.get(pk = pk)
        serializer = ArticleSerializer(articles, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)
        
    # delete an article
    def delete(self, request, pk):
        articles = Article.objects.get(pk = pk)
        articles.delete()
        return Response(status = status.HTTP_202_ACCEPTED)
    
            
            
            
