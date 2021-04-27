# Core Django imports
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

# app imports
from .models import Post
from .forms import EmailPostForm


class PostListView(ListView):
    """
    Listview for our home page containing all published posts
    """
    # use a specific queryset instead of retrieving all objects
    queryset = Post.published.all()
    context_object_name = 'recent_posts'
    paginate_by = 3
    template_name = "posts/list.html" # <app>/<model>_<viewtype>.html

def post_detail(request, year, month, day, post_slug):
    """
    Function view for a single post
    """
    post = get_object_or_404(Post, title_slug=post_slug,
                                   status='published',
                                   created__year=year,
                                   created__month=month,
                                   created__day=day)
    return render(request, template_name='posts/detail.html',\
                           context={'post': post} )

def post_share(request, post_id):
    """
    Function view to handle the email form and send an email
    """
    # retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        # if a form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # get a dict of valid fields and their value
            clean_data = form.cleaned_data
            # ... send email (left to do)
    else:
        form  = EmailPostForm()
    return render(request, template_name='posts/share.html',\
                           context={'post': post, 'form': form} )
