"""UK_Movies_Lib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.conf import settings
from  django.conf.urls.static import  static
from film import views


admin.site.site_header="UK_Movies_Lib project"
admin.site.index_title="UK_Movies"
admin.site.site_title="UK_Movies Ltd"


urlpatterns = [
    path('',views.manage_movie,name="movie"),
    path('mov_details/<int:movie_id>/',views.manage_movie_detail,name='mov_detail'),
    path('seri_details/<int:serie_id>/',views.manage_serie_detail,name='seri_detail'),
    #  path('season_details/<int:season>/',views.manage_season_in_serie,name='season_detail'),
    path('epis_details/<int:episodee_id>/',views.manage_episode_detail,name='epis_detail'),
    path('admin/', admin.site.urls),
    path("Search_items",views.manage_search,name="search_items"),
    path("Search_serie_items",views.manage_serie_search,name="search_serie_items"),
    
    path("signup", views.signup, name= "signup"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("Contact",views.contact_me,name="contact"),
    path("Sub_payment",views. Subscription_payment, name="sub_payment")
     
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

