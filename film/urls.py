from django.urls import path
from . import views


urlpatterns = [
    path('',views.manage_movie,name="movie"),
    path('mov_details/<int:movie_id>/',views.manage_movie_detail,name='mov_detail'),
    path('seri_details/<int:serie_id>/',views.manage_serie_detail,name='seri_detail'),
    #  path('season_details/<int:season>/',views.manage_season_in_serie,name='season_detail'),
    path("Search_items",views.manage_search,name="search_items"),
    path("Search_serie_items",views.manage_serie_search,name="search_serie_items"),
    path('epis_details/<int:episode_id>/',views.manage_episode_detail,name='epis_detail'),
    
    path("Actions",views.get_action,name="actions"),

    path("signup", views.signup, name= "signup"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("Contact",views.contact_me,name="contact"),
    path("Sub_payment",views. Subscription_payment, name="sub_payment"),     
    
]
