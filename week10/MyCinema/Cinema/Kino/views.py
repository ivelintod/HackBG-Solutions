from django.shortcuts import render
from .models import Movie, Projection


def index(request):
    movies = Movie.objects.all()

    movie_projections = {}

    for movie in movies:
        proj = movie.projection_set.all()
        #proj = Projection.objects.filter(movie_id=movie.id)
        movie_projections[movie] = proj

    return render(request, 'index.html', locals())
