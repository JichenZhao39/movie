# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 02:05
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_delete_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=''),
        ),
    ]
