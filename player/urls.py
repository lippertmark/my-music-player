from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sound/<slug:slug>/', views.show_sound, name='sound'),
    path('playlist/<slug:slug>/', views.playlist, name='playlist')
]