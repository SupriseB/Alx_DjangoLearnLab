from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

"""
    Represents an author in the blog system.
    Each author is linked to a Django User account.
    Additional author details (e.g., bio, profile picture) can be stored here.
"""
class Author(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_profile"
    )
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
    Represents a blog post with a title, content, publication date, and an associated author.
    The 'author' field creates a One-to-Many relationship from Author to Blog.
"""
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   # track edits
    author = models.ForeignKey(Author, related_name='blogs', on_delete=models.CASCADE)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title} by {self.author.name} on {self.published_date:%Y-%m-%d}"

    def get_absolute_url(self):
        # this allows Django to redirect to the detail page after create/update
        return reverse("blog-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
        
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    tags = TaggableManager()  # NEW

    def __str__(self):
        return self.title
