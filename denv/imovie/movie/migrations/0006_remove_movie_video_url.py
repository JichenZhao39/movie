# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 02:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='video_url',
        ),
    ]
