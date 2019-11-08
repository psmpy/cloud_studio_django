# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Comments


def add_comment(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      print(request.user.username)
      return HttpResponse("no register!")
    else:
      comment = Comments()
      comment.content = request.POST.get('content', '')
      comment.repler = request.user.username

      print(request.POST)
      print(request.user.pk)
      return redirect('a/')
