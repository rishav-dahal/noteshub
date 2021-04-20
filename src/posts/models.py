# Core Django imports
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# package imports
from core.models import TimeStampedModel

class PublishedManager(models.Manager):
    """
    Custom manager to retrieve all posts that have published status
    """
    def get_queryset(self):
        """
        Modify the default queryset to include our custom filter
        """
        return super(PublishedManager,\
                     self).get_queryset()\
                    .filter(status='published')

class Post(TimeStampedModel):
    """
    Base class to define our Post model and its properties
    """
    STATUS_CHOICES = (
            # <actual_value>, <what_it's_displayed_as>
            ('draft', 'Draft'),
            ('published', 'Published'),
            )
    title = models.CharField(max_length=50)
    title_slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(max_length=200)
    file_field = models.FileField(upload_to='user_uploads/', null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='draft')
    # our custom manager
    published = PublishedManager()
    # we'll also keep the default `objects` manager
    objects = models.Manager()

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        """ 
        Override the default save function to add a slug from the title
        """
        # if there's no slug provided then assign a slug using the object's name
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a representation of a post object,
        which's displayed in admin page
        """
        return self.title
    
