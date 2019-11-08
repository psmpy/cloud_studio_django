#coding=utf-8

from .models import UserProfile
from blog.views import *
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib import auth 
from user.forms import RegisterForm


def get_userprofile(request, username):
  user = UserProfile.objects.get(username=username)
  return render(request, 'user/user_profile.html', locals())


def user_register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    print("current path",request.path)
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)
 
        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()
 
            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()
 
    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'test_register.html', context={'form': form})


def user_login(request): 
  next = request.GET.get('next')
  redirect_to = request.POST.get('next')
  form = RegisterForm()
  if request.method == 'POST':
    
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    print(username,password)
    user = auth.authenticate(username=username, password=password)
    print("认证结果：",user)
    #print(request.session.items())
    #request.session['login_user'] = username
    #request.session['is_login'] = True
    #current_url = request.session.get('path')
    if user:
      print("hello")
      auth.login(request, user)
      print(request.user.username)
      return redirect(redirect_to)
    else:
      return redirect(redirect_to)
  return render(request, 'user/login.html', locals())


def user_logout(request):
  request.session.flush()
  print('hhhhhhhhhhhhhhhhhhhh')
  return redirect('/')