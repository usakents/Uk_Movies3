from django.contrib import admin
from django.db import models
from .models import Register_users,Movies,Series,Carousel,Category,Season,Episode
# Register your models here.

admin.site.register(Register_users)
admin.site.register(Movies)
admin.site.register(Series)
admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Episode)
