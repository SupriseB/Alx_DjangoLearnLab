from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post  # Import like/unlike views

# DRF router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# URL patterns
urlpatterns = [
    path('feed/', feed, name='feed'),               # Feed endpoint
    path('posts/<int:post_id>/like/', like_post, name='like-post'),   # Like a post
    path('posts/<int:post_id>/unlike/', unlike_post, name='unlike-post'), # Unlike a post
    path('"<int:pk>/like/", "<int:pk>/unlike/"),
]

# Include router URLs
urlpatterns += router.urls
