# Core Django imports
from django.shortcuts import render
from django.views.generic import ListView

# app imports
from .models import Post



class HomeView(ListView):
    """
    Class view for our home page
    """
    model = Post
    template_name = "posts/post_home.html" # <app>/<model>_<viewtype>.html
    context_object_name = 'all_posts'
    order_by = 'created' 
