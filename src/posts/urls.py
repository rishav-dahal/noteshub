# core django imports
from django.urls import path

# app imports
from .views import post_list, post_detail


app_name = 'posts'
urlpatterns = [
        path(
            route = '',
            view  = post_list,
            name  = 'posts_list'),
        path(
            route = '<int:year>/<int:month>/<int:day>/<slug:post_slug>/',
            view  = post_detail,
            name  = 'posts_detail'),
]
