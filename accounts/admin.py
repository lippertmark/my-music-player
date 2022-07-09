from django.contrib import admin
from player.models import Sound, Playlist, Sound_in_Playlist, TopSound

# Register your models here.
admin.site.register(Sound)
admin.site.register(Playlist)
admin.site.register(Sound_in_Playlist)
admin.site.register(TopSound)
