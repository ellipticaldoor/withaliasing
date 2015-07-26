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
                ('slug', models.SlugField(primary_key=True, max_length=40, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='CategoryToEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('category', models.ForeignKey(to='blog.Category')),
            ],
            options={
                'ordering': ['entry'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entryid', models.CharField(default=core.core._createId, primary_key=True, max_length=16, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField()),
                ('body_html', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=blog.models.Entry.get_image, null=True)),
                ('status', models.CharField(default='draft', max_length=10, choices=[('draft', 'draft'), ('published', 'published')], db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(related_name='categories', to='blog.Category')),
                ('user', models.ForeignKey(related_name='entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Entries',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='categorytoentry',
            name='entry',
            field=models.ForeignKey(to='blog.Entry'),
        ),
    ]
