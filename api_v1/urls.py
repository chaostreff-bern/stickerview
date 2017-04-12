# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework.routers import SimpleRouter
from api_v1 import views


r = SimpleRouter(trailing_slash=settings.APPEND_SLASH)

r.register(r'tags',     views.TagViewSet,       'tags')
r.register(r'stickers', views.StickerViewSet,   'stickers')

urlpatterns = [
]

urlpatterns.extend(r.urls)
