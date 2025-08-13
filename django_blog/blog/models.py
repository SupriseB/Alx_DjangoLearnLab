from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
    Represents an author in the blog system.
    Each author can have multiple blogs associated with them.
"""
class Author(models.Model):
    name= models.CharField(max_length=255, help_text="The authors full name")

    def __str__(self):
        return self.name

"""
    Represents a blog with a title, content,publication date, and an associated author.
    The 'author' field creates a One-to-Many relationship from Author to Blogs.
"""
class Blog(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='blog', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name} on {self.published_date:%Y-%m-%d}"

