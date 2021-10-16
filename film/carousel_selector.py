from.models import(Carousel)

def get_carousel():
    return Carousel.objects.all()

def get_carous(carous_id):
    return Carousel.get(pk=carous_id)    