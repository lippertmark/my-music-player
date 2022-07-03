from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import datetime
from mutagen.mp3 import MP3


class Sound(models.Model):
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    file = models.FileField(upload_to='tracks')
    cover_file = models.ImageField(upload_to='track_covers')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)
    text = models.TextField(blank=True)
    uploaded = models.DateField(blank=True, default=datetime.date.today)
    duration = models.TimeField(blank=True, default=datetime.time(0, 0, 0))

    def str_duration(self):
        if self.duration.hour == 0:
            return str(self.duration)[3:]
        return str(self.duration)

    def __str__(self):
        return self.name + ' - ' + self.creator

    def get_absolute_url(self):
        return reverse("sound", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        # TODO сделать уникальными слаги
        self.slug = slugify(self.name)
        self.uploaded = datetime.date.today()
        f = MP3(self.file)
        int_dur = int(f.info.length)
        self.duration = datetime.time(hour=int_dur // (60 * 60), minute=int_dur // 60, second=int_dur % 60)
        super().save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_birthday = models.DateField()


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Sound_in_Playlist(models.Model):
    sound = models.ForeignKey(Sound, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sound) + ' in ' + str(self.playlist)

