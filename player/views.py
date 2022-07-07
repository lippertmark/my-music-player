from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Sound, Playlist, Sound_in_Playlist
from django.conf import settings
from .forms import AddSoundForm, PlaylistForm, Sound_in_Playlist, AddSoundToPlaylist, AddSoundToPlaylistFromPlaylist
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


@login_required
def playlist(request, slug=None):
    if slug is None:
        sounds = Sound.objects.all()
        data = {
            'name': 'All sounds',
            'sounds': sounds,
        }
        return render(request, template_name='player/playlist.html', context=data)
    else:
        playlist = get_object_or_404(Playlist, slug=slug)
        if request.method == 'POST':
            form = AddSoundToPlaylistFromPlaylist(request.POST)
            if form.is_valid():
                form.instance.playlist = playlist
                form.save()
        sounds = map(lambda x:x.sound,Sound_in_Playlist.objects.filter(playlist=playlist))
        data = {
            'name': playlist.name,
            'sounds': sounds,
            'add_to_playlist': AddSoundToPlaylistFromPlaylist(),
        }
        return render(request, template_name='player/playlist.html', context=data)


@login_required
def show_sound(request, slug):
    sound = get_object_or_404(Sound, slug=slug)
    data = {
        'sound': sound,
        'add_to_playlist': AddSoundToPlaylist(),
    }
    if request.method == 'POST':
        if 'playlist' in request.POST:
            form = AddSoundToPlaylist(request.POST)
            if form.is_valid():
                form.instance.sound = sound
                form.save()
    return render(request, 'player/sound.html', context=data)


@login_required
def add_sound_to_playlist(request, slug):
    if request.method == "POST":
        sound = get_object_or_404(Sound, slug=slug)


@login_required
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


@login_required
def add_playlist(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Все оки) все создано')
    else:
        form = PlaylistForm()
    # return render(request)


@login_required
def profile(request):
    return render(request, 'player/profile.html', {'user': request.user})
