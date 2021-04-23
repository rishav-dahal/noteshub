# Core Django imports
from django.shortcuts import render, get_object_or_404

# app imports
from .models import Post


def post_list(request):
    """
    Function view for our home page containing all posts
    """
    template_name = "posts/post_list.html" # <app>/<model>_<viewtype>.html
    context = { 'recent_posts': Post.published.all().order_by('-created') }
    return render(request, template_name, context)

def post_detail(request, year, month, day, post_slug):
    """
    Function view for a single post
    """
    post = get_object_or_404(Post, title_slug=post_slug,
                                   status='published',
                                   created__year=year,
                                   created__month=month,
                                   created__day=day)
    return render(request, template_name='posts/post_detail.html',\
                           context={'post': post} )
