# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 et wrap tw=76 :

from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val
