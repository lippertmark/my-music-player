from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sound, Playlist, Sound_in_Playlist
from django.conf import settings
from .forms import AddSoundForm, PLaylistForm, Sound_in_Playlist
from django.views.generic import CreateView


def playlist(request, slug=None):
    if slug is None:
        music = Sound.objects.all()
        return HttpResponse('вся музыка')
    else:
        playlist = get_object_or_404(Playlist, slug=slug)
        sounds = Sound_in_Playlist.objects.filter(playlist=playlist)
        data = {
            'name': playlist.name,
            'sounds': sounds,
        }
        return render(request, template_name='player/playlist.html', context=data)


def show_sound(request, slug):
    sound = get_object_or_404(Sound, slug=slug)
    data = {
        'sound': sound,
    }
    return render(request, 'player/sound.html', context=data)
    return HttpResponse(sound.name)


def add_sound(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = AddSoundForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Все оки) все создано')
    else:
        form = AddSoundForm()

    return render(request, 'player/add_sound.html', context={'form': form})


def add_playlist(request):
    if request.method == 'POST':
        form = PLaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Все оки) все создано')
    else:
        form = PLaylistForm()
    #return render(request)
