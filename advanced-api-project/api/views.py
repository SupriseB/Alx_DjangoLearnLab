from rest_framework import generics, permissions, filters
from django.views.generic import ListView, DetailView, CreateView
from .models import Book
from .serializers import BookSerializer


# ======================================================
# Django REST Framework API VIEWS
# ======================================================

# ============================
# List API View (GET all books)
# ============================
class BookListAPIView(generics.ListAPIView):
    """
    Handles retrieving all books via API.
    Open to unauthenticated users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering


# ============================
# Detail API View (GET one book)
# ============================
class BookDetailAPIView(generics.RetrieveAPIView):
    """
    Handles retrieving a single book by ID via API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ============================
# Create API View (POST new book)
# ============================
class BookCreateAPIView(generics.CreateAPIView):
    """
    Handles creating a new book via API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ============================
# Update API View (PUT/PATCH existing book)
# ============================
class BookUpdateAPIView(generics.UpdateAPIView):
    """
    Handles updating an existing book via API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ============================
# Delete API View (DELETE existing book)
# ============================
class BookDeleteAPIView(generics.DestroyAPIView):
    """
    Handles deleting an existing book via API.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ======================================================
# Django HTML Class-Based Views (ListView, DetailView, CreateView)
# ======================================================

class BookListView(ListView):
    """HTML view for listing books."""
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    """HTML view for displaying a single book."""
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    """HTML view for creating a new book."""
    model = Book
    fields = ['title', 'author', 'publication_year']
    template_name = 'books/book_form.html'
    success_url = '/books/'
