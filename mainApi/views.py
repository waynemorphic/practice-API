import imp
from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from mainApi.serializers import ArticleSerializer
from mainApi.models import Article
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, parse

# Create your views here.

class ArticlesData(APIView):
    # GET method
    def get(self, request):
        # serializer queryset
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    
    # POST method    
    def post(self, request, format = None):     
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
            # if not valid
        return Response(serializer.errors)

class ArticleDetail(APIView):
        
    # get a single article depending on their primary key   
    def get(self, request, pk):
        try:
            articles = Article.objects.get(pk = pk)
            serializer = ArticleSerializer(articles)
            return Response(serializer.data)
        
        except Article.DoesNotExist:
            return Response(status = 404)
        
    # alter the details of an article
    def put(self, request, pk):
        articles = Article.objects.get(pk = pk)
        serializer = ArticleSerializer(articles, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    # delete an article
    def delete(self, request, pk):
        articles = Article.objects.get(pk = pk)
        articles.delete()
        return Response(status = 204)
    
            
            
            
