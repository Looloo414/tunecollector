from django.shortcuts import render
from django.views.generic import CreateView
from .models import Tune


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tunes_index(request):
    tunes = Tune.objects.all()
    return render(request, 'tunes/index.html', { 'tunes': tunes })

def tunes_detail(request, tune_id):
  tune = Tune.objects.get(id=tune_id)
  return render(request, 'tunes/detail.html', { 'tune': tune })

class TuneCreate(CreateView):
  model = Tune
  fields = '__all__'
  success_url = '/tunes/'




# class Tune:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, artist, song, genre, length):
#     self.artist = artist
#     self.song = song
#     self.genre = genre
#     self.length = length

# tunes = [
#   Tune('Avett Brothers', 'Morning Song', 'folk/rock', 3),
#   Tune('Canyon City', 'When I Fell', 'melody', 4),
#   Tune('One Direction', 'History', 'pop', 4)
# ]