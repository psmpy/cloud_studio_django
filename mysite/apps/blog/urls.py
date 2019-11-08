#coding=utf-8
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.index, name='index'),
  path('blog/', views.index, name='index'),
  path('blog/search/', views.blog_search, name="blog_search"),
  path('blog/categorys/', views.category, name="category"),
  path('blog/<path:sort>/<int:pk>/', views.detail, name='detail'),
  path('blog/<path:sort>/', views.sort_index, name='sort_index'),
  
   
]
#print(urlpatterns)