from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tunes_index(request):
  return render(request, 'tunes/index.html', { 'tunes': tunes })

class Tune:  # Note that parens are optional if not inheriting from another class
  def __init__(self, artist, song, genre, length):
    self.artist = artist
    self.song = song
    self.genre = genre
    self.length = length

tunes = [
  Tune('Avett Brothers', 'Morning Song', 'folk/rock', 3),
  Tune('Canyon City', 'When I Fell', 'melody', 4),
  Tune('One Direction', 'History', 'pop', 4)
]