from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields from the Book model.
    Includes custom validation to ensure 'publication_year' is not in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model including nested representation of related books.
    Uses the BookSerializer to serialize 'books' dynamically.
    """
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['name', 'books']
