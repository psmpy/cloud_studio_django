from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

from DjangoUeditor.models import UEditorField


class Category(models.Model):
  name = models.CharField('分类', max_length=128)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "博客分类"
    verbose_name_plural = verbose_name
    
class Tag(models.Model):
  name = models.CharField('标签', max_length=128)  

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "博客标签"
    verbose_name_plural = verbose_name

class Blog(models.Model):

  state_choices = (
    ('publish', '发布'),
    ('unpublish', '不发布')
  )

  title = models.CharField('文章标题', max_length=128)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
  img = models.ImageField(upload_to='blog_img/', null=True, blank=True, verbose_name='博客配图', max_length=100)
  body = UEditorField('正文', height=100, width=900, imagePath='uploadimg/', filePath='upload/', toolbars='besttome')
  state = models.CharField('状态', max_length=10, choices=state_choices, default="publish" )
  visits = models.PositiveIntegerField('访问量', default=0)
  comments = models.PositiveIntegerField('评论数', default=0)
  category = models.ForeignKey(Category, verbose_name='博客分类',on_delete=models.CASCADE)
  abstract = models.CharField('摘要', max_length=200, blank=True, default="")
  create_time = models.DateTimeField('创建时间', auto_now_add=True)
  modify_time = models.DateTimeField('修改时间', auto_now=True)

  def __str__(self):
    return self.title
  
  class Meta:
    ordering = ['-create_time']
    verbose_name = '博客'
    verbose_name_plural = verbose_name
 
  @property
  def img_url(self):
    if self.img and hasattr(self.img, 'url'):
      return self.img.url

    