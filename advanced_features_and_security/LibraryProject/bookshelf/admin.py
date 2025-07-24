

from django.contrib import admin
from .models import Book

# Create a custom admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year',)
    search_fields = ('title', 'author')

# Register using the custom admin class
admin.site.register(Book, BookAdmin)
