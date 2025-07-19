import django
import os

# Setup Django environment for standalone script
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author named {author_name} found.")

def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")

LibraryProject/relationship_app/query_samples.py doesn't contain: ["Librarian.objects.get(library="]

if __name__ == "__main__":
    # Example usage:
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
