# Core Django imports
from django.db import models


class Post(models.Model):
    """
    Base class to define our Post model and its properties
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        """
        Returns a representation of a post object,
        which's displayed in admin page
        """
        return self.title
