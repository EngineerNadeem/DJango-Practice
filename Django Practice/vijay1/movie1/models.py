from django.db import models

# Create your models here.
#we creat two modols with names Movie and Songs.

class Movie(models.Model):
    actor = models.CharField(max_length=30)
    actor_movie = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    movie_logo = models.CharField(max_length=100)

class Songs(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_name = models.CharField(max_length=100)

