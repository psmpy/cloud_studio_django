from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):

  gender_choices = (
    ('male', '男'),
    ('female', '女')
  )

  nick_name = models.CharField('昵称', max_length=50, default='')
  birthday = models.DateField('生日', null=True, blank=True)
  gender = models.CharField('性别', max_length=10, choices=gender_choices, default='male')
  address = models.CharField('地址', max_length=100, default='')
  mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
  image = models.ImageField('头像', upload_to='user/image/%Y%m', default='', max_length=100)

  class Meta:
    verbose_name = '用户信息'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.username

  def get_image_url(self):
    image_url = self.image
    return image_url


class EmailVerifyRecord(models.Model):

  send_choices = (
    ('register', '注册'),
    ('forget', '忘记密码')
  )

  code = models.CharField('验证码', max_length=20)
  email = models.EmailField('邮箱', max_length=50)
  send_type = models.CharField(choices=send_choices, max_length=10)
  send_time = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = '邮箱验证码'
    verbose_name_plural = verbose_name


class Banner(models.Model):
  title = models.CharField('标题', max_length=100)
  image = models.ImageField('轮播图', upload_to="banner/image/%Y%m", max_length=100)
  url = models.URLField('访问地址', max_length=200)
  index = models.IntegerField('访问顺序', default=100)
  add_time = models.DateTimeField('添加时间', auto_now_add=True)

  class Meta:
    verbose_name = '轮播图'
    verbose_name_plural = verbose_name

  
