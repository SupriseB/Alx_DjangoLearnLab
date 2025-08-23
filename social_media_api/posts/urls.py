from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed  # Import feed view

# DRF router for posts and comments
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

# URL patterns
urlpatterns = [
    path('feed/', feed, name='feed'),  # Feed endpoint
]

# Include router URLs
urlpatterns += router.urls
