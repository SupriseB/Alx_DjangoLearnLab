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

def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # <-- updated line
        print(f"Librarian for library '{library_name}': {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library named {library_name} found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to library '{library_name}'.")


if __name__ == "__main__":
    # Example usage:
    query_books_by_author("J.K. Rowling")
    list_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
