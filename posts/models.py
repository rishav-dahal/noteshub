# Core Django imports
from django.db import models


class Post(models.Model):
    """
    Base class to define our Post model and its properties
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
