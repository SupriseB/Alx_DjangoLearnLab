# ============================
# Update View (PUT/PATCH an existing book)
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
# Delete View (DELETE an existing book)
# Restricted to authenticated users
# ============================
class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting an existing book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

