from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

"""
    Represents an author in the blog system.
    Each author is linked to a Django User account.
    Additional author details (e.g., bio, profile picture) can be stored here.
"""
class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="author_profile")
    name = models.CharField(max_length=255, help_text="The author's full name")
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    def __str__(self):
        return self.name or self.user.username
    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


"""
    Represents a blog with a title, content, publication date, and an associated author.
    The 'author' field creates a One-to-Many relationship from Author to Blogs.
"""
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, related_name='blogs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name} on {self.published_date:%Y-%m-%d}"
