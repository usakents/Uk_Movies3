from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.admin.views.decorators import staff_member_required



from .form import NewUserForm
from .filters import Movie_filter
from .filters import  Movie_title_filter
from .filters import Serie_filter
from .filters import Serie_title_filter
from.models import(Movies)
from .movie_selector import(get_movie,get_movies)
from .category_selector import(get_category,get_categ)
from .carousel_selector import(get_carousel,get_carous)
from.serie_selector import(get_series,get_serie,get_season_in_serie,get_episode_in_season,get_season)

# Create your views here.
# @login_required(login_url='login')
def manage_movie(request):
    get_moviys = get_movies()
    get_categorys=get_category()
    get_carousels=get_carousel()
    get_seriys=get_series()

    user_filter = Movie_filter(request.GET, queryset=get_moviys)

    get_moviy_title_filter =  Movie_title_filter(request.GET, queryset=get_moviys)

    user_series_filter = Serie_filter(request.GET, queryset=get_seriys)
    
    get_serititle_filter =  Serie_title_filter(request.GET, queryset=get_seriys)
   
   
    context={
        "user_filter":user_filter,
        "get_categorys":get_categorys,
        "get_carousels":get_carousels,
        "get_seriys":get_seriys,
        "get_moviy_title_filter":get_moviy_title_filter,
        "user_series_filter":user_series_filter,
        "get_serititle_filter":get_serititle_filter
    }
    return render (request,"index.html", context) 

# @staff_member_required(login_url='signup')
# @login_required(login_url='login')
@user_passes_test(lambda u: u.is_staff, login_url='sub_payment')
@user_passes_test(lambda u: u.is_superuser, login_url='sub_payment')
@user_passes_test(lambda u: u.groups.filter(name='free').exists(),login_url='sub_payment')     
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

def manage_search(request):
    get_moviys = get_movies()
   

    user_filter = Movie_filter(request.GET, queryset=get_moviys)
   
  
    context={
        "user_filter":user_filter,
       
    }
    return render (request,"search.html", context) 

def manage_serie_search(request):
    get_seriys=get_series()

    
    user_series_filter = Serie_filter(request.GET, queryset=get_seriys)

    context={
         "user_series_filter":user_series_filter
    }
    return render (request,"serie_search.html", context) 

# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("movie")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="register.html", context={"register_form":form})

# def login_request(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'Invalid Credentials')
#             return redirect('login')
    
#     else:
#         return render (request,'login.html')  

def signup(request):
    form = NewUserForm()
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Registered successfully'+user)
            return redirect("login")

    context={
        "form":form
    }
    return render(request, "signup.html",context)    

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('movie')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html')      

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("movie")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")

def contact_me(request):
 return render(request, 'contact.html')

def Subscription_payment(request):
 return render(request, 'subscription1.html')
