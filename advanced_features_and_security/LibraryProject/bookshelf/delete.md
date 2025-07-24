# Delete Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
```

## Output:
```python
<QuerySet []>  # Book deleted successfully
```
