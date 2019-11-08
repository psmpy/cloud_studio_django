# coding: utf-8
from django.urls import path
import xadmin
from . import views

app_name = 'comment'

urlpatterns = [
  path('', views.add_comment, name='add_comment'),
]