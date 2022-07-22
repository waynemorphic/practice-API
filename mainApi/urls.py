from django.urls import path
from mainApi import views

urlpatterns = [
    path('article', views.ArticlesData.as_view(), name = 'article endpoint'),
    path('article/detail/<int:pk>', views.ArticleDetail.as_view(),name = "article details" )
]