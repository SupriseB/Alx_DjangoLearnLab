# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the previous list view (if still needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Include all router URLs
    path('', include(router.urls)),
]



