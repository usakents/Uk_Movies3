from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout


from .form import NewUserForm
from.models import(Movies)
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
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("movie")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("movie")