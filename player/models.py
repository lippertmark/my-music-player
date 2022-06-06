from django.db import models

# Create your models here.

class Track(models.Model):
    name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)

    slug = models.SlugField()