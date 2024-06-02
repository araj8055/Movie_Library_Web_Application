from django.urls import path
from .views import search_movies, movie_lists

urlpatterns = [
    path('search/', search_movies, name='search_movies'),
    path('lists/', movie_lists, name='movie_lists'),
]
