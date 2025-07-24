# views.py
## Using Django ORM with form validation to prevent SQL injection


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm  # You’ll need to create this form if not already done.

# View all books — requires can_view permission
@permission_required('yourapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# Create a new book — requires can_create permission
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# Edit an existing book — requires can_edit permission
@permission_required('yourapp.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form, 'book': book})

# Delete a book — requires can_delete permission
@permission_required('yourapp.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

# SECURITY

from django.shortcuts import render
from .models import Book
from .forms import SearchForm

# Example: Safe search view using ORM and form validation
def search_books(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        title_query = form.cleaned_data['title']
        results = Book.objects.filter(title__icontains=title_query)
    return render(request, 'books/book_search.html', {'form': form, 'results': results})

