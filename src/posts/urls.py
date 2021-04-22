# core django imports
from django.urls import path

# app imports
from .views import post_list, PostDetailView


app_name = 'posts'
urlpatterns = [
        path(
            route = '',
            view  = post_list,
            name  = 'posts_home'),

        path(
            route = 'posts/<slug:title_slug>/',
            view  = PostDetailView.as_view(),
            name  = 'posts_detail')
]
