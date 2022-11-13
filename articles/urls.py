from django.urls import path, include
from Articles import views

urlpatterns = [
    path('', views.articleAPI.as_view()),
    path('<int:article_id>/', views.ArticleDetail.as_view(), name = "article_view")
]
