# -*- coding: utf-8 -*-

from django.contrib import admin
from api_v1 import models


admin.site.register(models.Tag)
admin.site.register(models.Sticker)
