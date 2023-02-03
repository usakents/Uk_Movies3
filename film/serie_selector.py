from.models import(Series,Season,Episode)

def get_series():
    return Series.objects.all()

def get_serie(serie_id):
    return Series.objects.get(pk=serie_id)

def get_season_in_serie(serie):
    return Season.objects.filter(serie=serie)

def get_season(season_id):
    return Season.objects.get(pk=season_id)
   
def get_episode_in_season(season):
    return Episode.objects.filter(season=season)
    
def get_episode(episode_id):
    return Episode.objects.get(pk=episode_id)
   