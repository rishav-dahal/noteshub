# Core Django imports
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

# app imports
from .models import Post


class PostListView(ListView):
    """
    Listview for our home page containing all published posts
    """
    # use a specific queryset instead of retrieving all objects
    queryset = Post.published.all()
    context_object_name = 'recent_posts'
    paginate_by = 3
    template_name = "posts/post_list.html" # <app>/<model>_<viewtype>.html

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
