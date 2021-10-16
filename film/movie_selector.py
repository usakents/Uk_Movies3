from.models import(Movies)

def get_movies():
    return Movies.objects.all()

def get_movie(movie_id):
    return Movies.objects.get(pk=movie_id)
   
