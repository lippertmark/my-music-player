from django.db import models


class AdditionalInformation(models.Model):
    avatar = models.ImageField(default=None)
