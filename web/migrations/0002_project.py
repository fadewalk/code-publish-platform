# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-05 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='项目名')),
                ('repo', models.CharField(max_length=128, verbose_name='仓库地址')),
                ('env', models.CharField(choices=[('prod', '正式'), ('test', '测试')], default='test', max_length=16, verbose_name='环境')),
            ],
        ),
    ]
