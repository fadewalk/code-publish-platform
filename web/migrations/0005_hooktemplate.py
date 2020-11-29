# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-05 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_deploytask'),
    ]

    operations = [
        migrations.CreateModel(
            name='HookTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('content', models.TextField(verbose_name='脚本内容')),
                ('hook_type', models.IntegerField(choices=[(2, '下载前'), (4, '下载后'), (6, '发布前'), (8, '发布后')], verbose_name='钩子类型')),
            ],
        ),
    ]
