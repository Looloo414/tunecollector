from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tunes/', views.tunes_index, name='index'),
    path('tunes/<int:tune_id>/', views.tunes_detail, name='detail'),
    path('tunes/create/', views.TuneCreate.as_view(), name='tunes_create'),
    path('tunes/<int:pk>/update/', views.TuneUpdate.as_view(), name='tunes_update'),
    path('tunes/<int:pk>/delete/', views.TuneDelete.as_view(), name='tunes_delete'),
    path('tunes/<int:tune_id>/add_group/', views.add_group, name='add_group'),
]
