from django.db import models
from blog.models import Blog
from django.conf import settings

from DjangoUeditor.models import UEditorField

class Comments(models.Model):
  blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog", blank=True, null=True)
  replyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="replyer", on_delete=models.CASCADE, blank=True, null=True)
  be_replyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="be_replyer", on_delete=models.CASCADE, blank=True, null=True)
  parent_comment = models.ForeignKey('self', related_name="p_comment", verbose_name="父评论", on_delete=models.CASCADE, blank=True, null=True)
  content = UEditorField('正文', height=100, width=900, imagePath='uploadimg/', filePath='upload/', toolbars='besttome')
  create_time = models.DateTimeField('评论时间', auto_now_add=True, blank=True, null=True)

  def __str__(self):
    return self.content

  class Meta:
    verbose_name = "评论"
    verbose_name_plural = verbose_name