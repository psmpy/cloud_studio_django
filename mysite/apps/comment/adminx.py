import xadmin
from .models import Comments


class CommentsAdmin(object):
  list_display = ['content']


xadmin.site.register(Comments, CommentsAdmin)