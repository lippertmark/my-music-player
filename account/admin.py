from django.contrib import admin
from player.models import Sound, Playlist, Sound_in_Playlist

# Register your models here.
admin.site.register(Sound)
admin.site.register(Playlist)
admin.site.register(Sound_in_Playlist)
