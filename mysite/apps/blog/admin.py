from django.contrib import admin
from . import models
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  list_display = ['title', 'author', 'visits', 'create_time']


admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Blog, BlogAdmin)