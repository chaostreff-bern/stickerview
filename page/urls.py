# -*- coding: utf-8 -*-

from django.conf.urls import url
from page import views


urlpatterns = [
    url(r'^$',              views.index),
]
