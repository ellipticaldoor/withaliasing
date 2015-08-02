# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models
import core.core


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=40, serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entryid', models.CharField(max_length=16, default=core.core._createId, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField()),
                ('body_html', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.Entry.get_image, blank=True)),
                ('status', models.CharField(db_index=True, max_length=10, default='draft', choices=[('draft', 'draft'), ('published', 'published')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(related_name='categories', to='blog.Category')),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('imageid', models.CharField(max_length=16, default=core.core._createId, serialize=False, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=blog.models.Image.get_image, blank=True)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ImageEntryLink',
            fields=[
                ('linkid', models.CharField(max_length=33, serialize=False, primary_key=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entry', models.ForeignKey(related_name='entry_link', to='blog.Entry')),
                ('image', models.ForeignKey(related_name='image_link', to='blog.Image')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
