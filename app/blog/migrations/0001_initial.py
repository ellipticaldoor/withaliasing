# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import core.core
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(serialize=False, primary_key=True, max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entryid', models.CharField(default=core.core._createId, serialize=False, primary_key=True, max_length=16)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True, max_length=100)),
                ('body', models.TextField()),
                ('body_html', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=blog.models.Entry.get_image, null=True, blank=True)),
                ('entry_type', models.CharField(max_length=10, default='post', db_index=True, choices=[('post', 'post'), ('howto', 'howto'), ('game', 'game')])),
                ('status', models.CharField(max_length=10, default='draft', db_index=True, choices=[('draft', 'draft'), ('published', 'published')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(related_name='categories', to='blog.Category')),
                ('user', models.ForeignKey(related_name='entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'ordering': ['-created'],
            },
        ),
    ]
