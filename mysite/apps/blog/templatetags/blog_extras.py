from django import template
import datetime
from blog.models import Blog 
from comment.models import Comments
from django.contrib.contenttypes.models import ContentType


register = template.Library()

#返回当前类型的实例（如某一篇blog）的评论列表
@register.simple_tag
def get_comments_list(obj):
  #content_type = ContentType.objects.get_for_model(obj)
  #comments = Comments.objects.filter(content_type=content_type, object_id=obj.id).order_by('-create_time')
  comments = obj.blog.all()
  return comments
