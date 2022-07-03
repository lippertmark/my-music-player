from django import forms
from .models import Sound, Sound_in_Playlist, Playlist


class AddSoundForm(forms.ModelForm):
    class Meta:
        model = Sound
        fields = ['name', 'creator', 'file', 'cover_file', 'text']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'text_input',
            }),
            'creator': forms.TextInput(attrs={
                'placeholder': 'Creator',
                'class': 'text_input',
            }),
            'file': forms.FileInput(attrs={

            }),
            'cover_file': forms.FileInput(attrs={

            }),
            'text': forms.Textarea(attrs={
                'placeholder': 'Text',
                'class': 'text_input',
            })
        }


class SoundInPlaylistForm(forms.ModelForm):
    class Meta:
        model = Sound_in_Playlist
        fields = ['playlist', 'sound']


class PLaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'text_input'
            })
        }
