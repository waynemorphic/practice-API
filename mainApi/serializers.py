from dataclasses import fields
from rest_framework import serializers
from mainApi.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:        
        model = Article
        fields = ["title", "author","email"]
    