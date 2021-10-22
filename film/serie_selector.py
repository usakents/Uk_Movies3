from.models import(Series,Season,Episode)

def get_series():
    return Series.objects.all()

def get_serie(serie_id):
    return Series.objects.get(pk=serie_id)

def get_season_in_serie(season):
    return Season.objects.filter(season=season)
   
def get_episode_in_season(season_id):
    pass   
   