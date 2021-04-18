# Core Django imports
from django.db import models

# package imports
from core.models import TimeStampedModel


class Post(TimeStampedModel):
    """
    Base class to define our Post model and its properties
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    file_field = models.FileField(upload_to='user_uploads/', null=True)

    def __str__(self):
        """
        Returns a representation of a post object,
        which's displayed in admin page
        """
        return self.title

