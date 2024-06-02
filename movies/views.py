from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
from .models import MovieList

@login_required
def search_movies(request):
    query = request.GET.get('query')
    movies = []
    if query:
        response = requests.get(f'http://www.omdbapi.com/?s={query}&apikey={settings.OMDB_API_KEY}')
        data = response.json()
        movies = data.get('Search', [])
    return render(request, 'search.html', {'movies': movies})

@login_required
def movie_lists(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        movies = request.POST.get('movies').split(',')
        is_public = 'is_public' in request.POST
        MovieList.objects.create(name=name, movies=movies, is_public=is_public, user=request.user)
        return redirect('movie_lists')
    lists = MovieList.objects.filter(user=request.user)
    return render(request, 'movie_lists.html', {'lists': lists})
