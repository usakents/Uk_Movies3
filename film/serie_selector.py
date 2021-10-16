from.models import(Series)

def get_series():
    return Series.objects.all()

def get_serie(serie_id):
    return Series.objects.get(pk=serie_id)
   