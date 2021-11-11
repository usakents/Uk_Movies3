from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField

# Create your models here.

class Register_users(models.Model):
    User_name=models.CharField(max_length=200,null=False)
    Email=models.EmailField()
    password=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

class Movies(models.Model):
    movie_title=models.CharField(max_length=200,null=False)
    movie_actor=models.CharField(max_length=200,null=False)
    movie_general=models.CharField(max_length=300,null=False)
    movie_VJ=models.CharField(max_length=200)
    movie_cost=models.CharField(max_length=300)
    STATUS1_TYPE_CHOICES=[
        ('New','New'),
        ('Featured','Featured')
    ]
    movie_status1=models.CharField(max_length=300,null=False,choices=STATUS1_TYPE_CHOICES)
    STATUS2_TYPE_CHOICES=[
        ('Free','Free'),
        ('Paid','Paid')
    ]
    movie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    movie_release_date=models.DateField(auto_now_add=True)
    movie_image=models.ImageField(upload_to='pic')
    movie_video=models.FileField(upload_to='m_videos')

class Series(models.Model):
    serie_title=models.CharField(max_length=200,null=False)
    serie_actor=models.CharField(max_length=200,null=False)
    serie_general=models.CharField(max_length=300,null=False)
    serie_VJ=models.CharField(max_length=200)
    serie_cost=models.CharField(max_length=200)
    # serie_cost=models.CharField(max_length=200, verbose_name="Omuwendo")
  
    STATUS1_TYPE_CHOICES=[
      
        ('New','New'),
        ('Featured','Featured')
    ]
    serie_status1=models.CharField(max_length=300,null=False,choices=STATUS1_TYPE_CHOICES)
    STATUS2_TYPE_CHOICES=[
        ('Free','Free'),
        ('Paid','Paid')
    ]
    serie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    serie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    serie_release_date=models.DateField(auto_now_add=True)
    serie_image=models.ImageField(upload_to='pic')
    

class Season(models.Model):
    season_name=models.CharField(max_length=200)
    serie=models.ForeignKey(Series,on_delete=CASCADE)
    release_date=models.DateField()
    description=models.CharField(max_length=1000)

class Episode(models.Model):
    episode_name=models.CharField(max_length=200)
    season=models.ForeignKey(Season,on_delete=CASCADE)
    release_date=models.DateField()
    description=models.CharField(max_length=1000,null=True, blank=True)
    episode_video=models.FileField(upload_to='s_videos')


class Carousel(models.Model):
    image_name=models.CharField(max_length=200)
    carousel_image=models.ImageField(upload_to='pic')

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    





    


