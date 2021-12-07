from django.db import models
from django.conf import settings
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__ (self):
        return self.name

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name

class Movie(models.Model) :
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    poster_path = models.CharField(max_length=500)
    overview = models.TextField()
    vote_average = models.FloatField()
    original_title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    genrename = models.TextField()
    actors = models.ManyToManyField(Actor, related_name = 'movie_actor') 
    actorname = models.TextField()

    def __str__(self):
        return self.title