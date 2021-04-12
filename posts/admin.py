# core django imports
from django.contrib import admin

# app imports
from .models import Post

admin.site.register(Post)
