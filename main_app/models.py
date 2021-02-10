from django.db import models
from django.urls import reverse

# Create your models here.


class Tune(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    length = models.IntegerField()

    def __str__(self):
        return self.artist
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tune_id': self.id})

class Instrument(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
