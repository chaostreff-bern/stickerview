# -*- coding: utf-8 -*-

from django.db import models


class Tag(models.Model):
    name    = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Sticker(models.Model):
    name    = models.CharField(max_length=50)
    image   = models.ImageField(upload_to='stickers')
    tags    = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
