# -*- coding: utf-8 -*-

from django.shortcuts import render
from api_v1.models import Sticker, Tag


def index(request):
    stickers    = Sticker.objects.all()
    tags        = Tag.objects.all()
    content = {
        'stickers': stickers,
        'tags': tags,
    }
    return render(
        request,
        'stickers.hbs',
        content,
    )
