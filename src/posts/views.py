# Core Django imports
from django.shortcuts import render
from django.views.generic import DetailView

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

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_object(self, queryset=None):
        """
        Return the object based on the kwargs given in the url
        """
        return Post.objects.get(title_slug=self.kwargs.get("title_slug"))
