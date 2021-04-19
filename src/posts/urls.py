# core django imports
from django.urls import path

# app imports
from .views import home


urlpatterns = [
        path(
            route = '',
            view  = home,
            name  = 'posts_home'
            ),
]
