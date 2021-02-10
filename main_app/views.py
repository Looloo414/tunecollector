from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Tune
from .forms import GroupForm


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
  group_form = GroupForm()
  return render(request, 'tunes/detail.html', { 'tune': tune, 'group_form': group_form })

class TuneCreate(CreateView):
  model = Tune
  fields = '__all__'
  success_url = '/tunes/'

class TuneUpdate(UpdateView):
  model = Tune
  fields = ['song', 'genre', 'length']

class TuneDelete(DeleteView):
  model = Tune
  success_url = '/tunes/'




