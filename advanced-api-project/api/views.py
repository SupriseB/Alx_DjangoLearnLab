from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ============================
# List View (GET all books)
# Accessible to everyone (Read-Only for unauthenticated users)
# ============================
class BookListView(generics.ListAPIView):
    """
    Handles retrieving all books.
    Open to unauthenticated users (read-only).
    Allows searching by title or author name.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']


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
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom create behavior:
        This is where you can attach the current user's related Author profile.
        """
        serializer.save()
        # Example if linking to Author model:
        # serializer.save(author=self.request.user.author_profile)


# ============================
# Update View (PUT/PATCH a book)
# Restricted to authenticated users
# ============================
class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing book.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ============================
# Delete View (DELETE a book)
# Restricted to authenticated users
# ============================
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting a book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
