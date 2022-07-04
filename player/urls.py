from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sound/<slug:slug>/', views.show_sound, name='sound'),
    path('sound/<slug:slug>/add_to_playlist/', views.add_sound_to_playlist, name='add_sound_to_playlist'),
    path('playlist/', views.playlist, name='playlist_all'),
    path('playlist/<slug:slug>/', views.playlist, name='playlist'),
    path('add_sound', views.add_sound, name='add_sound'),

]