from django.urls import path, include
from articles import views

urlpatterns = [
   path('', views.ArticleListview.as_view(), name = 'article_view'),
   path('feed/', views.FeedView.as_view(), name = 'feed_view'),
   path('<int:article_id>/', views.ArticleDetailView.as_view(), name = 'article_datail_view'),
   path('<int:article_id>/comment/', views.CommentView.as_view(), name = 'commnet_view'),
   path('<int:article_id>/comment/<int:comment_id>/', views.CommentDetailView.as_view(), name = 'commnet_detail_view'),
   path('<int:article_id>/like/', views.LikeView.as_view(), name = 'like_view'),  
]   