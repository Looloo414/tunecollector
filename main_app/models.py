from django.db import models

# Create your models here.
class Tune(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    length = models.IntegerField()
