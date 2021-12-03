import django_filters
from django_filters import CharFilter,DateFilter
from .models import Movies

class Movie_filter(django_filters.FilterSet):
    start_date = DateFilter(field_name="movie_release_date",lookup_expr='gte')
    end_date = DateFilter(field_name="movie_release_date",lookup_expr='lte')
    movie_title = django_filters.CharFilter(lookup_expr='icontains')
    movie_VJ = django_filters.CharFilter(lookup_expr='icontains')
    # movie_title = CharFilter(field_name="movie_title", lookup_expr='icontains')
    class Meta:
        model = Movies
        fields = ['movie_title','movie_general','movie_VJ','movie_cost','movie_status1','movie_release_date']
        # exclude =['movie_general']
       
    

    