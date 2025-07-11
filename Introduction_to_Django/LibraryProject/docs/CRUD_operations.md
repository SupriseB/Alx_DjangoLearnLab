# CRUD Operations Summary

This file summarizes all the Create, Retrieve, Update, and Delete operations performed in the Django shell using the `Book` model.

# Create Operation

## Command:
```python
from book_store.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
```

## Output:
```python
<Book: 1984>  # Book instance created successfully
```

# Retrieve Operation

## Command:
```python
from book_store.models import Book
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```

## Output:
```python
1984 George Orwell 1949  # Retrieved book details
```

# Update Operation

## Command:
```python
from book_store.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
```

## Output:
```python
Nineteen Eighty-Four  # Title updated successfully
```

# Delete Operation

## Command:
```python
from book_store.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
```

## Output:
```python
<QuerySet []>  # Book deleted successfully
```

All operations were executed successfully via the Django shell.
