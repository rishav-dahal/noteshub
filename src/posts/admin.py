# core django imports
from django.contrib import admin

# app imports
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields of the model that are displayed in admin object list
    list_display = ('title', 'title_slug', 'author', 'created')
    list_filter = ('created', 'author') 
    search_fields = ('title', 'description')
    # change how author is displayed (lookup widget instead of drop-down menu)
    raw_id_fields = ('author',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'modified')
    search_fields = ('name', 'email', 'body')

