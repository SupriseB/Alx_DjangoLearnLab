from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Author(models.Model):
    """
    Represents an author in the system.
    Each author can have multiple books associated with them.
    """
    name = models.CharField(max_length=255, help_text="The author's full name.")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book with a title, publication year, and an associated author.
    The 'author' field creates a One-to-Many relationship from Author to Books.
    """
    title = models.CharField(max_length=255, help_text="The title of the book.")
    publication_year = models.IntegerField(help_text="The year the book was published.")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
