from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework


# ============================
# List View (GET all books)
# Accessible to everyone (Read-Only for unauthenticated users)
# Supports search and ordering via query parameters
# ============================
class BookListView(generics.ListAPIView):
    """
    Handles retrieving all books.
    Open to unauthenticated users (read-only).
    Allows searching by title or author name.
    Allows ordering by title or publication year.

    Query params examples:
    - Search: ?search=django
    - Order ascending: ?ordering=title
    - Order descending: ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


# ============================
# Detail View (GET a single book by ID)
# Accessible to everyone (Read-Only for unauthenticated users)
# ============================
class BookDetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single book by its ID.
    Open to unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ============================
# Create View (POST a new book)
# Restricted to authenticated users
# ============================
class BookCreateView(generics.CreateAPIView):
    """
    Handles creating a new book.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class =_
