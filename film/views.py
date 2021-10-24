from django.http import request
from django.shortcuts import render
from django.contrib import messages
from.models import(Movies)

from .form import Register_userForm
from .movie_selector import(get_movie,get_movies)
from .category_selector import(get_category,get_categ)
from .carousel_selector import(get_carousel,get_carous)
from.serie_selector import(get_series,get_serie,get_season_in_serie,get_episode_in_season,get_season)
# Create your views here.

def manage_movie(request):
    get_moviys = get_movies()
    get_categorys=get_category()
    get_carousels=get_carousel()
    get_seriys=get_series()
   
    # Registeruser = Register_userForm()
    # if request.method == "POST":
    #     Registeruser = Register_userForm(request.POST,request.FILES)
    #     if Registeruser.is_valid():
    #         Registeruser.save()
    #         messages.success(request,'user registered successfully')
    #     else:
    #         messages.warning(request,'invalid user input')    
    context={
        "get_moviys":get_moviys,
        "get_categorys":get_categorys,
        "get_carousels":get_carousels,
        "get_seriys":get_seriys
    }
    return render (request,"index.html",context) 
    
def manage_movie_detail(request,movie_id):

    movie_detail=get_movie(movie_id)
    context={
     "movie_detail":movie_detail
    }  
    return render(request,"movie_preview.html",context)

def manage_serie_detail(request,serie_id):
    serie_detail=get_serie(serie_id)
    
    context={
        "serie_detail":serie_detail
       
    }
    return render(request,"serie_preview.html",context)
def manage_season_in_serie(request,serie_id):
    serie = get_serie(serie_id)
    serie_seasons = get_season_in_serie(serie)
    context={
        "serie_seasons":serie_seasons
    }

def manage_episode_in_season(request,season_id):
    season = get_season(season_id)
    episode_season = get_episode_in_season(season)
    context={
        "episode_season":episode_season
    }


      
