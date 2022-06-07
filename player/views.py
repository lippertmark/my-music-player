from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sound, Playlist
from django.conf import settings

def playlist(request, slug):
    return HttpResponse(slug)


def show_sound(request, slug):
    sound = get_object_or_404(Sound, slug=slug)
    data = {
        'BASE_URL': settings.BASE_DIR,
        'MEDIA_URL': settings.MEDIA_URL,
        'sound': sound,
    }
    return render(request, 'player/sound.html', context=data)
    return HttpResponse(sound.name)
