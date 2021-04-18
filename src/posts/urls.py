# core django imports
from django.urls import path

# app imports
from .views import HomeView


urlpatterns = [
        path(
            route = '',
            view  = HomeView.as_view(),
            name  = 'posts_home'
            ),
]
