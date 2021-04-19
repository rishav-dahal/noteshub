# Core Django imports
from django.shortcuts import render

# app imports
from .models import Post


def home(request):
    """
    Function view for our home page
    """
    template_name = "posts/post_home.html" # <app>/<model>_<viewtype>.html
    context = {
            'all_posts': Post.objects.all().order_by('-created')
            }
    return render(request, template_name, context)
