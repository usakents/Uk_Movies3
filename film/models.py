from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User


# Create your models here.

class Register_users(models.Model):
    User_name=models.CharField(max_length=200,null=False)
    Email=models.EmailField()
    password=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)

class Movies(models.Model):
    movie_title=models.CharField(max_length=200,null=False)
    movie_actor=models.CharField(max_length=200,null=False)
    CATEGORY_CHOICES=[
        ('ACTION','ACTION'),
        ('HORROR','HORROR'),
        ('SCIENCE FRICTION','SCIENCE FRICTION'),
        ('LOVE STORY','LOVE STORY'),
        ('INDIAN','INDIAN'),
        ('COMEDY','COMEDY')
    ]
    movie_genre=models.CharField(max_length=300,null=False,choices=CATEGORY_CHOICES,default='ACTION')
    movie_VJ=models.CharField(max_length=200)
    movie_cost=models.CharField(max_length=300)
    STATUS1_TYPE_CHOICES=[
        ('New','New'),
        ('Featured','Featured')
    ]
    movie_status1=models.CharField(max_length=300,null=False,choices=STATUS1_TYPE_CHOICES,default='New')
    STATUS2_TYPE_CHOICES=[
        ('Free','Free'),
        ('Paid','Paid')
    ]
    movie_status2=models.CharField(max_length=200,choices=STATUS2_TYPE_CHOICES)
    movie_release_date=models.DateField(auto_now_add=True)
    movie_image=models.ImageField(upload_to='pic')
    movie_video=models.FileField(upload_to='m_videos')

    def __str__(self):
        return self.movie_title

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
    
class Plan(models.Model):
    plan_name=models.CharField(max_length=200)
    plan_amount=models.CharField(max_length=100)

class Subscription(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    plan=models.ForeignKey(Plan,on_delete=CASCADE)
    STATUS_TYPE_CHOICES=[
        ('PAID','PAID'),
        ('FREE','FREE')
    ]
    subscription_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)    
    






    


