from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets


# Create your views here.
# api/views.py


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer



class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    Supports: list, create, retrieve, update, partial_update, destroy
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
