from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds bio, profile_picture, and a follow system.
    """
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    # Users this user is following
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',  # reverse relation: user.followers.all()
        blank=True
    )

    def __str__(self):
        return self.username

