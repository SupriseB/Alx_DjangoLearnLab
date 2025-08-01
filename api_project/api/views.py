from django.shortcuts import render
from rest_framework import generics
from .models import Book 
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
# api/views.py

"""A ViewSet for viewing and editing Book instances.Supports: list, create, retrieve, update, partial_update, destroy"""
   

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all() # Retrieve all books
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # only logged-in users can access
