# -*- coding: utf-8 -*-
import django
from .views import get_ueditor_controller

DJANGO_VERSION = django.VERSION[:2]

app_name = 'DjangoUeditor'

if DJANGO_VERSION >= (1, 8):
    from django.conf.urls import url
    from django.urls import path

    urlpatterns = [
        url(r'^controller/$', get_ueditor_controller),
        
    ]

else:
    try:
        from django.conf.urls import patterns, url
    except ImportError:
        from django.conf.urls.defaults import patterns, url

    urlpatterns = patterns('',
        url(r'^controller/$', get_ueditor_controller)
    )
