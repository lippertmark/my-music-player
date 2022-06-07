from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Sound(models.Model):
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    file = models.FileField(upload_to='tracks')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)

    def get_absolute_url(self):
        return reverse("sound", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
