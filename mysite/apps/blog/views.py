#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

from functools import wraps


#统计功能，装饰器
def zhandiantongji(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        categorys = Category.objects.all()
        blogs = Blog.objects.filter(state='publish')
        rand_blogs = Blog.objects.filter(state='publish').order_by("?")[:10]
        # print(rand_blogs)
        category_to_blogs ={}
        kwargs['categorys'] = categorys  
        kwargs['blogs'] = blogs
        kwargs['rand_blogs'] = rand_blogs
        for category_ in categorys:
            category_to_blogs[category_.name] = category_.blog_set.filter(state='publish')
        category_to_blogs = sorted(category_to_blogs.items(), key=lambda x:x[1].count(), reverse=True)
        kwargs['category_to_blogs'] = category_to_blogs
        return func(*args, **kwargs)
    return wrapper


@zhandiantongji
def index(request, **kwargs):
    categorys = kwargs.get('categorys', None)
    blogs = kwargs.get('blogs', None)
    rand_blogs = kwargs.get('rand_blogs', None)
    # print(rand_blogs)
    category_to_blogs = kwargs.get('category_to_blogs', None)
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 10)
    try:
        page_blogs = paginator.page(page)
    except EmptyPage:
        page_blogs = paginator.page(1)
    except PageNotInteger:
        page_blogs = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog_index.html', locals())


def detail(request, sort, pk, **kwargs):
    blog = Blog.objects.get(id=pk)
    category = blog.category.name
    #tag = blog.tag.all()[0].name
    return render(request, 'blog/blog_detail.html', locals())


@zhandiantongji
def sort_index(request, sort, **kwargs):
    #右侧栏分类、随机推荐
    category_to_blogs = kwargs.get('category_to_blogs', None)
    rand_blogs = kwargs.get('rand_blogs', None)
    try:
        category = Category.objects.get(name=sort)
        blogs = category.blog_set.filter(state='publish')
    except:
        return render(request, 'blog/blog_502.html', locals())
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 10)
    try:
        page_blogs = paginator.page(page)
    except EmptyPage:
        page_blogs = paginator.page(1)
    except PageNotAnInteger:
        page_blogs = paginator.page(paginator.num_pages)
    #print(locals())
    return render(request, 'blog/blog_index.html', locals())


#搜索
@zhandiantongji
def blog_search(request, **kwargs):
    category_to_blogs = kwargs.get('category_to_blogs', None)
    rand_blogs = kwargs.get('rand_blogs', None)
    if request.method == "GET":
        search_ = request.GET.get('kw', None)  
        #print(search_)
        page_blogs = Blog.objects.filter(title__icontains=search_)
        return render(request, 'blog/blog_search.html', locals())


#按分类归档
@zhandiantongji
def category(request, **kwargs):
    rand_blogs = kwargs.get('rand_blogs', None)
    category_to_blogs = kwargs.get('category_to_blogs', None) 
    return render(request, 'blog/blog_category.html', locals())

  
