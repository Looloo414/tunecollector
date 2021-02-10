from django.db import models
from django.urls import reverse

# Create your models here.
PLAYLIST = (
    ('C', 'Country'),
    ('R', 'Rock'),
    ('P', 'Pop'),
    ('H', 'HipHop'),
    ('M', 'Melody'),
)

class Instrument(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('instruments_detail', kwargs={'pk': self.id})

class Tune(models.Model):
    artist = models.CharField(max_length=100)
    song = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    length = models.IntegerField()
    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.artist
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'tune_id': self.id})

class Group(models.Model):
    name = models.CharField(max_length=30)
    playlist = models.CharField(
        max_length=1,
        choices=PLAYLIST,
        default=PLAYLIST[0][0]
    )
    tune = models.ForeignKey(Tune, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_playlist_display()} on {self.name}"



