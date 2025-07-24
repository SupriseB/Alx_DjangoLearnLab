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