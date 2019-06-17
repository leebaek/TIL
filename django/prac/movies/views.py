from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    context = {'movies':movies}
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        title_origin = request.POST.get('title_origin')
        vote_count = request.POST.get('vote_count')
        open_date = request.POST.get('open_date')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        poster_url = request.POST.get('poster_url')
        description = request.POST.get('description')
        movie = Movie(title=title, title_origin=title_origin, vote_count=vote_count, open_date=open_date,
                      genre=genre, score=score, poster_url=poster_url, description=description)
        movie.save()
        return redirect('movies:index')
    else:
        return render(request, 'movies/create.html')