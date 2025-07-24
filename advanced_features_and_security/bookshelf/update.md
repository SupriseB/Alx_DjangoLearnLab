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