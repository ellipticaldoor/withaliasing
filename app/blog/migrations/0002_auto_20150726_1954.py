# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorytoentry',
            name='category',
        ),
        migrations.RemoveField(
            model_name='categorytoentry',
            name='entry',
        ),
        migrations.DeleteModel(
            name='CategoryToEntry',
        ),
    ]