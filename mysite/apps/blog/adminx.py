import xadmin
from .models import Category, Tag, Blog


class CategoryAdmin(object):
  list_display = ['name']

class TagAdmin(object):
  list_display = ['name']

class BlogAdmin(object):
  list_display = ['title', 'author', 'visits', 'create_time']
  list_filter = ['title', 'create_time']
  search_fields = ['title', 'author']
  style_fields = {'body': 'ueditor'}


xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Blog, BlogAdmin)