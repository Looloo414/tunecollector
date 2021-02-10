from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tune, Group, Instrument
from .forms import GroupForm


# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def tunes_index(request):
    tunes = Tune.objects.all()
    return render(request, 'tunes/index.html', { 'tunes': tunes })
@login_required
def tunes_detail(request, tune_id):
  tune = Tune.objects.get(id=tune_id)
  instruments_tune_doesnt_have = Instrument.objects.exclude(id__in = tune.instruments.all().values_list('id'))
  group_form = GroupForm()
  return render(request, 'tunes/detail.html', { 'tune': tune, 'group_form': group_form, 'instruments': instruments_tune_doesnt_have })

@login_required
def add_group(request, tune_id):
    form = GroupForm(request.POST)
    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.tune_id = tune_id
        new_group.save()
    return redirect('detail', tune_id=tune_id)

@login_required
def assoc_instrument(request, tune_id, instrument_id):
  Tune.objects.get(id=tune_id).instruments.add(instrument_id)
  return redirect('detail', tune_id=tune_id)

@login_required
def unassoc_instrument(request, tune_id, instrument_id):
  Tune.objects.get(id=tune_id).instruments.remove(instrument_id)
  return redirect('detail', tune_id=tune_id)

class TuneCreate(LoginRequiredMixin, CreateView):
  model = Tune
  fields = '__all__'
  success_url = '/tunes/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class TuneUpdate(LoginRequiredMixin, UpdateView):
  model = Tune
  fields = ['song', 'genre', 'length']

class TuneDelete(LoginRequiredMixin, DeleteView):
  model = Tune
  success_url = '/tunes/'

class InstrumentList(LoginRequiredMixin, ListView):
  model = Instrument

class InstrumentDetail(LoginRequiredMixin, DetailView):
  model = Instrument

class InstrumentCreate(LoginRequiredMixin, CreateView):
  model = Instrument
  fields = '__all__'

class InstrumentUpdate(LoginRequiredMixin, UpdateView):
  model = Instrument
  fields = ['name', 'kind']

class InstrumentDelete(LoginRequiredMixin, DeleteView):
  model = Instrument
  success_url = '/instruments/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




