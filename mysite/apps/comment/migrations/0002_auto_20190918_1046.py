# Generated by Django 2.2.4 on 2019-09-18 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='be_replyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='be_replyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.Blog'),
        ),
        migrations.AddField(
            model_name='comments',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='评论时间'),
        ),
        migrations.AddField(
            model_name='comments',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='p_comment', to='comment.Comments', verbose_name='父评论'),
        ),
        migrations.AddField(
            model_name='comments',
            name='replyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replyer', to=settings.AUTH_USER_MODEL),
        ),
    ]
